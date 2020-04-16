def main():
  n, s = map(int, input().split())
  nums = list(map(int, input().split()))

  count = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if (nums[i]+nums[j]) % s==0:
        # print(nums[i], nums[j])
        count+=1
  
  print(count)

if __name__ == "__main__":
    main()