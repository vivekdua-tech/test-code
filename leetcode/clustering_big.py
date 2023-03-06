

'''''''''''''''''''''

import itertools


# from util.app.union_find import UnionFind


class UnionFind:
    """An implementation of union-find data structure by rank.
    """

    def __init__(self, n):
        """Initialize an union-find with n items(objects).
        """
        self.root = list(range(n))
        self.rank = [0] * n
        self.num = n  # the number of clusters

    def find(self, x):
        """Find the root(pointer) of the item x. Using path compression.
        """
        s_list = self.root
        if s_list[x] != x:
            s_list[x] = self.find(s_list[x])
        return s_list[x]

    def count(self):
        return self.num

    def union(self, x, y):
        """Union x and y.
        """
        s = self.root
        rank_list = self.rank

        s1 = self.find(x)
        s2 = self.find(y)

        if s1 == s2:
            return

        self.num -= 1
        if rank_list[s1] == rank_list[s2]:
            s[s2] = s1
            rank_list[s1] += 1
        elif rank_list[s1] > rank_list[s2]:
            s[s2] = s1
        else:
            s[s1] = s2

    def connected(self, x, y):
        """Check if x and y are in the same cluster.
        """
        return self.find(x) == self.find(y)


class BigClusterFinder:

    def __init__(self, input_file):
        with open(input_file, "r") as file:
            nodes, bits_per_node = file.readline().split()
            self._size = int(nodes)
            self._bits = int(bits_per_node)
            self._numbers = {}
            for node in range(1, self._size + 1):
                line = file.readline().split()
                bits = tuple((int(num) for num in line))
                num = 0
                for index, bit in enumerate(bits[::-1]):
                    num += bit * (2 ** index)
                if num in self._numbers:
                    self._numbers[num].append((node, bits))
                else:
                    self._numbers[num] = [(node, bits)]

    def find_number_of_clusters(self):
        uf = UnionFind(self._size)
        distances = [2 ** i for i in range(self._bits)]
        distances.extend([-num for num in distances])
        for pair in itertools.combinations(distances, 2):
            bit_1, bit_2 = pair
            distances.append(bit_1 + bit_2)
        distances = [0] + distances
        unions_zero, unions_one, unions_two = [], [], []
        for distance in distances:
            for i in self._numbers.keys():
                if (i + distance) in self._numbers:
                    for node_from, bits_from in self._numbers[i]:
                        for node_to, bits_to in self._numbers[i + distance]:
                            if self._hamming(bits_from, bits_to) == 0:
                                unions_zero.append((node_from, node_to))
                            elif self._hamming(bits_from, bits_to) == 1:
                                unions_one.append((node_from, node_to))
                            elif self._hamming(bits_from, bits_to) == 2:
                                unions_two.append((node_from, node_to))
        self._make_unions(uf, unions_zero)
        self._make_unions(uf, unions_one)
        self._make_unions(uf, unions_two)
        return uf.count

    @staticmethod
    def _hamming(bits_from, bits_to):
        hamming = 0
        for index, bit in enumerate(bits_from):
            if bit != bits_to[index]:
                hamming += 1
        return hamming

    @staticmethod
    def _make_unions(uf, unions_zero):
        for node_from, node_to in unions_zero:
            if not uf.connected(node_from, node_to):
                uf.union(node_from, node_to)


if __name__ == "__main__":
    cluster_finder = BigClusterFinder("clustering_big.txt")
    print(cluster_finder.find_number_of_clusters())

'''''''''''''''''''''''



f = open('clustering_big.txt', 'r')

f.readline()
ls = f.readline()
graph = []
while ls:
    graph += [ls[:-1].replace(' ', '')]
    ls = f.readline()
f.close()

graph = list(set(graph))
N = len(graph)
gn = [int(i, 2) for i in graph]


def nb(v):
    n = 24
    data = []
    for i in range(n):
        s = list(v)
        s[i] = '1' if s[i] == '0' else '0'
        data += [int(''.join(s), 2)]
        for j in range(i+1, n):
            ss = s.copy()
            ss[j] = '1' if ss[j] == '0' else '0'
            data += [int(''.join(ss), 2)]
    return data


uf = {i: i for i in gn}
rank = {i: 0 for i in gn}


def find(i):
    global uf
    if uf[i] == i:
        return i
    elif uf[uf[i]] == uf[i]:
        return uf[i]
    else:
        newi = uf[i]
        while uf[newi] != newi:
            newi = uf[newi]
        uf[i] = newi
        return newi


def merge(i, j):
    global uf, rank
    i, j = find(i), find(j)
    if i != j:
        if rank[i] > rank[j]:
            uf[j] = i
        elif rank[i] < rank[j]:
            uf[i] = j
        else:
            uf[j] = i
            rank[i] += 1


for s in range(N):
    if s % 10000 == 0:
        print('scan %i, size=%i' % (s+1, len(set(uf.values()))))
    for vn in nb(graph[s]):
        if vn in uf:
            merge(gn[s], vn)

for i in uf:
    find(i)
print('DONE, cluster size=%i' % len(set(uf.values())))