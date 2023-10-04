
NOTE: This is a python file that runs different sorting algorithms and records the time that each algorithm takes to sort a given list. The results are saved to a graph by using the pyplot library

<h1>Findings:</h1>

<h3>Comparison of time consumption of slow & fast sorting algorithms on randomized data</h3>

It’s apparent by the resulting charts that selection sort runs O(n^2) times on average and insertion sort is also O(n^2)

<h4>Slow algorithms</h4>

The expected complexity of running times for each slow algorithm on randomized data was: Selection and Insertion sort were both O(n^2). The resulting graphs verify these expectations because they both grow quadratically and appear similar.

<img width="488" alt="image" src="https://github.com/thomasriley0/Sorting-Algorithm-Analysis/assets/129229020/4e90d8e9-4a1d-490b-80cf-37baaf4ccbb7">

<h4>Fast algorithms</h4>

The expected complexity of running times for each fast algorithm on randomized data was: Heap sort: O(n log n), Built-in: O,(nlogn) *however much faster than others because of it’s hybrid design (timsort) Merge: O(n log n) and quicksort O(n log n. The resulting graphs verify these claims considering that each graph is similar in shape and all follow a logarithmic pattern besides python’s-built-in sort which follows a linear pattern.

<img width="483" alt="image" src="https://github.com/thomasriley0/Sorting-Algorithm-Analysis/assets/129229020/360fe10f-c0ab-494e-9663-be344c1f4f3a">


<h3>Comparison of time consumption of slow & fast sorting algorithms on reverse sorted data</h3>

<h4>Slow algorithms</h4>

The expected complexity of running times for each slow algorithm on reverse sorted data was: Selection and Insertion sort were both O(n^2). The resulting graphs verify these expectations because they both grow quadratically and appear similar.

<img width="566" alt="image" src="https://github.com/thomasriley0/Sorting-Algorithm-Analysis/assets/129229020/3fd9d198-1ffb-45c3-bc01-e8fcc1ea68cc">


<h4>Fast algorithms</h4>

The expected complexity of running times for each fast algorithm on reverse sorted data was: Heap sort: O(n log n), Built-in: O(n log n) *however much faster than others because of it’s hybrid design (timsort), Merge: O(n log n) and quicksort O(n log n. The resulting graphs verify these claims considering that each graph is similar in shape and all follow a logarithmic pattern besides python’s-built-in sort which follows a linear pattern.

<img width="560" alt="image" src="https://github.com/thomasriley0/Sorting-Algorithm-Analysis/assets/129229020/a3a7fba4-6ed4-4cf0-8ef6-7c419cfdd94d">

<h3>Comparison of time consumption of slow & fast sorting algorithms on already sorted data</h3>

<h4>Slow algorithms</h4>

The expected complexity of running times for each slow algorithm on already sorted data was: Selection O(n^2) and Insertion sort o(n). The resulting graphs verify these expectations because they selection sort grows quadratically and insertion short is linear and it’s time consumption is near zero.

<img width="507" alt="image" src="https://github.com/thomasriley0/Sorting-Algorithm-Analysis/assets/129229020/c6b594b1-b693-4f5a-94c8-94ce89ab336f">

<h4>Fast algorithms</h4>

The expected complexity of running times for each fast algorithm on already sorted data was: Heap sort: O(n log n), Built-in: O,(nlogn) *however much faster than others because of it’s hybrid design (timsort),  Merge: O(n log n) and quicksort O(n log n. The resulting graphs verify these claims considering that Heap, Merge & Quicksort follow a logarithmic pattern (heap sort varying slightly due to its consistency issues) besides python’s-built-in sort which follows a linear pattern and has a time consumption near zero.





