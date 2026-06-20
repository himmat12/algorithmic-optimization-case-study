# Project Euler - Problem Zero Algorithmic Optimisation & Performance Case Study

A case study in identifying software scaling bottlenecks, profiling CPU-bound execution environments, and engineering an alternative algorithmic architecture to achieve a **99.99% latency reduction**.

## The Experiment At A Glance
This repository uses a mathematical sandbox (generating perfect square numbers) to visually map out and contrast an unoptimized brute-force search space against a linear generation pipeline. 

By restructuring the underlying math logic, the execution time for calculating large sets of targets dropped from **2.25 hours** down to **0.36 seconds**, enabling a scale factor shift capable of generating **1,000,000 targets in under 6 seconds**.

---

## Key Insights & Discoveries

### 1. The Algorithmic Complexity Wall
Our initial brute-force approach relied on an $O(\text{num})$ trial-division prime factorization method executed sequentially inside an $O(m)$ search loop. This compounded into an aggressive **$O(k^4)$ runtime burden** relative to the target size $k$. 

As a result, tracking data points revealed a classic, flattening **Square Root Curve ($y = \sqrt{x}$)**. The massive horizontal plateaus represent millions of CPU cycles wasted profiling non-square numbers.

### 2. The Concurrency Epiphany: Why Infrastructure Alone Couldn't Save the Brute-Force Code
During Phase 1 of development, the initial goal was to simply push the heavy brute-force math loops into the background using a `ProcessPoolExecutor` to bypass Python's Global Interpreter Lock (GIL). 

However, an analysis of the $O(k^4)$ algorithmic complexity wall revealed an architectural truth, because a brute-force approach requires checking 1,000,000 numbers to find just 1,000 targets, throwing multiple CPU cores at billions of unoptimized operations would only provide a minor linear speedup. The code would still take hours to complete. This realized bottleneck forced a structural pivot, proving that hardware and concurrency infrastructure cannot rescue an inefficient complexity class—optimisation had to begin with logic.

### 3. Resolving the Bottleneck with Lazy Generation
The bottleneck was broken by flipping the structural paradigm: shifting from an iterative *search-and-verify* model to a direct *algebraic generation* model using Python generators (`yield`). This compressed the search space into an explicit **$O(k)$ linear time complexity class**, transforming our data visualization into a perfect $45^\circ$ tracking line ($y=x$).

---

## Concurrency & Architecture Highlights
* **Process Isolation:** Leveraged a non-blocking `asyncio` event loop paired with `ProcessPoolExecutor` to offload heavy CPU calculations to dedicated, background OS worker pools, successfully bypassing Python's Global Interpreter Lock (GIL).
* **Lazy Evaluation:** Engineered memory-safe data streaming via infinite generators to maintain a totally flat RAM footprint.
* **Deterministic Logging:** Automated comprehensive execution metric captures, dumping atomic timestamps and iteration tracking directly into overwrite-safe JSON manifests.

## Deep Dives
* [Problem Zero - Brute-Force Algorithmic Complexity Case Study](docs/problem_zero/brute_force/README.md)
* [Problem Zero - Optimised Algorithmic Complexity Case Study](docs/problem_zero/optimised/README.md)