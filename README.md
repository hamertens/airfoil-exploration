# airfoil-exploration

**Bayesian Optimization**

Create anaconda environment from yml file by running
```
conda env create -f exploration.yml -n exploration
```
Activate environment
‘conda activate exploration’
Or ‘source activate exploration’ if that doesn’t work
Define names of parameters in first_run.py and bo.py by adjusting strings in list ‘parameter_names’ - works with any number of parameters
Define initial training data in first_run.py by adjusting values in dictionary ‘initial_data’
Currently there are 3 data-points - at least 1 is needed
Run first_run.py - creates history.csv file
Run bo.py - selects new candidate point and writes it to csv file candidate.csv
Run your simulation with new candidate point
Your code needs to add a new row to history.csv before running bo.py again

**Active Learning**
