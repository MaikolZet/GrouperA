import numpy as np

def result(x,y):
    xy = np.zeros((len(x[:,0]),len(x[0,:])))
    for i in range(0,len(xy[:,0])):
        for j in range(0,len(xy[0,:])):
            xy[i,j] = y[int(x[i,j])]
    counter = []
    perf = sum(y)/len(xy)
    for i in range(0,len(xy[:,0])):
        counter.append(abs(sum(xy[i,:])-perf))
    return sum(counter)