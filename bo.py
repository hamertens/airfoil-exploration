import pandas as pd
import torch
from botorch.models import SingleTaskGP
from botorch.models.transforms import Normalize, Standardize
from botorch.fit import fit_gpytorch_mll
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.acquisition import UpperConfidenceBound
from botorch.optim import optimize_acqf

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
loss = 'Energy level'

# Load the data from the CSV file
df = pd.read_csv('history.csv')

# Extract the relevant columns and convert them to torch tensors
train_X = torch.tensor(df[parameter_names].values, dtype=torch.double)
loss_Y = torch.tensor(df[[loss]].values, dtype=torch.double)
# Get absolute values of the loss
loss_Y = torch.abs(loss_Y)

# Negate the loss values to convert the minimization problem to a maximization problem
negated_loss_Y = -loss_Y

# Initialize the GP model with the negated loss values
gp = SingleTaskGP(
    train_X=train_X,
    train_Y=negated_loss_Y,
    input_transform=Normalize(d=len(parameter_names)),
    outcome_transform=Standardize(m=1),
)
mll = ExactMarginalLogLikelihood(gp.likelihood, gp)
fit_gpytorch_mll(mll)

# beta value determines exploration-exploitation trade-off. Higher beta values lead to more exploration.
ucb = UpperConfidenceBound(model=gp, beta=4.0)

# Define the bounds for optimization using the parameter bounds
bounds = torch.tensor(
    [[param_bounds[name][0] for name in parameter_names],
     [param_bounds[name][1] for name in parameter_names]],
    dtype=torch.double
)

# Optimize the acquisition function to find the next candidate point
candidate, acq_value = optimize_acqf(
    ucb, bounds=bounds, q=1, num_restarts=5, raw_samples=20,
)

# Save the candidate point to a new CSV file
candidate_df = pd.DataFrame(candidate.numpy(), columns=parameter_names)
candidate_df.to_csv('candidate.csv', index=False)



