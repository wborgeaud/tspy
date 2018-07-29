# tspy: An optimization package for the traveling salesman problem.
The *tspy* package gives a Python framework in which to study the famous [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) (TSP). In this package, one can work on specific instances of the TSP. Approximation methods and lower bounds are included by default. The structure of the package makes it easy to create and include your own methods.

## Installation
The *tspy*  package can be installed using *pip*:
```
pip install tspy
```

## How to use tspy
### Creating an instance
To create an instance of the TSP, use:
```python
from tspy import TSP
tsp = TSP()
```
Currently, data can be given to the instance in two ways: by giving it the *NxN* distance matrix *D* or, in the case of an Euclidian TSP, a *NxP* data matrix *X* and a distance function.
```python
# Using the distance matrix
tsp.read_mat(D)

# Using the data matrix and a distance function
tsp.read_data(X, dist)
```

### Computing approximate solutions
The module `tsp.solvers` contains several algorithms providing approximate solutions of TSP instances. For example, the [2-opt](https://en.wikipedia.org/wiki/2-opt) algorithm gives good solutions rather quickly. Here is how it can be used in the *tspy* package:
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
![alt text](https://github.com/wborgeaud/tspy/blob/master/images/two_opt_sol.jpg)

At any point, the best solution that has been computed can be retrieved:
```python
best_tour = tsp.get_best_solution()
```

### Computing lower bounds
The TSP being *NP-hard*, it is difficult to get exact solutions for large instances. However, by computing lower bounds we can know how good our approximations are. The *tspy* package provides several lower bounds methods. One example is given by the `Simple_LP_bound` which gives the optimal solution of the [LP relaxation](https://en.wikipedia.org/wiki/Linear_programming_relaxation) of the TSP:
```python
from tspy.lower_bounds import Simple_LP_bound
lower_bound = tsp.get_lower_bound(Simple_LP_bound())
```
At any point, the best lower bound that has been computed can be retrieved:
```python
best_lower_bound = tsp.get_best_lower_bound()
```

## Future
The following features will be added soon:
- Genetic programming 
- Ant colony optimization
- Lin–Kernighan heuristic
- Better LP lower bounds

Feel free to contact me if you would like to contribute.


## Author
*tspy* was written by William Borgeaud (williamborgeaud[at]gmail.com).
