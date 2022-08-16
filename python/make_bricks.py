def make_bricks(small, big, goal):
  if goal > (big * 5 + small):
    return False
  elif small < (goal % 5):
    return False
#  elif goal // 5 < big:
#     return False
  else:
    return True

