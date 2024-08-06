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

2. Define initial training data in first_run.py by adjusting values in dictionary ‘initial_data’ - Currently there are 3 data-points, at least 1 is needed
3. Run first_run.py to create the history.csv file 
```
python first_run.py 
```
4. Run bo.py - selects new candidate point and writes it to csv file candidate.csv
5. Run your simulation with new candidate point
6. Your code needs to add a new row to history.csv before running bo.py again

**Active Learning**
