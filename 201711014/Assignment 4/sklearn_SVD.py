from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
import numpy as np
import timeit

# generate a random matrix of user ratings for music items
# users = 1 million
# music items = 5 million

n_users = 10000
n_music_items = 50000

X = sparse_random_matrix(n_music_items,n_users, density=0.01, random_state=45)

#SKLEARN IMPLEMENTATION

svd = TruncatedSVD(n_components=5, n_iter=7, random_state=123)

#normalization and squash the  value between 0 and 1
from sklearn.preprocessing import normalize
x = np.absolute(X)
x_normalized = normalize(x, norm='l1', axis=0)

print(x_normalized)

start = timeit.default_timer()
x_cap = svd.fit(x_normalized)
stop = timeit.default_timer()

print(x_cap)

#Time taken

print(stop-start)

#Usage of Memory

import sys
print sys.getsizeof(svd),sys.getsizeof(X)

##printing the values of the decomposed components

print("VT")
print(svd.components_)  
print("Sigma")
print(svd.singular_values_)

print(svd.explained_variance_ratio_)

start = timeit.default_timer()
x_cap= svd.fit_transform(x_normalized)
stop = timeit.default_timer()

print (x_cap)

print(start-stop)
