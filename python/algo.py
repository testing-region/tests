# implement gradient descent algorithm

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time
import sys
import os
import csv
import pandas as pd
import scipy.stats as stats
import scipy.optimize as optimize
import scipy.interpolate as interpolate
import scipy.integrate as integrate


# compute cost function
def compute_cost(x, y, theta):
    """
    Compute cost for linear regression
    J = compute_cost(x, y, theta) computes the cost of using theta as the
    parameter for linear regression to fit the data points in x and y
    """
    m = len(y) # number of training examples
    J = 0
    h = np.dot(x, theta)
    J = (1/(2*m)) * np.dot((h - y).T, (h - y))
    return J



def gradient_descent(x, y, theta, alpha, m, num_iters):
    """
    Performs gradient descent to learn theta
    theta = gradient_descent(x, y, theta, alpha, m, num_iters) updates theta by
    taking num_iters gradient steps with learning rate alpha
    """
    # Initialize some useful values 
    J_history = np.zeros(num_iters)
    for i in range(num_iters):
        h = np.dot(x, theta)
        theta = theta - alpha * (1/m) * np.dot(x.T, h - y)
        J_history[i] = compute_cost(x, y, theta)
    return theta, J_history

# test
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
theta = np.array([0, 0])
alpha = 0.01
m = len(y)
num_iters = 1000
theta, J_history = gradient_descent(x, y, theta, alpha, m, num_iters)

# print theta to screen
print(theta)