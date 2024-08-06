import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import pandas as pd
import itertools

import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Define the parameter names
parameter_names = [
    'first_parameter', # name of first parameter
    'second_parameter', # name of second parameter
    # Add more parameters as needed
    #'third_parameter', # name of third parameter
    #'fourth_parameter' # name of fourth parameter
]

param_bounds = {
    parameter_names[0]: (10, 200),
    parameter_names[1]: (1, 10),
    # Add more parameters as needed
    #parameter_names[2]: (1e-5, 1e-1),
    #parameter_names[3]: (1e-5, 1e-1),
    #parameter_names[4]: (1e-5, 1e-1)
}

output = 'Energy level'

def generate_parameter_combinations(param_bounds, discretization):
    # Create a list to hold the range of values for each parameter
    param_values = []
    
    for bounds in param_bounds.values():
        param_min, param_max = bounds
        param_values.append(np.linspace(param_min, param_max, discretization))
    
    # Generate all combinations of parameter values
    combinations = list(itertools.product(*param_values))
    
    # Convert to a numpy matrix
    combinations_matrix = np.array(combinations)
    
    return combinations_matrix

discretization = 100  # Change this to your desired discretization level
possible_candidates = generate_parameter_combinations(param_bounds, discretization)


# Load the data from the CSV file
df = pd.read_csv('history.csv')

train_X = df[parameter_names].values
output_Y = df[[output]].values

# Initialize the GP model
kernel = RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=kernel)
gpr.fit(train_X, output_Y)

# Predict for all possible input pairs
_, Y_std = gpr.predict(possible_candidates, return_std=True)
# Find max uncertainty
max_index = np.argmax(Y_std)

# Save the candidate point to a new CSV file
candidate_df = pd.DataFrame(possible_candidates[max_index].reshape(2,1).T, columns=parameter_names)
candidate_df.to_csv('candidate.csv', index=False)

