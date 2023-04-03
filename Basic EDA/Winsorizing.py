
import numpy as np

def winsorize(arr, limits):
    '''
    Winsorize the values in an array.
    arr: numpy array
    limits: tuple, representing the lower and upper percentile limits
    '''
    lower_limit, upper_limit = np.percentile(arr, limits)
    arr[arr < lower_limit] = lower_limit
    arr[arr > upper_limit] = upper_limit
    return arr
