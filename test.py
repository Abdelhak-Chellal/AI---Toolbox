from toolbox import *

problem = Problem([("A", "B"), ("B", "C"), ("C", "A"), ("3", "5"), ("C", "G"), ("C", "M"), ("N", "A"), ("V", "5"), ("5", "C")])

edge = []
edge.append("S")
edge.append("A")

problem.add_an_edge(edge)
t = toolbox(problem)
#test functions here
#remove ["A", "B"]
t.animate_solution(["A", "B"])


