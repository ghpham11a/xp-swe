# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        
        def search(topRight, bottomLeft):

            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))

            if not sea.hasShips(topRight, bottomLeft):
                return 0

            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2
            mid = Point(midX, midY)

            topLeftArea = search(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            topRightArea = search(topRight, Point(mid.x + 1, mid.y + 1))
            bottomRightArea = search(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))
            bottomLeftArea = search(Point(mid.x, mid.y), bottomLeft)

            return topLeftArea + topRightArea + bottomRightArea + bottomLeftArea

        return search(topRight, bottomLeft)
        