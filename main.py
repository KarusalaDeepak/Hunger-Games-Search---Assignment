from optimization_engine import OptimizationEngine
from benchmark_functions import benchmark_functions
from hgs import hunger_games_search

if __name__ == "__main__":
    algorithms = {
        "HGS": hunger_games_search
    }

    engine = OptimizationEngine(benchmark_functions, algorithms, plot_interval=1)
    engine.run_optimization()
