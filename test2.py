from tspy import TSP
from tspy.lower_bounds import Simple_LP_bound
from tspy.lower_bounds import Connected_LP_bound
from tspy.lower_bounds import MinCut_LP_bound
from tspy.solvers import TwoOpt_solver
from tspy.solvers import NN_solver
import numpy as np

a = TSP()
N = 20
print(N)
a.read_data(np.random.rand(N,2))
a.get_approx_solution(TwoOpt_solver('NN'))
a.get_approx_solution(NN_solver())

bounds = [Simple_LP_bound(),Connected_LP_bound(),MinCut_LP_bound()]

for b in bounds:
    a.get_lower_bound(b)

print(a.lower_bounds)

a.get_best_solution()
a.get_best_lower_bound()
