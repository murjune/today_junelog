# 2개의 직사각형이 겹치는지 검사하는 프로그램
class Rectangle:
    x = 0
    y = 0
    w = 0
    h = 0
    def __init__(self,x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        tup = (self.x, self.y, self.w , self.h)
        return tup

    def overlap(self, r):
            r_x, r_y, r_w, r_h = r.__str__()

            r_left, r_right  = self.x, (self.x + self.w)
            r_top, r_bottom = self.y, (self.y - self.h)

            r2_left, r2_right = r_x, r_x + r_w
            r2_top, r2_bottom = r_y, r_y - r_h

            if (r_left > r2_right or r_right < r2_left or r_top < r2_bottom or r_bottom> r2_top):
                return False

            return True

r = Rectangle(200,200, 100, 100)
r2 = Rectangle(10, 10, 100, 100)
print(r.overlap(r2))