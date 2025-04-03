"""
#------------------------------------------------------------------------------- 
Filename:         main.py
Description:      main file for the project
Author:           Nithin Adidela
Date Created:     2025 March 28
Last Modified:    2025 March 28
#------------------------------------------------------------------------------- 
"""

import numpy as np
import matplotlib.pyplot as plt

import grid2D

L = 1.
N = 8

X, Y = grid2D.grid2D(L, N)

Uref = np.sin(np.pi * X) * np.cos(np.pi * Y)
f = -2 * np.pi**2 * np.sin(np.pi * X) * np.cos(np.pi * Y)

plt.contourf(X, Y, Uref, 50, cmap='viridis')
plt.colorbar()
plt.title("Exact Solution to Poisson Equation (Dirichlet BCs)")
plt.xlabel('x')
plt.ylabel('y')
plt.show()