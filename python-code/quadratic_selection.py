#quadratic variable selection



#
# TODO: See if the coefficents of LR change much across the groups.

#

from itertools import combinations

execfile("data_exploring.py")


vdata = data.values
ix = []
n,d = vdata.shape
print vdata.shape
#there are d*(d-1)/2 different combinations.

qdata = np.zeros( (n, d*(d-1)/2 ) )

for col_pos, comb in enumerate( combinations( range(d), 2) ):
    i = comb[0]
    j = comb[1]
    qdata[:, col_pos] = vdata[:,i]*vdata[:,j]
    ix.append( (i,j) )
    print col_pos 

    
lr = sklm.Lasso( alpha = .0005, normalize = True)

