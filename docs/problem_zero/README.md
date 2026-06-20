# Problem Zero - Optimised Solution Algorithmic Complexity Analysis

## Code Implementation
* [Optimised Algorithm Implementation](../../problems/problem_zero.py)
* [problem_zero_test.py](../../tests/problem_zero/problem_zero_test.py)
    * [Test file (square_numbers.txt)](../../tests/problem_zero/square_numbers.txt)
* [Benchmarks](./benchmarks/README.md)

## Asymptotic Analysis
The brute-force solution is highly inefficient because it checks each integer sequentially and factors every single number using unoptimized trial division.

* **`get_prime_factors(num)`**: In the worst-case scenario (when `num` is prime), the loop must increment the divisor all the way up to `num`, resulting in a time complexity of **$O(\text{num})$**.
* **`is_square_num(num)`**: Inherits the **$O(\text{num})$** worst-case complexity due to calling the prime factorization step.
* **`generate_k_square_nums(k)`**: The algorithm tests every integer up to a maximum iteration limit $m$. Because it performs an $O(i)$ factorization check on every integer $i$ from $1$ to $m$, the total workload is the sum of arithmetic progressions ($\sum_{i=1}^{m} i$), yielding an implementation complexity of **$O(m^2)$**.

Since the $k$-th perfect square occurs exactly at $m = k^2$, we can substitute this into our runtime equation. This means the overall time complexity of this brute-force approach relative to our input $k$ is an aggressive **$O(k^4)$**.

Although the number of squares found grows sub-linearly at a rate of $O(\sqrt{m})$, the algorithm is forced to perform heavy prime factorization math on every single non-square integer it encounters. Thus, the real-world latency is driven entirely by the massive range of the search space rather than the targets found.

## Conclusion
According to our definitive execution benchmarks, the algorithm scales terribly under this $O(k^4)$ burden:
* At `k = 10` ($m = 100$), it completes in **0.318 seconds**.
* At `k = 100` ($m = 10,000$), it completes in **0.774 seconds**.
* At `k = 1000` ($m = 1,000,000$), the computation hits the complexity wall, taking **2.25 hours (8,098.075 seconds)** to complete. 

This sandbox perfectly illustrates why infrastructure optimizations (like multi-processing) cannot save a program from poor algorithmic complexity.