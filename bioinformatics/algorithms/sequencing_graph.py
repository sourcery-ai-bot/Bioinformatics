
def prefix(i):
    return i[:-1]
def suffix(i):
    return i[1:]


class Graph:
    def __init__(self, nodes:set,edges:dict):
        self.nodes = nodes
        self.edges = edges
        
    def __str__(self):
        output = ""
        for so in self.edges:
            if len(self.edges[so])!=0:
                output += so + " -> " + ",".join(self.edges[so]) + "\n"
        return output.strip()
    
    def __repr__(self):
        return self.__str__()
    
    def copy(self):
        nodes = self.nodes.copy()
        edges = {i:self.edges[i].copy() for i in self.edges}
        return Graph(nodes,edges)
    
    def add_edge(self,a,b):
        if a in self.edges:
            self.edges[a].add(b)
        else:
            self.edges[a] = set([b])
class Overlap_Graph(Graph):
    def __init__(self, patterns):
        nodes = set(patterns)
        edges = {i:set([j for j in patterns if prefix(j)==suffix(i)])for i in patterns}
        Graph.__init__(self,nodes,edges)
    
class DeBruijn_Graph(Graph):
    def __init__(self, nodes,edges):
        Graph.__init__(self,nodes,edges)
        
        

def text_to_debruijn(k,text):
    raw_edges = [(text[i:i+k-1],text[i+1:i+k]) for i in range(len(text)-k+1)]
    nodes = set([i for i,j in raw_edges])
    edges = {i:set() for i in nodes}
    for i,j in raw_edges:
        edges[i].add(j)
    return DeBruijn_Graph(nodes,edges)

def kmers_to_debruijn(kmers):
    raw_edges = [(prefix(mer),suffix(mer)) for mer in kmers]
    nodes = set([i for i,j in raw_edges])
    edges = {i:set() for i in nodes}
    for i,j in raw_edges:
        edges[i].add(j)
    return DeBruijn_Graph(nodes,edges)