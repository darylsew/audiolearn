from sklearn import svm
from sklearn.metrics import confusion_matrix
from numpy import array
from math import sin, cos
from decimal import Decimal
from random import random, randint

labeled_points = []
for i in range(0, 1000):
    # generate random point in the domain [-5,5]
    xval = random()*10 - 5

    # randomly choose if it will be sin, cos, or x**2 functype = randint(0,2) 
    functype = randint(0, 2)
    if functype == 0: # cos
        yval = cos(xval)
    elif functype == 1: # sin
        yval = sin(xval)
    elif functype == 2: # x**2
        yval = xval**2

    xval = Decimal(xval).quantize(Decimal('.001'))
    yval = Decimal(yval).quantize(Decimal('.001'))
    labeled_points.append([xval,yval,functype])
    
# create anonymized data
labels = [ p[2] for p in labeled_points ] 

unlabeled_points = [ p[:2] for p in labeled_points ]
unlabeled_points = array(unlabeled_points)
labels = array(labels)

clf = svm.SVC()
clf.fit(unlabeled_points, labels)
import pdb; pdb.set_trace()
# Type clf.predict([x, y]) to get info on the type of function!
