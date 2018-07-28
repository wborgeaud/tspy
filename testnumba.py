from tspy import TSP
from tspy.solvers import TwoOpt_solver
from tspy.lower_bounds import Held_Karp
from tspy.lower_bounds import Connected_LP_bound
import numpy as np

a = TSP()
N = 100
a.read_data(np.random.rand(N,2))
sol = TwoOpt_solver('NN')
a.get_approx_solution(sol)

a.get_lower_bound(Connected_LP_bound())
a.get_lower_bound(Held_Karp(n_iter=500, batch_size=50))

