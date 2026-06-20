import asyncio
from concurrent.futures import ProcessPoolExecutor
import json
from math import sqrt
from time import perf_counter
from collections import defaultdict
from datetime import datetime

# this recursive algorithm is not viable while computing massive numbers like 100k
def get_prime_factors_recur(num: int, divisor: int = 2) -> int:
    if num <= 1:
        return []

    if num % divisor == 0:
        return [divisor] + get_prime_factors_recur(num // divisor, divisor)
    else:
        return get_prime_factors_recur(num, divisor + 1)


def get_prime_factors(num: int, divisor: int = 2) -> int:
    if num <= 1:
        return []

    prime_factors = []
    current_factor = num
    while True:
        if current_factor == 1:
            break
        if current_factor % divisor != 0:
            divisor += 1
            continue
        current_factor = current_factor // divisor
        prime_factors.append(divisor)
    return prime_factors


# this recursive algorithm is not viable while computing massive numbers like 100k
def is_square_num_recur(num: int) -> bool:
    prime_factors = get_prime_factors(num)
    prime_factors_freq = defaultdict(int)

    for factor in prime_factors:
        prime_factors_freq[factor] += 1

    for value in prime_factors_freq.values():
        if value % 2 != 0:
            return False
    return True


def is_square_num(num: int) -> bool:
    prime_factors = get_prime_factors(num)
    factor_freq = defaultdict(int)

    for factor in prime_factors:
        factor_freq[factor] += 1

    for freq in factor_freq.values():
        if freq % 2 != 0:
            return False
        continue
    return True


def generate_k_square_nums(k: int) -> tuple[list[int], defaultdict, defaultdict]:
    each_iteration_computation_benchmarks = defaultdict()
    each_square_num_computation_benchmarks = defaultdict()

    each_iteration_computation_benchmarks["start_time"] = {"start_time": f"{datetime.now()}"}
    each_square_num_computation_benchmarks["start_time"] = {"start_time": f"{datetime.now()}"}
    
    n = 1
    square_nums = []

    while True:
        start = perf_counter()
        if len(square_nums) >= k:
            each_iteration_computation_benchmarks["end_time"] = {"end_time": f"{datetime.now()}"}
            each_square_num_computation_benchmarks["end_time"] = {"end_time": f"{datetime.now()}"}
            break
        if is_square_num(n):
            square_nums.append(n)
            end = perf_counter()
            each_square_num_computation_benchmarks[n] = {
                        "square_num": n,
                        "iteration": n,
                        "square_nums_count": len(square_nums),
                        "duration": end - start,
                        "timestamp": f"{datetime.now()}",
                    }
            each_iteration_computation_benchmarks[n] = {
                            "iteration": n,
                            "square_nums_count": len(square_nums),
                            "duration": end - start,
                            "timestamp": f"{datetime.now()}",
                        }
            n += 1
            continue
        end = perf_counter()
        each_iteration_computation_benchmarks[n] = {
                        "iteration": n,
                        "square_nums_count": len(square_nums),
                        "duration": end - start,
                        "timestamp": f"{datetime.now()}",
                    }
        n += 1
    return (square_nums, each_iteration_computation_benchmarks, each_square_num_computation_benchmarks)

def save_iteration_computation_benchmarks_to_file(location, each_iteration_computation_benchmarks):
     start = perf_counter()
     with open(f"./docs/problem_zero/benchmarks/{location}/problem_zero_each_iteration_computation.json.txt", 'w') as f:
         f.write(f"Start of IO: {start}\n\n")
         f.write('[')
         for key, val in each_iteration_computation_benchmarks.items():
            f.write(f"{json.dumps(val)},\n")
         f.write(']')
         end = perf_counter()
         f.write(f"\n\nEnd of IO: {end}")
         f.write(f"\nDuration of IO: {end - start}")
         
def save_square_num_computation_benchmarks_to_file(location, each_square_num_computation_benchmarks):
     start = perf_counter()
     with open(f"./docs/problem_zero/benchmarks/{location}/problem_zero_each_square_num_computation.json.txt", 'w') as f:
         f.write(f"Start of IO: {start}\n\n")
         f.write('[')
         for key, val in each_square_num_computation_benchmarks.items():
            f.write(f"{json.dumps(val)},\n")
         f.write(']')
         end = perf_counter()
         f.write(f"\n\nEnd of IO: {end}")
         f.write(f"\nDuration of IO: {end - start}")
         
def save_computed_square_nums_to_file(location, nums: list[int]):
     start = perf_counter()
     with open(f"./docs/problem_zero/benchmarks/{location}/problem_zero_computed_square_nums.json.txt", 'w') as f:
         f.write(f"Start of IO: {start}\n\n")
         for num in nums:
             f.write(f"{str(num)}, ")
         end = perf_counter()
         f.write(f"\n\nEnd of IO: {end}")
         f.write(f"\nDuration of IO: {end - start}")
  
def save_problem_zero_computation_benchmarks_to_file(location, benchmarks):
     with open(f"./docs/problem_zero/benchmarks/{location}/problem_zero_computation_benchmarks.json.txt", 'w') as f:
         f.write('[\n')
         for key, benchmark in benchmarks.items():
             f.write(f"{json.dumps({key : benchmark})},\n")
         f.write(']')


k = 1000
FILE_LOCATIONS = {
    10 : "when_k_equals_10",
    100 : "when_k_equals_100",
    1000 : "when_k_equals_1000",
    10000 : "when_k_equals_10000",
    100000 : "when_k_equals_100000",
    1000000 : "when_k_equals_1000000"
}
square_nums = []
location = FILE_LOCATIONS[k]

problem_zero_computation_benchmark = defaultdict()

async def main():
    try:
        print (f"When k = {k}\n\n")
        loop = asyncio.get_running_loop()
        
        start = perf_counter()
        problem_zero_computation_benchmark["start_time"] = start
        print(f"Start: {start}")
        print("Heavy computation in progress in seperate process...")
        
        with ProcessPoolExecutor() as pool:
            computation_result= await loop.run_in_executor(pool, generate_k_square_nums, k)
            square_nums = computation_result[0]
            each_iteration_computation_benchmarks = computation_result[1]
            each_square_num_computation_benchmarks = computation_result[2]
            
        end = perf_counter()
        duration = end - start
        problem_zero_computation_benchmark["end_time"] = end
        problem_zero_computation_benchmark["total_duration"] = duration
        
        if square_nums:
            print("Computation completed successfully. Writing benchmarks to file...")
            print(f"End: {end}")
            print(f"Duration: {duration}\n")
            save_iteration_computation_benchmarks_to_file(location, each_iteration_computation_benchmarks)
            save_square_num_computation_benchmarks_to_file(location, each_square_num_computation_benchmarks)
            save_computed_square_nums_to_file(location, square_nums)
            save_problem_zero_computation_benchmarks_to_file(location, problem_zero_computation_benchmark)
            print("All files saved successfully.")
            
        else:
            print("No numbers were generated.")
            
        
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
