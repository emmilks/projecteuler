'''
Project_Euler # 4
Find the difference between the sum of the squares of the first 100 natural fibNumbers
and the square of the sum.
'''
# Original brute force solution
'''
naturals = [i for i in range(limit+1)]
naturals_squared = [i**2 for i in range(limit+1)]
squared_sum = sum(naturals_squared)
sum_squared = sum(naturals)**2
'''
from project_euler import difference_squared_sums

# Prints the answer
print(difference_squared_sums(100))
