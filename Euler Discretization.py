#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Differential equation: dy/dt = y
def f(t, y):
    return y

# Starting value
t0, y0 = 0, 1
# Step size
h = 0.1
# Number of steps
n_steps = 20

# Calculation with Euler method
t_values = [t0]
y_values = [y0]

t, y = t0, y0
for _ in range(n_steps):
    y = y + h * f(t, y)
    t = t + h
    t_values.append(t)
    y_values.append(y)

# The aactual solution
t_real = np.linspace(0, 2, 100)
y_real = np.exp(t_real)

# Graphic drawing
plt.plot(t_values, y_values, 'b-o', label='Euler Method')
plt.plot(t_real, y_real, 'r-', label='Actual Solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('Numerical Solution with Euler Method')
plt.show()


# In[ ]:




