import pandas as pd

# Define the parameter names
parameter_names = [
    'first_parameter', # name of first parameter
    'second_parameter', # name of second parameter
    # Add more parameters as needed
    #'third_parameter', # name of third parameter
    #'fourth_parameter' # name of fourth parameter
]
loss = 'Energy level'
initial_data = {
    parameter_names[0]: [1, 2, 3],
    parameter_names[1]: [5, 6, 7],
    # Add more parameters as needed
    # 'parameter_names[2]: [9, 10, 11],
    loss: [0.1, 0.2, 0.3],
}
df = pd.DataFrame(initial_data)

# Step 2: Save the DataFrame to a CSV file
df.to_csv('history.csv', index=False)