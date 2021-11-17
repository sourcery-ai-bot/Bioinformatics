from algorithms.four_russians_binary_encoding import LCS, Sequence,DNACode
from rosalind.q3a import q3a
from rosalind.q7f import q7f
from algorithms.needleman_wunsch import align_needleman
###########
# Example #
###########
def FourRussianLCS():
    n= 3000
    s1 = Sequence(DNACode,n).random()
    s2 = Sequence(DNACode,n).random()
    print(s1==s2)
    print(LCS(s1,s2))


############
# ROSALIND #
############

q3a()

##############
# Playground #
##############




#FourRussianLCS()

