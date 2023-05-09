
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
''' Here's an example usage:
    Create a numpy array with random values '''
arr = np.random.rand(10)

''' Winsorize the array to keep only values within the 10th and 90th percentiles '''
winsorized_arr = winsorize(arr, (10, 90))

''' In this example, the winsorize function takes in a numpy array and a tuple representing the lower and upper percentile limits. 
# It calculates the percentile limits using the np.percentile function, then replaces any values in the array that are outside those limits with the limit value. 
# Finally, it returns the winsorized array.
