from collections import deque
 
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = {
            'Arad': 366,
            'Bucharest': 0,
            'C': 160,
            'D': 242,
            'Eforle': 161,
            'F': 178,
            'G': 77,
            'H': 151,
            'Lasi': 226,
            'Lugoj': 244,
            'M': 241,
            'N': 234,
            'O': 380,
            'P': 98,
            'R': 193,
            'S': 253,
            'T': 329,
            'U': 80,
            'V': 199,
            'Z': 374,

        }
 
        return H[n]
 
    def Greedy_Search(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])
        poo = {}
        poo[start] = 0
        # print
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
            
        # print("open_lst",open_lst)
        while len(open_lst) > 0:
            n = None
            # print("par", par)
            # print("poo",poo)
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or self.h(v) < self.h(n) :
                    n = v
                # if n not in closed_lst:
                            
                #         closed_lst.add(n)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
                while par[n] != n:
                    reconst_path.append(n)
                    # print("par[n]",par[n])
                    
                    n = par[n]
                # print("reconst_path",reconst_path)
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            # print("poo", poo)
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    # if poo[m] > poo[n] + weight:
                    #     poo[m] = poo[n] + weight
                    #     par[m] = n
 
                        if m in closed_lst:
                            
                            closed_lst.remove(m)
                            open_lst.add(m)
            print("closed_lst",closed_lst)
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None

adjac_lis = {
    'Arad': [('Z', 75), ('S', 140), ('T', 118)],
    'Bucharest': [('U', 85), ('G', 90)],
    'C': [('P', 138), ('D', 120), ('R', 146)],
    'F': [('S', 99), ('Bucharest', 211)],
    'O': [('S', 151), ('Z', 75)],
    'P': [('R', 97), ('Bucharest', 101), ('C', 138)],

    'R': [('S', 80), ('P', 97), ('C', 146)],
    'S': [('R', 80), ('F', 99), ('O', 151), ('Arad', 140)],
    'T': [('Arad', 118), ('Lugoj', 111)],
    'Z': [('O', 75), ('Arad', 75)],
    'Lugoj': [('T', 111), ('M', 70)],
    'M': [('D', 75), ('Lugoj', 70)],
    'D': [('M', 75), ('C', 120)],
    
    
}
graph1 = Graph(adjac_lis)
graph1.Greedy_Search('Arad', 'Bucharest')
