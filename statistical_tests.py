import os
import pandas as pd
from scipy.stats import friedmanchisquare, wilcoxon

# Perform Friedman Test
def perform_friedman_test(results_df):
    # Assuming results are structured with each algorithm as a column and rows as function/problem results
    stat, p_value = friedmanchisquare(*[results_df[algo] for algo in results_df.columns[2:]])
    print("Friedman Test Results:")
    print(f"Statistic: {stat}, p-value: {p_value}")
    if p_value < 0.05:
        print("Significant differences detected among algorithms.")
    else:
        print("No significant differences among algorithms.")

# Perform Wilcoxon Signed-Rank Test (pairwise comparisons)
def perform_wilcoxon_tests(results_df):
    algo_columns = results_df.columns[2:]  # Assuming algorithms start from third column
    for i in range(len(algo_columns)):
        for j in range(i + 1, len(algo_columns)):
            alg1 = results_df[algo_columns[i]]
            alg2 = results_df[algo_columns[j]]
            stat, p_value = wilcoxon(alg1, alg2)
            print(f"Wilcoxon Test: {algo_columns[i]} vs {algo_columns[j]}")
            print(f"Statistic: {stat}, p-value: {p_value}")
            if p_value < 0.05:
                print(f"Significant difference between {algo_columns[i]} and {algo_columns[j]}.")
            else:
                print(f"No significant difference between {algo_columns[i]} and {algo_columns[j]}.")
