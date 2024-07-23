import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  p = 1
  sum = v
  while v//(k**p) != 0:
    sum = sum + v//(k**p)
    p+=1
  return sum



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):

  for v in range(n):
    if sum_series(v, k) >= n:
      return v
  return n
      

  

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    high = n
    low = 0
    while high > low:
        v = (high + low) // 2 
        ser = sum_series(v, k)
        if ser == n:
            break
        elif ser < n:
            low = v + 1 
        elif ser > n:
            high = v - 1
    # Check if low or high is closer to the desired number:
    if 0 <= sum_series(low, k) - n < ser - n:
      v = low 
    else: v
    
    if 0 <= sum_series(high, k) - n < ser - n or ser < n:
      v = high    
    else: v
    
    return v


def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
