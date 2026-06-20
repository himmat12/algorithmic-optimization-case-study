import time
import json
import pandas as pd
import matplotlib.pyplot as plt


k = 10
FILE_LOCATIONS = {
    10 : "when_k_equals_10",
    100 : "when_k_equals_100",
    1000 : "when_k_equals_1000"
}

def deserialize_file(file_path: str):
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(e)

def plot_benchmarks(file_path, k):
    iteration_computation_benchmarks_data = deserialize_file(file_path)
    records = [d for d in iteration_computation_benchmarks_data]

    df = pd.DataFrame(records)
    plt.figure(figsize=(10,5))
    plt.plot(df["iteration"], df["square_nums_count"])
    plt.xlabel("Iterations")
    plt.ylabel("Square Numbers")
    plt.title(f"Square Numbers per Iteration when k = {k}")
    plt.show()

def main():
    for k, file in FILE_LOCATIONS.items():
        location = FILE_LOCATIONS[k]
        iteration_compute_benchmark_file_path = f"./docs/problem_zero/data_visualisation/{location}/problem_zero_each_iteration_computation.json"
        plot_benchmarks(iteration_compute_benchmark_file_path, k)

if __name__ == "__main__":
    main()