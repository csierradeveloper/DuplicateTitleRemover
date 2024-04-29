Script to take an input file containing some number of repeated lines, and create a sorted output file containing
each line once, with the number of times each line added, removing all entries that appear less than a given
minimum of times.

Sample Input:

> A  
> A  
> A  
> A  
> B  
> B  
> C  
> C  
> C  
> C  
> C  
> C  
> D

Sample Output, minimum # required is 4:

> 005 - C  
> 004 - A

Input is read from an "Input.txt" file in the top-level directory.
Output is written to an "Output.txt" file in the top-level directory.