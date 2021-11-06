from algorithms.four_russians_binary_encoding import LCS, Sequence,DNACode
from rosalind.q7f import q7f
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

q7f()

##############
# Playground #
##############


#FourRussianLCS()
