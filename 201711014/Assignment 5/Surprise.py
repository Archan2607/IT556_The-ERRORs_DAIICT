import numpy as np
import surprise  # run 'pip install scikit-surprise' to install surprise
import os
from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise import SVD
from surprise.model_selection import cross_validate

class MatrixFacto(surprise.AlgoBase):
    '''A basic rating prediction algorithm based on matrix factorization.'''
    
    def __init__(self, learning_rate, n_epochs, n_factors):
        
        self.lr = learning_rate  # learning rate for SGD
        self.n_epochs = n_epochs  # number of iterations of SGD
        self.n_factors = n_factors  # number of factors
        self.skip_train = 0
        
    def train(self, trainset):
        '''Learn the vectors p_u and q_i with SGD'''
        
        print('Fitting data with SGD...')
        
        # Randomly initialize the user and item factors.
        p = np.random.normal(0, .1, (trainset.n_users, self.n_factors))
        q = np.random.normal(0, .1, (trainset.n_items, self.n_factors))
        
        # SGD procedure
        for _ in range(self.n_epochs):
            for u, i, r_ui in trainset.all_ratings():
                err = r_ui - np.dot(p[u], q[i])
                # Update vectors p_u and q_i
                p[u] += self.lr * err * q[i]
                q[i] += self.lr * err * p[u]
                # Note: in the update of q_i, we should actually use the previous (non-updated) value of p_u.
                # In practice it makes almost no difference.
        
        self.p, self.q = p, q
        self.trainset = trainset

    def estimate(self, u, i):
        '''Return the estmimated rating of user u for item i.'''
        
        # return scalar product between p_u and q_i if user and item are known,
        # else return the average of all ratings
        if self.trainset.knows_user(u) and self.trainset.knows_item(i):
            return np.dot(self.p[u], self.q[i])
        else:
            return self.trainset.global_mean
            
            
data = surprise.Dataset.load_builtin('ml-1m')
xdict = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)

lst = []
for k in xdict.keys():
    lst.append(xdict[k])
lst = np.array(lst)

rmse2 = np.mean(lst[0])
fittime2 = np.mean(lst[2])


print(rmse2,fittime2)

data = surprise.Dataset.load_builtin('ml-1m')
xdict =cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=4, verbose=True)

lst = []
for k in xdict.keys():
    lst.append(xdict[k])
lst = np.array(lst)

rmse4 = np.mean(lst[0])
fittime4 = np.mean(lst[2])

data = surprise.Dataset.load_builtin('ml-1m')
xdict= cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=6, verbose=True)


data = surprise.Dataset.load_builtin('ml-1m')
xdict= cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=6, verbose=True)

data = surprise.Dataset.load_builtin('ml-1m')
xdict = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=8, verbose=True)


lst = []
for k in xdict.keys():
    lst.append(xdict[k])
lst = np.array(lst)

rmse8 = np.mean(lst[0])
fittime8 = np.mean(lst[2])


#PERFORMANCE RSME ANALYSIS

import matplotlib.pyplot as plt
#plt.hist(lst[0,:])
n_groups=4

rmse=np.array((rmse2,rmse4,rmse6,rmse8))
rmse=tuple(rmse.reshape(1, -1)[0])


plt.plot([5,7.5,8.3,8.75],rmse,'ro')
plt.plot([5,7.5,8.3,8.75],rmse)
plt.xlabel('Data-size (in lakhs)')
plt.ylabel('RMSE')
plt.title('Performance Analysis')

plt.xticks([5,7.5,8.3,8.75])

plt.tight_layout()
plt.show()


#RUNTIME ANALYSIS


import matplotlib.pyplot as plt
#plt.hist(lst[0,:])
n_groups=4

fit=np.array((fittime2,fittime4,fittime6,fittime8))
fit=tuple(fit.reshape(1, -1)[0])

plt.plot([5,7.5,8.3,8.75],fit,'ro')
plt.plot([5,7.5,8.3,8.75],fit)

plt.xlabel('Data-size (in lakhs)')
plt.ylabel('RunTime (in sec)')
plt.title('Performance Analysis')

plt.xticks([5,7.5,8.3,8.75])

plt.tight_layout()
plt.show()


