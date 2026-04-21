"""Functions used in Exercise 8 and 9 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import numpy as np

# Define your new functions below
def gaussian(mu, sigma, x):
    coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return coefficient * exponent #returns the value

def chi_squared(observed, expected, sigma):
    N = len(observed)
    residuals = (observed - expected) ** 2
    chi2 = (residuals / sigma**2).sum() / N
    return chi2

def linregress (x, y):
    delta = (len(x) * (x**2).sum()) - (x.sum()**2)
    A = (((x**2).sum() * y.sum()) - (x.sum() * (x*y).sum())) / delta
    B = ((len(x)*(x*y).sum()) - (x.sum() * y.sum())) / delta
    return A, B

def pearson(x, y):
    x_mean = x.mean()
    y_mean = y.mean()

    numerator = ((x - x_mean) * (y - y_mean)).sum()
    denominator = np.sqrt(((x - x_mean) ** 2).sum() * ((y - y_mean) ** 2).sum())

    r = numerator / denominator
    return r

