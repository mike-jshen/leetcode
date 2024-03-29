def findMin(nums: List[int]) -> int:
  if len(nums) == 1:
    return nums[0]

  l = 0
  r = len(nums) - 1
  mid = math.floor((l+r)/2)
  while l < r:
    if nums[mid] > nums[r]:
      print("increase mid")
      l = mid + 1
      mid = math.floor((r+l)/2)

    elif nums[mid] < nums[l]:
      print("decrease mid")
      r = mid
      mid = math.floor((r+l)/2)
            
    else:
      return nums[l]
    
    return nums[mid]
