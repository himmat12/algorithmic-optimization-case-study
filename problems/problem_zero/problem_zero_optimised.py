import asyncio
from concurrent.futures import ProcessPoolExecutor
import json
from time import perf_counter
from collections import defaultdict
from datetime import datetime

# OPTIMISED square number generator
def generate_square_nums():
    '''
    Optimised infinite square number generator.
    
    Returns:
        tuple[int, float]: A tuple containing the generated square number and the performance benchmark start count.
    '''
    num = 1
    while True:
        start = perf_counter()
        yield (num * num, start)
        num += 1

def generate_k_square_nums(k: int) -> tuple[list[int], defaultdict, defaultdict]:
    each_iteration_computation_benchmarks = defaultdict()
    each_square_num_computation_benchmarks = defaultdict()

    each_iteration_computation_benchmarks["start_time"] = {"start_time": f"{datetime.now()}"}
    each_square_num_computation_benchmarks["start_time"] = {"start_time": f"{datetime.now()}"}
    
    square_nums = []
    for i, res in enumerate(generate_square_nums()):
        """
        `end` value is captured right after iteration starts because start is already computed by `generate_square_nums` generator and yielded 
        therefore in order to benchmrak accurate latency end is right after the iteratation
        """
        end = perf_counter() 
        start = res[1]
        square_num = res[0]
        if len(square_nums) >= k:
            each_iteration_computation_benchmarks["end_time"] = {"end_time": f"{datetime.now()}"}
            each_square_num_computation_benchmarks["end_time"] = {"end_time": f"{datetime.now()}"}
            break
        square_nums.append(square_num)
        each_square_num_computation_benchmarks[square_num] = {
                    "square_num": square_num,
                    "iteration": i,
                    "square_nums_count": len(square_nums),
                    "duration": end - start,
                    "timestamp": f"{datetime.now()}",
                }
        each_iteration_computation_benchmarks[i] = {
                        "iteration": i,
                        "square_nums_count": len(square_nums),
                        "duration": end - start,
                        "timestamp": f"{datetime.now()}",
                    }
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


k = 1000000
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
        print("Heavy but optimised computation in progress...")
        
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
