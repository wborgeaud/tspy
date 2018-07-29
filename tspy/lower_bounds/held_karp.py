from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
from .utils import get_cost
import matplotlib.pyplot as plt

class Held_Karp:

    def __init__(self, n_iter=100, batch_size=10, alp_factor=0.95, start_alp=2,
                 remove_node=0):
        self.n_iter = n_iter
        self.batch_size = batch_size
        self.alp_factor = alp_factor
        self.remove_node = remove_node
    
    def bound(self,tsp):
        N = tsp.N
        mat = tsp.mat
        C = np.max(mat[mat!=np.inf])/1000
        vec = np.random.uniform(-C,C,N)
        ans = [0]
        U = get_cost(tsp.get_best_solution(),tsp)
        alp = 2
        for _ in range(self.n_iter):
            if _!=0 and _%self.batch_size==0:
                alp = self.alp_factor * alp
            matN = np.copy(mat)
            for i in range(N):
                matN[i]-=vec[i]
                matN[:,i]-=vec[i]
            mat0 = np.delete(matN,self.remove_node,0)
            mat0 = np.delete(mat0,self.remove_node,1)
            tree = np.where(minimum_spanning_tree(mat0).toarray()!=0)
            ans.append(sum(mat0[minimum_spanning_tree(mat0).toarray()!=0]) + sum(sorted(matN[i])[:2]) + 2*sum(vec))
            inter = np.array([sum(tree[0]==i) + sum(tree[1]==i) for i in range(N-1)])
            coef = alp*(U-ans[-1])/(np.sum((2-inter)**2))
            coef = 0.001
            ran = np.append(np.arange(0,self.remove_node),np.arange(self.remove_node+1,N))
            vec[ran] = vec[ran] + coef * (2-inter)    
        print('The lower bound is ', max(ans))
        plt.plot(ans)
        plt.show()
