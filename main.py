from optimization_engine import OptimizationEngine
from benchmark_functions import benchmark_functions
from hgs import hunger_games_search
from statistical_tests import perform_friedman_test, perform_wilcoxon_tests  # Import test functions
import pandas as pd
import os
from datetime import datetime

if __name__ == "__main__":
    algorithms = {
        "HGS": hunger_games_search
    }

    engine = OptimizationEngine(benchmark_functions, algorithms, plot_interval=1)
    engine.run_optimization()

    # Code Performing the statistical tests. As we have only one algorithm, couldn't perform the test.
    # # Load the results CSV and perform statistical tests
    # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # results_path = os.path.join("csv_results", f"results_{timestamp}.csv")

    # if os.path.exists(results_path):
    #     results_df = pd.read_csv(results_path)
    #     perform_friedman_test(results_df)
    #     perform_wilcoxon_tests(results_df)
    # else:
    #     print(f"Results file not found: {results_path}")