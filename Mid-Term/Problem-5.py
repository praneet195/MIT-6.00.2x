def max_contig_sum(L):
   
    
    max_ending_here = max_so_far = L[0]
    for i in L[1:]:
        max_ending_here = max(i, max_ending_here + i)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
