import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from .solvers.utils import get_cost

class TSP:
    """ Base class for a TSP instance"""

    def __init__(self):
        self.tours = {}

    def read_mat(self, mat):
        self.N = len(mat)
        self.mat = mat
        for i in range(len(mat)):
            self.mat[i,i] = np.inf

    def read_data(self, data, dist = 'euclidean'):
        self.data = data
        mat = squareform(pdist(data,dist))
        self.read_mat(mat)
        
    def plot_data(self):
        if hasattr(self,'data'):
            plt.scatter(*self.data.T)
            plt.show()
        else:
            raise Exception('No 2d data of the instance has been loaded')

    def get_approx_sol(self, solver):
        tour = solver.solve(self)
        print('The cost is {}.'.format(get_cost(tour,self)))
        self.tours[solver.__class__.__name__] = tour

    def plot_solution(self,which):
        if isinstance(which, int):
            which = list(self.tours.keys())[which]
        tour = self.tours[which]
        plt.scatter(*self.data.T)
        for i in range(self.N):
            plt.plot(*self.data[[tour[i],tour[i+1]]].T,'b')
        plt.show()

