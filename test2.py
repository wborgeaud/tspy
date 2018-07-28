from tspy import TSP
from tspy.lower_bounds import Simple_LP_bound
from tspy.lower_bounds import Connected_LP_bound
from tspy.lower_bounds import MinCut_LP_bound
from tspy.solvers import TwoOpt_solver
from tspy.solvers import NN_solver
import numpy as np

a = TSP()
a.read_data(np.random.rand(100,2))
a.get_approx_sol(TwoOpt_solver('NN'))

bound = MinCut_LP_bound()

bound.bound(a)
