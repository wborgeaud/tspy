from tspy import TSP
from tspy.solvers import NN_solver
import numpy as np

a = TSP()
a.read_data(np.random.rand(10,2))

sol = NN_solver(-1)
a.get_approx_sol(sol)

a.plot_solution(0)
