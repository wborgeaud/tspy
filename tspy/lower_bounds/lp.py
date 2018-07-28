import numpy as np
from cvxopt import matrix, solvers, sparse, spmatrix
from scipy.sparse.csgraph import connected_components
import networkx as nx



class Simple_LP_bound:

    def bound(self, tsp):
        sol = _lp(tsp.mat,[])
        sol['x'] = _clean_sol(sol['x'])
        self.sol = sol
        return sol

class Connected_LP_bound:

    def bound(self, tsp):
        opt_res = Simple_LP_bound().bound(tsp)
        sol = opt_res['x']
        N = tsp.N
        mat = tsp.mat
        SS = []
        k = 2
        while k>1:
            graph = np.zeros((N,N))
            count=0
            for i in range(N):
                for j in range(i+1,N):
                    if sol[count]>0:
                        graph[i,j] = 1
                        graph[j,i] = 1
                    count+=1
            CC = connected_components(graph,directed=False)
            k = CC[0] 
            if k == 1:
                if not SS:
                    self.constraints = SS
                    self.sol = opt_res
                    return opt_res
                break
            for i in range(k):
                SS.append(np.arange(N)[CC[1]==i])
            opt_res = _lp(mat, SS)
            sol = _clean_sol(opt_res['x'])
            opt_res['x'] = sol
        self.constraints = SS
        self.sol = opt_res
        return opt_res

class MinCut_LP_bound:

    def bound(self,tsp):
        conn = Connected_LP_bound()
        opt_res = conn.bound(tsp)
        if not conn.constraints:
            return opt_res
        SS = conn.constraints
        sol = opt_res['x']
        N = tsp.N
        mat = tsp.mat
        k = 1
        while k<1.95:
            graph = np.zeros((N,N))
            count=0
            for i in range(N):
                for j in range(i+1,N):
                    graph[i,j] = sol[count]
                    graph[j,i] = sol[count]
                    count+=1
            CC = connected_components(graph,directed=False)
            is_not_conn = CC[0]!=1
            while is_not_conn:
                for ii in range(CC[0]):
                    SS.append(np.arange(N)[CC[1]==ii])
                opt_res = _lp(mat,SS)
                opt_res['x'] = _clean_sol(opt_res['x'])
                sol = opt_res['x']
                graph = np.zeros((N,N))
                count=0
                for i in range(N):
                    for j in range(i+1,N):
                        if sol[count]>0:
                            graph[i,j] = 1
                            graph[j,i] = 1
                        count+=1
                CC = connected_components(graph,directed=False)
                is_not_conn = CC[0]!=1
            cut = nx.stoer_wagner(nx.Graph(graph))
            k = cut[0]
            if k>1.95:
                break
            part = cut[1]
            smpart = part[0] if len(part[0])<len(part[1]) else part[1]
            SS.append(smpart)
            opt_res = _lp(mat,SS)
            opt_res['x'] = _clean_sol(opt_res['x'])
            sol = opt_res['x']
        self.sol = opt_res
        return opt_res


def _lp(mat,SS):
    N = len(mat)
    dim = int(N * (N-1) / 2 )
    count = 0
    c = []
    dic = {}
    for i in range(N):
        for j in range(i+1,N):
            dic[(i,j)] = count
            count+=1
            c.append(mat[i,j])
    c = np.array(c)
    A_eq = np.zeros(dim)
    b_eq = []
    for i in range(N):
        new = np.zeros(dim)
        for j in range(i):
            new[dic[(j,i)]] = 1
        for j in range(i+1,N):
            new[dic[(i,j)]] = 1
        A_eq = np.vstack([A_eq, new])
        b_eq.append(2)
    b_eq = np.array(b_eq)
    A_eq = A_eq[1:]
    A_up = sparse([spmatrix(1.0,range(dim),range(dim)), spmatrix(-1.0,range(dim),range(dim))])
    b_up = np.append(np.ones(dim),np.zeros(dim))
    for S in SS:
        A_up, b_up = add_cut(S,A_up,b_up,dic,N)
    c = matrix(c)
    b_up = matrix(b_up.reshape(-1,1),(len(b_up),1),'d')
    A_eq = sparse(matrix(A_eq))
    b_eq = matrix(b_eq.reshape(-1,1),(len(b_eq),1),'d')
    solvers.options['show_progress'] = False
    sol = solvers.lp(c,A_up,b_up,A_eq,b_eq)
    return sol

def add_cut(S,A_up,b_up,dic,N):
    dim = A_up.size[1]
    new = np.zeros(dim)
    for j in [yy for yy in range(N) if yy not in S]:
        for sam in S:
            sm, bi = min([j,sam]),max([j,sam])
            new[dic[(sm,bi)]] = 1
    new = matrix(new.reshape(1,-1),(1,len(new)),'d')
    A_up = sparse([A_up,-new])
    b_up = np.append(b_up,-2)
    return A_up, b_up

def _clean_sol(vect):
    vect = np.array(vect).ravel()
    vect = np.round(vect,5)
    vect = np.abs(vect)
    return vect
