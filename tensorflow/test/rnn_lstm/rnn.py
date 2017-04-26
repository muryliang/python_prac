import numpy as np

X = [1,2]
state = [0.0,0.0]

w_cell_state = np.asarray([[0.1,0.2],[0.3,0.4]])
w_cell_input = np.asarray([0.5,0.6])
b_cell = np.asarray([0.1, -0.1])

w_output = np.asarray([[1.0],[2.0]])
b_output = 0.1

for i in range(len(X)):
    before = np.dot(state, w_cell_state) + X[i]*w_cell_input + b_cell
    state = np.tanh(before)
    final = np.dot(state, w_output) + b_output
    print "before", before
    print "state", state
    print "final", final

