from graphviz import *

# Define DFA transitions
transitions = {(0, 'a'): 1, (0, 'b'): 0, (1, 'a'): 0, (1, 'b'): 1}

# Create new graph
dot = Digraph(format='png')

# Add nodes
dot.node('a', 'Machine Learning Errors')

dot.node('b', 'RMSE')

dot.node('c', 'MAE')
# Add edges
dot.edges(['ab', 'ac'])
print(dot.source)
# Render the graph to a file or display it
dot.render('try', format='png')
