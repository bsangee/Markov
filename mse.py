#Number of requests for which we obtain least MSE (only requests of length 2, 4 and 8 are considered)
from parse import parser
import states
import chained
import numpy as np

from sklearn.metrics import mean_squared_error

order = 2
y_true=[]
y_pred=[]
mse = []

p = parser()
p.parse_file()  #File name can be changed in parse.py
text = p.write_bytes
text = states.write_bytes_states(text)

pred =chained.markov_chain(text[:2],order)
print pred
y_true.append(np.float(text[3]))
y_pred.append(np.float(pred[0]))
mse.append(mean_squared_error(y_true, y_pred))
for i in xrange(4,8,2):
        pred =chained.markov_chain(text[:i],order)
        y_true=[]
        y_pred=[]
        y_true.append([float(s) for s in (text[i+1:(2*i - 1)])])
        y_pred.append([float(s) for s in (pred[:i-2])])
        mse.append(mean_squared_error(y_true, y_pred))


print 'Optimal Length:' + str( (mse.index(min(mse)) * 2 + 2) )
