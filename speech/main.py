from svt import processWav
from sklearn.cross_validation import StratifiedKFold
from sklearn import svm
from sklearn.metrics import confusion_matrix
from numpy import array
from math import sin, cos
from decimal import Decimal
from random import random, randint

centroids, frequencies, volumes = processWav('../sample/aaa.wav', 1)
