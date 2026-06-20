# Problem Zero - Optimised Solution Algorithmic Complexity Analysis

> ### you can check the brute-force algorithm analysis and implementation in `problem_zero_brute_force_case_study` branch

## Code Implementation
* [Optimised Algorithm Implementation](../../problems/problem_zero.py)
* [problem_zero_test.py](../../tests/problem_zero/problem_zero_test.py)
    * [Test file (square_numbers.txt)](../../tests/problem_zero/square_numbers.txt)
* [Benchmarks](./benchmarks/README.md)

## Asymptotic Analysis
The optimised solution is highly efficient because it eliminates the trial-division prime factorization bottlenecks entirely. Instead, it computes perfect square numbers sequentially and natively on demand.

* **`generate_square_nums()`**: Generates the perfect square of each integer sequentially using a lazy generator pattern. Each yielded computation performs a single, direct algebraic multiplication, executing in constant time **$O(1)$**.
* **`generate_k_square_nums(k)`**: Acts as a controller loop that pulls exactly $k$ items from the generator. Because it performs an $O(1)$ step exactly $k$ times, the structural time complexity scales strictly linearly as **$O(k)$**.

By switching from an iterative search space model to a direct mathematical generation model, the total operations required to find $k$ squares dropped from a staggering $O(k^4)$ down to a lean **$O(k)$**.

## Conclusion
According to our definitive execution benchmarks, the optimized algorithm scales excellently:
* At `k = 10` (Max Square: $100$), it completes in **0.321 seconds**.
* At `k = 100` (Max Square: $10,000$), it completes in **0.488 seconds**.
* At `k = 1000` (Max Square: $1,000,000$), it completes in **0.363 seconds**. (This is where our original brute-force baseline hit a wall and took over **2.25 hours**).
* At `k = 10000` (Max Square: $100,000,000$), it completes in **0.447 seconds**.
* At `k = 100000` (Max Square: $10,000,000,000$), it completes in **0.847 seconds**.
* At `k = 1000000` (Max Square: $1,000,000,000,000$), it completes in **5.957 seconds**.

This optimization sandbox beautifully demonstrates how addressing core algorithmic complexity solves scale bottlenecks where infrastructure adjustments alone fall short.