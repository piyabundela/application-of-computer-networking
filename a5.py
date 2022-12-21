class create_heap:
    def __init__(self, data):
        self.data = data
        self.track = dict()
        for idx in range(0, len(self.data)):
            self.track[idx] = idx
        self.build_heap()
        self.n = len(data)

    def get_parent(self, index):
        return (index - 1) // 2

    def get_left_child(self, index):
        return 2 * index + 1

    def get_right_child(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        return self.data[self.get_parent(index)]

    def left_child(self, index):
        return self.data[self.get_left_child(index)]

    def right_child(self, index):
        return self.data[self.get_right_child(index)]

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]
        self.track[self.data[index1][1]] = index1
        self.track[self.data[index2][1]] = index2

    def heapifyUp(self, index):
        if self.get_parent(index) >= 0 and (self.parent(index)[0] < self.data[index][0]):
            self.swap(self.get_parent(index), index)
            self.heapifyUp(self.get_parent(index))

    def heapifyDown(self, index):
        largest = index
        if self.get_left_child(index) < len(self.data) and (self.data[largest][0] < self.left_child(index)[0]):
            largest = self.get_left_child(index)
        if self.get_right_child(index) < len(self.data) and (self.data[largest][0] < self.right_child(index)[0]):
            largest = self.get_right_child(index)
        if largest != index:
            self.swap(index, largest)
            self.heapifyDown(largest)

    def build_heap(self):
        for i in range((len(self.data) // 2) - 1, -1, -1):
            self.heapifyDown(i)

    def max_heap(self):
        if len(self.data) == 0:
            return
        root = self.data[0]
        lastNode = self.data[len(self.data) - 1]
        self.track[lastNode[1]] = 0
        self.track[root[1]] = '#'
        self.data[0] = lastNode
        self.data.pop()
        self.heapifyDown(0)
        return root

    def enqueue(self, new):
        self.track[len(self.data)] = len(self.data)
        self.data.append(new)
        self.heapifyUp(len(self.data) - 1)

    def printt(self):
        print([i for i in self.data])

    def update(self, index, x):
        if x > self.data[index][0]:
            self.data[index][0] = x
            self.heapifyUp(index)
        elif x < self.data[index][0]:
            self.data[index][0] = x
            self.heapifyDown(index)


class Graph:
    def __init__(self, vrt):
        self.graph = [[] for i in range(vrt)]

    def insert_edge(self, v1, v2, cap):
        self.graph[v1].append((cap, v2))
        self.graph[v2].append((cap, v1))



def minima(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    else:
        return min(a, b)


def findMaxCapacity(n, links, source, target ):
    G = Graph(n)
    for i in range(len(links)):
        (a, b, c) = links[i]
        G.insert_edge(a, b, c)

    heap = create_heap([])

    for j in range(0, n):
        if j == source:
            heap.enqueue([0, source])
        else:
            heap.enqueue([-1, j])

    parent = [None for i in range(n)]

    while heap.data != []:
        maxima = heap.max_heap()
        m = maxima[1]
        if m == target:
            capacity = maxima[0]

        for i in range(len(G.graph[m])):
            j = G.graph[m][i]      #(c,v)
            y = heap.track[j[1]]
            if y != '#':
                x = minima(j[0], maxima[0])
                if x >= heap.data[y][0]:
                    parent[j[1]] = maxima[1]
                    heap.update(y, x)

    path = []
    u = target
    while u!=None:
        path.append(u)
        u = parent[u]
    path.reverse()

    return (capacity, path)

print(findMaxCapacity(10, [(0,1,1), (1,2,2), (2,3,3), (3,4,4), (4,5,5), (5,6,6), (6,7,7), (7,8,8), (8,9,9), (9,5,10), (8,6,11), (4,1,12), (0,6,13), (5,2,14)], 0, 5))