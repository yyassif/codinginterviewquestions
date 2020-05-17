from threading import Lock
class Foo:
    def __init__(self):
        self.firstLock = Lock()  #careful not to name variables same as method names
        self.secondLock = Lock()
        self.firstLock.acquire()
        self.secondLock.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None: 
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstLock.release()
            

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstLock:
            printSecond()
            self.secondLock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondLock:
            printThird()
