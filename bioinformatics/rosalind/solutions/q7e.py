from algorithms.distance_matrix import DistanceMatrix
from algorithms.limb_length import limb_length_n
from algorithms.additive_phylogeny import additive_phylogeny
from algorithms.neighbour_joining import neighbour_joining
def q7e():
    i = "src/rosalind/io/i.txt"
    o = "src/rosalind/io/o.txt"
    with open(i,"r") as f:
        n = int(f.readline())
        mat = [list(map(int,f.readline().strip().split())) for _ in range(n)]
        d_mat = DistanceMatrix(mat,list(map(str,range(n))))
        f2 = open(o,"w+")
        f2.writelines(str(neighbour_joining(d_mat)))
    f2.close()