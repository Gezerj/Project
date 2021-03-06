# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:59:34 2016

@author: Admin
"""
from __future__ import division
import numpy as np 
import scipy.constants as sc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from Verlet_main import *

E = np.abs((Esum[0] - Esum[:])/Esum[0])

plt.close('all')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(A[:, 0], A[:, 1], A[:, 2], 'o'); plt.plot(B[:, 0], B[:, 1], B[:, 2]); plt.plot(C[:, 0], C[:, 1], C[:, 2])


fig = plt.figure()
plt.plot(A[:, 0], A[:, 1], 'o'); plt.plot(B[:, 0], B[:, 1]); plt.plot(C[:, 0], C[:, 1])


plt.ylabel(r'Distance $(AU)$')
plt.xlabel(r'Distance $(AU)$')

plt.figure()
plt.plot(T, E, color='blue')
plt.xlabel("Time (yrs)")
plt.ylabel("Energy (J)")
plt.title("Graph of Total energy of system")

plt.figure()
plt.plot(T, Esum, color='blue', label='Total'); plt.plot(T, Ea, color='red', label='Sun'); plt.plot(T, Eb, color='green', label='Earth'); plt.plot(T, Ec, color='pink', label='Moon')
plt.legend(loc='best')
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.title("Graph of Energy of system")

plt.figure()
plt.plot(T, Ea/Esum, color='red', label='Sun'); plt.plot(T, Eb/Esum, color='green', label='Earth'); plt.plot(T, Ec/Esum, color='pink', label='Moon')
plt.legend(loc='best')
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.title("Graph of Energy Ratio of system")

plt.show()




