# airfoil-exploration


**Anaconda Environment**

Create anaconda environment from yml file by running
```
conda env create -f exploration.yml -n exploration
```
Activate environment
```
conda activate exploration
```
If that doesn’t work
```
source activate exploration
```
**Bayesian Optimization**
1. Define names of parameters in first_run.py and bo.py by adjusting strings in list ‘parameter_names’ - works with any number of parameters

2. Define parameter bounds in first_run.py and bo.py by adjusting values in 'param_bounds' dictionary

3. Define initial training data in first_run.py by adjusting values in dictionary ‘initial_data’ - Currently there are 3 data-points, at least 1 is needed
4. Run first_run.py - creates the history.csv file 
```
python first_run.py 
```
5. Run bo.py - selects new candidate point and writes it to csv file candidate.csv
```
python bo.py 
```
6. Run your simulation with the new candidate point
7. Your code needs to add a new row to history.csv before running bo.py again

**Active Learning**
1. Define names of parameters in first_run.py and al.py by adjusting strings in list ‘parameter_names’ - works with any number of parameters

2. Define parameter bounds in first_run.py and al.py by adjusting values in 'param_bounds' dictionary

3. Define initial training data in first_run.py by adjusting values in dictionary ‘initial_data’ - Currently there are 3 data-points, at least 1 is needed
4. Run first_run.py - creates the history.csv file 
```
python first_run.py 
```
5. Run al.py - selects new candidate point and writes it to csv file candidate.csv
```
python al.py 
```
6. Run your simulation with the new candidate point
7. Your code needs to add a new row to history.csv before running bo.py again
