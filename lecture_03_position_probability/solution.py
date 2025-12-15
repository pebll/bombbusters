"""
Solution for Exercise 3: Position Probability
"""

from lecture_02_hypergeometric.solution import hypergeometric_probability


def position_probability_given_cables(M: int, T: int, c: int, j: int, 
                                      smaller_numbers_count: int) -> float:
    """Calculate P(number i at position j | player has c cables)"""
    if j >= c or c <= 0:
        return 0.0
    
    probability = 0.0
    
    # Sum over all possible values of k (number of cables of number i)
    for k in range(1, min(M, c) + 1):
        # Sum over all possible values of s (number of cables of smaller numbers)
        # such that s ≤ j < s+k, i.e., max(0, j-k+1) ≤ s ≤ min(j, c-k)
        s_min = max(0, j - k + 1)
        s_max = min(j, c - k)
        
        for s in range(s_min, s_max + 1):
            # P(player has exactly s cables of smaller numbers)
            prob_s_smaller = hypergeometric_probability(T, smaller_numbers_count, c, s)
            
            # Given s cables of smaller numbers, remaining = c - s
            # Remaining population = T - smaller_numbers_count
            # Of these, M are number i, (T - smaller_numbers_count - M) are larger
            
            remaining_total = T - smaller_numbers_count
            remaining_cables = c - s
            
            if remaining_cables <= 0:
                continue
            
            # P(exactly k cables of number i | s smaller cables)
            prob_k_i = hypergeometric_probability(remaining_total, M, remaining_cables, k)
            
            # Given s smaller and k of number i, number i occupies positions s..s+k-1
            # So position j contains number i with probability 1 (since s ≤ j < s+k)
            probability += prob_s_smaller * prob_k_i
    
    return probability
