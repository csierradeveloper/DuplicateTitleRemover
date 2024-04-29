Script to take an input file containing some number of repeated lines, and create 
a sorted output file containing each line once, with the number of times each line 
appeared added, removing all lines that appeared less than a given minimum of times.
Ignores lines matching a provided pattern.

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

Ignored lines are of the form:
> Lastname, Firstname *