from tspy import TSP
from tspy.solvers import NN_solver
from tspy.solvers import TwoOpt_solver
import numpy as np

a = TSP()
N = 150
a.read_data(np.random.rand(N,2))

sol = NN_solver()
a.get_approx_solution(sol)

a.plot_solution('NN_solver')

sol = TwoOpt_solver(list(a.tours.values())[0],500)
a.get_approx_solution(sol)
a.plot_solution('TwoOpt_solver')

