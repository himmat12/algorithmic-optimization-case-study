### Benchmarked Difference across Input Sizes (`k`)

The [log](#logs) below captures how the execution time of this brute-force algorithm explodes exponentially as the target size `k` grows from 10 to 1000. 

While finding the first 10 square numbers takes an already high `0.318s`, scaling to `k = 1000` hits a massive algorithmic wall. Because the search space expands quadratically ($k^2$), finding 1000 square numbers requires evaluating 1,000,000 integers. Combined with increasingly heavy prime factorization loops, the duration spikes from under a second to over **2.25 hours** (`8098.075s`).

You can see the detailed computation benchmarks (tracked by iteration, individual square number discovery, and total task duration) here:
* [When k is 10](./when_k_equals_10/)
* [When k is 100](./when_k_equals_100/)
* [When k is 1000](./when_k_equals_1000/)

Data visualizations of the square number computation trajectory per iteration:
* [When k is 10](../data_visualisation/charts/when_k_is_10.png)
* [When k is 100](../data_visualisation/charts/when_k_is_100.png)
* [When k is 1000](../data_visualisation/charts/when_k_is_1000.png)


### Logs

```txt
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 10


Start: 26096.2867909
Heavy computation in progress in seperate process...
Computation completed successfully. Writing benchmarks to file...
End: 26096.6052864
Duration: 0.31849549999969895

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 100


Start: 26126.7806489
Heavy computation in progress in seperate process...
Computation completed successfully. Writing benchmarks to file...
End: 26127.5556188
Duration: 0.7749699000014516

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 1000


Start: 26156.633784
Heavy computation in progress in seperate process...
Computation completed successfully. Writing benchmarks to file...
End: 34254.7090933
Duration: 8098.0753092999985

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> 
```