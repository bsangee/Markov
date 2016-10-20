#IN PPROGRESS
from parse import parser
import states
import chained
import numpy as np

from sklearn.metrics import mean_squared_error

order = 2
y_true=[]
y_pred=[]

p = parser()
p.parse_file()  #File name can be changed in parse.py
text = p.write_bytes
text = states.write_bytes_states(text)
pred =chained.markov_chain(text[:2],order)
y_true.append(np.float(text[3]))
y_pred.append(np.float(pred[0]))
print mean_squared_error(y_true, y_pred)

pred =chained.markov_chain(text[:4],order)
y_true=[]
y_pred=[]
y_true.append([float(s) for s in (text[5:7])])
y_pred.append([float(s) for s in (pred[:2])])
print mean_squared_error(y_true, y_pred)

pred =chained.markov_chain(text[:8],order)
y_true=[]
y_pred=[]
y_true.append([float(i) for i in (text[9:13])])
y_pred.append([float(i) for i in (pred[:4])])
print mean_squared_error(y_true, y_pred)


#print pred
