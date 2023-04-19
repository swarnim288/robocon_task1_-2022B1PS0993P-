class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]

############

class Solution(object):
  def constructRectangle(self, area):
    """
    :type area: int
    :rtype: List[int]
    """
    root = int(area ** 0.5)
    while root > 0:
      if area % root == 0:
        return int(area / root), root
      root -= 1