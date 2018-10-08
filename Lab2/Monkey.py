import math

def checking(k): 
  hours_count = 0
  for index in range(0, len(piles)):
    hours_count += math.ceil(piles[index]/k)
  if hours_count <= H:
    return True
  else:
    return False

def countEatingSpeed(piles, H):
  piles = sorted(piles)
  left_limit = 1
  right_limit = max(piles)  

  while left_limit < right_limit:  
      mid = (left_limit + right_limit) // 2
      if not checking(mid):
        left_limit = mid + 1
      else:
        right_limit = mid
  return left_limit


if __name__ == '__main__':
    piles = [30,11,23,4,40]
    H = 6

    print(countEatingSpeed(piles, H))
