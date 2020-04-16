memo = {}

def fibonacci(n):
  global memo
  if n == 0:
    return memo[0]
  elif n == 1:
    return memo[1]
  elif n in memo.keys():
    return memo[n]
  else:
    memo[n] = fibonacci(n-2) + fibonacci(n-1)**2
    return memo[n]

def main():
  global memo
  t0, t1, n = map(int, input().split())
  memo[0] = t0
  memo[1] = t1
  print(fibonacci(n-1))

if __name__ == "__main__":
  main()  