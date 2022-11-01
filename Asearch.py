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
            'Craiova': 160,
            'Dobreta': 242,
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
 
    def a_star_algorithm(self, start, stop):
        # Và closed_lst là danh sách các nút đã được truy cập
        # Trong open_lst này là một tập hợp các nút đã được truy cập
        open_lst = set([start])
        closed_lst = set([])
        # poo có khoảng cách hiện tại từ đầu đến tất cả các nút khác
         # giá trị mặc định là + infinity
        poo = {}
        poo[start] = 0
        par = {}
        par[start] = start
            
        print("open_lst",open_lst)
        while len(open_lst) > 0:
            n = None
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v
 
            if n == None:
                print('Path does not exist!')
                return None
            # nếu nút hiện tại là điểm dừng
            # sau đó chúng ta bắt đầu lại từ đầu
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
            # print("n",n)
            print(self.get_neighbors(n))
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            
                            closed_lst.remove(m)
                            open_lst.add(m)
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None

adjac_lis = {
    'Arad': [('Z', 75), ('S', 140), ('T', 118)],
    'Bucharest': [('U', 85), ('G', 90)],
    'Craiova': [('P', 138)],
    'F': [('S', 99), ('Bucharest', 211)],
    'O': [('S', 151), ('Z', 75)],
    'P': [('R', 97), ('Bucharest', 101), ('Craiova', 138)],

    'R': [('S', 80), ('P', 97), ('Craiova', 146)],
    'S': [('R', 80), ('F', 99), ('O', 151), ('Arad', 140)],
    'T': [('Arad', 118), ('Lugoj', 111)],
    
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('Arad', 'Bucharest')
