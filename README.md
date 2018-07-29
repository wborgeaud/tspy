# **tspy**: An optimization package for the traveling salesman problem.
The *tspy* package gives a Python framework in which to study the famous [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP). In this package, one can work on specific instances of the TSP. Approximation methods and lower bounds are included by default. The structure of the package makes it easy to create and include your own methods.

## Installation
The *tspy*  package can be installed using *pip*:
```
pip install tspy
```

## How to use **tspy**
### Creating an instance
To create an instance of the TSP, use:
```python
from tspy import TSP
tsp = TSP()
```
Currently, data can be given to the instance in two ways: by giving it the distance matrix $D \in \mathbb{R}^{N\times N}$ or, in the case of an Euclidian TSP, a data matrix $X \in \mathbb{R}^{N\times P}$ and a distance function.
```python
# Using the distance matrix
tsp.read_mat(D)

# Using the data matrix and a distance function
tsp.read_data(X, dist)
```

### Computing approximate solutions
The module `tsp.solvers` contains algorithms providing approximate solutions of TSP instances. For example, the [2-opt](https://en.wikipedia.org/wiki/2-opt) algorithm gives good solutions rather quickly. Here is how it can be used in the *tspy* package:
```python
from tspy.solvers import TwoOpt_solver
two_opt = TwoOpt_solver(initial_tour='NN', iter_num=100)
two_opt_tour = tsp.get_approx_solution(two_opt)
```
Other solvers are used similarly.

Current solutions are stored in the dictionary `tsp.tours`. If a data matrix has been provided to the instance, a plot of the solution can be shown:
```python
tsp.plot_solution('TwoOpt_solver')
```
![alt text](https://github.com/wborgeaud/tspy/tree/master/imges/two_opt_sol.png)






`tspy` was written by `William Borgeaud <williamborgeaud@gmail.com>`_.
