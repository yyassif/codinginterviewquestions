#sol from https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/call_center/call_center.ipynb
from abc import ABCMeta, abstractmethod
from enum import Enum
class Rank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2
class Employee(metaclass=ABCMeta):
    def __init__(self, employee_id, name, rank, call_center):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.call = None
        self.call_center = call_center
    def take_call(self, call):
        self.call = call
        self.call.employee = self
        self.call.state = CallState.IN_PROGRESS
    def complete_call(self):
        self.call.state = CallState.COMPLETE
        self.call_center.notify_call_completed(self.call)
    @abstractmethod
    def escalate_call(self):
        pass
    def _escalate_call(self):
        self.call.state = CallState.READY
        call = self.call
        self.call = None
        self.call_center_call_escalated(call)
class CallState(Enum):
    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2
class Call(object):
    def __init__(self,rank):
        self.employee = None
        self.state = CallState.READY
        self.rank = rank

class CallCenter(object):
    def __init__(self,operators, supervisors, directors):
        self.operators = operators
        self.supervisors = supervisors
        self.directors = directors
        self.queued_calls = []
    def _dispatch_call(self, call, employees): #helper function for dispatch call
        for employee in employees:
            if employee.call is None:
                employee.take_call(call)
                return employee
        return None
    #when a call is dispatched, go through all employees by rank to see if anyone is available
    def dispatch_call(self,call):
        if call.rank not in {Rank.OPERATOR, Rank.SUPERVISOR, Rank.DIRECTOR}:
            raise ValueError("invalid call rank")
        employee=None
        if call.rank == Rank.OPERATOR:
            employee = self._dispatch_call(call, self.operators)
        if call.rank == Rank.SUPERVISOR:
            employee = self._dispatch_call(call, self.supervisors)
        if call.rank == Rank.DIRECTOR:
            employee = self._dispatch_call(call, self.directors)
        if employee is None:
            self.queued_calls.append(call) #everyone is busy - que the call

class Operator(Employee):
    def __init__(self, employee_id, name):
        super(Operator, self).__init__(employee_id, name, Rank.OPERATOR)
    def escalate_call(self):
        self.call.level = Rank.SUPERVISOR
        self._escalate_call()
class Supervisor(Employee):
    def __init__(self, employee_id,name):
        super(Operator, self).__init__(employee_id, name, Rank.SUPERVISOR)

    def escalate_call(self):
        self.call.level = Rank.DIRECTOR
        self._escalate_call()

class Director(Employee):
    def __init__(self, employee_id,name):
        super(Operator, self).__init__(employee_id, name, Rank.OPERATOR)

    def escalate_call(self):
        raise NotImplemented('directors handle every call')

