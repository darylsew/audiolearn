from svt import processWav
from sklearn.cross_validation import StratifiedKFold
from sklearn import svm
from sklearn.metrics import confusion_matrix
from numpy import array
from math import sin, cos
from decimal import Decimal
from random import random, randint

ac, af, av = processWav('../pyaudio/aaa.wav', 1)
ec, ef, ev = processWav('../pyaudio/eee.wav', 1)

clf = svm.SVC()
clf.fit(af[:100] + ef[:100], [0 for i in range(100)] + [1 for i in range(100)])
print clf.predict(af[120])
