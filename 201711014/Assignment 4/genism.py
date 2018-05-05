
#Using genism

import gensim
start = timeit.default_timer()
mat= gensim.models.lsimodel.stochastic_svd(X,2,50000)
stop = timeit.default_timer()

#Time taken
print(stop-start)

#Usage of Memory
print(sys.getsizeof(svd))

#sigma (singular value of corpus)
print(mat[1])

#left singular value
print(mat[0])
