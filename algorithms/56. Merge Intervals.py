#sorting method time-O(nlogn) space O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n==0:
            return intervals
        i=0
        intervals.sort(key=lambda x:(x[0],x[1]))
        while i<n-1:
            s = intervals[i][0]
            e = intervals[i][1]
            sn = intervals[i+1][0]
            en = intervals[i+1][1]
            print(i,intervals)
            while i<n-1 and e>=sn:
                intervals[i][1] = en if en>e else e
                del intervals[i+1]
                n-=1
                if i<n-1:
                    s = intervals[i][0]
                    e = intervals[i][1]
                    sn = intervals[i+1][0]
                    en = intervals[i+1][1]
                else:
                    break
            i+=1
        return intervals
###################################################################################
#connected component sol - space/runtime O(n^2)
class Solution:
    def overlap(self, a, b): #START <= NEXT_END AND END>=NEXT_START
        return a[0] <= b[1] and a[1]>=b[0]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)
        #BUILD CONNECTED COMPONENTS = OVERLAPPING EDGES ARE CONNECTED COMPONENTS
        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):    #CHECK FOR OVERLAPPING EDGES
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]

            
            
