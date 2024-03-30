def longestConsecutive(nums: List[int]) -> int:
  s = set(nums)
  result = 0

  for num in s:
      if num - 1 not in s:
          count = 1
          temp = num + 1
          while temp in s:
              count += 1
              temp += 1
          result = max(result,count)

  return result
