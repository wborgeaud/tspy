""" 2-opt heuristic for TSP """

import numpy as np
from .utils import get_cost
from .nearest_neighbor import NN_solver


class TwoOpt_solver:

    def __init__(self, initial_tour, iter_num=100):
        """
        Parameters
        ----------
        initial_tour : permutation of the nodes
                       Starting tour on which to apply 2-opt
        iter_num : int
                   Number of iterations in the local 2-opt search
        """
        self.initial_tour = initial_tour
        self.iter_num = iter_num
    def solve(self, tsp):
        if self.initial_tour == 'NN':
            self.initial_tour = NN_solver().solve(tsp)

        best_tour = self.initial_tour
        old_best = np.inf
        for _ in range(self.iter_num):
            best = get_cost(best_tour,tsp)
            tour = best_tour[:]
            for i in range(tsp.N):
                maxx = tsp.N if i!=0 else tsp.N-1
                for j in range(i+2,maxx):
                    ftour = tour[:]
                    j1 = j+1
                    if tsp.mat[ftour[i],ftour[i+1]] + tsp.mat[ftour[j],ftour[j1]] > tsp.mat[ftour[i],ftour[j]] + tsp.mat[ftour[i+1],ftour[j1]]:
                        ftour[i+1: i+j-i+1]= list(reversed(ftour[i+1:j1]))
                        cost = get_cost(ftour,tsp)
                        if cost<best:
                            best = cost
                            best_tour = ftour
            if best == old_best:
                return best_tour
            else:
                old_best = best
        return best_tour




