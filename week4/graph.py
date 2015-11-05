# /usr/bin/network python
import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo, glib
from gtk import gdk
import gobject
import random as r
import copy as cop
import os
import numpy as np
import time
import pickle

from scipy.special import expit, logit

np.set_printoptions(precision=4)

## Above is stuff copy-pasted from network.py

# Below is stuff we import to print stuff out in nice graphs
import matplotlib.pyplot as plt

# Obviously you can change the filename I used below
#f = open('errors10.txt', 'rb' ) #Open a file for reading

errors = [line.rstrip('\n') for line in open('errors1000.txt', 'rb' )] # load errors in a way that I hope Windows likes!
     
plt.plot(errors)
plt.ylabel('RMS Error')
plt.xlabel('Epochs')
plt.show()