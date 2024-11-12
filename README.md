This repository contains implementations of various data structures and algorithms in Python.The goal is to provide easy-to-understand code for each concept with explanations,making it a helpful resource for anyone learning or practicsig DSA in Python.
TABLE OF CONTENTS:
1.Data Structures
• Arrays
• Linked Lists
• Stacks
• Queues
• Trees
• Graphs
• Hash Tables
• Heaps

♦ Linear Search:
In linear search, we will find the position of two elements that sum to a taget present in array linearly..
➞ Iterate through each element in the list using an outer loop.
➞ For each element in the outer loop,use an inner loop to check every other element that comes after it.
➞ If a pair of numbers adds up to target,return their indices or values.
𝔗𝔦𝔪𝔢 ℭ𝔬𝔪𝔭𝔩𝔢𝔵𝔦𝔱𝔶:This approach has a time complexity of O(n^2),as each element is compared with every other element.

♦ Binary Search:
Binary search is a highly efficient algorithm used to find the position of a target value with in a sorted list.It operates by repeatedly dividing the seearch interval in half,making it much faster than linear search in large databases.
➞ Start with two pointers-left at the beginning and right at the end of the list.
➞ Calculate the middle index and check if the element matches the target.
➞ If the lement matches the target, you've found the target.
➞ If the target is less than the mid element ,narrow the search to the left half by setting right to mid-1.
➞ If the target is greater than the middle element,narrow to the right half by setting left to mid+1.
➞ Repeat until the target is found or low exceeds high.
𝔗𝔦𝔪𝔢 ℭ𝔬𝔪𝔭𝔩𝔢𝔵𝔦𝔱𝔶:O(logn)
Each comparison cuts the list size in half,making binary search logarithmic and highly efficient,especially for large lists
NOTE:We can apply a Binary search only when the array is sorted.

♦ Two pointer approach:
Two pointer approach is an efficient algorithmic technique often used for problmrs involving sorted arrays,where you need to find the pairs in linear time O(n)
