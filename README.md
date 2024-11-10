# HUNGER GAMES SEARCH

## Install

```bash
git clone https://github.com/KarusalaDeepak/Hunger-Games-Search---Assignment
cd Hunger-Games-Search---Assignment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python3 main.py
```

This should run the algorithm from `main.py` and generate the logs of the run in the `logs` directory. Each entry has timestamp, metrics and filename of the log file of each run.

### Change/Add Algorithm

To add a new algorithm, create a new folder in the `algorithms` directory with the name of the algorithm. The folder should contain the following files: `hyperparameters.json` and `__init__.py`. The `hyperparameters.json` file should contain the hyperparameters for the algorithm. The `__init__.py` file should contain the function (imported from another file is also fine, just the function must be available here).
<br>
Then import that function in `algorithms/__init__.py` file.


### Update Benchmark Functions

To update the benchmark functions, modify the `benchmark_functions.py` file. The functions should be defined in the same format as the existing functions.
