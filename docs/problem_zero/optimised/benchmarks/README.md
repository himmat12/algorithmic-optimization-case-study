### Benchmarked Performance Gains across Input Sizes (`k`)

The [logs](#logs) below capture how the optimized generation algorithm fundamentally eliminates the performance walls found in the original brute-force sandbox. 

By replacing sequential integer factorization checks with an $O(k)$ direct-generation generator stream, computing $k = 1000$ squares no longer takes **2.25 hours** (`8098.075s`), it completes instantly in **0.363 seconds**. Even when scaling the input workload exponentially to find **1,000,000 perfect squares**, the total execution time stays well under six seconds.

Detailed computation logs (tracking performance maps by loop iteration, discrete square number discovery intervals, and total execution cycles) are cataloged below:
* [When k is 10](./when_k_equals_10/)
* [When k is 100](./when_k_equals_100/)
* [When k is 1000](./when_k_equals_1000/)
* [When k is 10000](./when_k_equals_10000/)
* [When k is 100000](./when_k_equals_100000/)
* [When k is 1000000](./when_k_equals_1000000/)

Data visualizations of the linear computation trajectory per iteration:
* [When k is 10](../data_visualisation/charts/when_k_is_10.png)
* [When k is 100](../data_visualisation/charts/when_k_is_100.png)
* [When k is 1000](../data_visualisation/charts/when_k_is_1000.png)
* [When k is 10000](../data_visualisation/charts/when_k_is_10000.png)
* [When k is 100000](../data_visualisation/charts/when_k_is_100000.png)
* [When k is 1000000](../data_visualisation/charts/when_k_is_1000000.png)


### Logs

```txt
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 10


Start: 111097.0553196
Heavy but optimised computation in progress...
Computation completed successfully. Writing benchmarks to file...
End: 111097.3771835
Duration: 0.32186389999696985

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 100


Start: 111106.616347
Heavy but optimised computation in progress...
Computation completed successfully. Writing benchmarks to file...
End: 111107.1051824
Duration: 0.4888353999995161

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 1000


Start: 111174.1187486
Heavy but optimised computation in progress...
Computation completed successfully. Writing benchmarks to file...
End: 111174.482117
Duration: 0.3633684000087669

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 10000


Start: 111285.8601127
Heavy but optimised computation in progress...
Computation completed successfully. Writing benchmarks to file...
End: 111286.3067786
Duration: 0.44666590000269935

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 100000


Start: 111301.3935478
Heavy but optimised computation in progress...
Computation completed successfully. Writing benchmarks to file...
End: 111302.2409255
Duration: 0.8473776999890106

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler> python .\problems\problem_zero.py
When k = 1000000


Start: 111315.9840961
Heavy but optimised computation in progress...
Computation completed successfully. Writing benchmarks to file...
End: 111321.9413636
Duration: 5.957267499994487

All files saved successfully.
(.venv) PS C:\Users\HBRAI\Desktop\coding\project_euler>
```