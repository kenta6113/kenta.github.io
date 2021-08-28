class Shape:
  def what_am_i(self):
    print('I am a shape')


class Rectage(Shape):
  def __init__(self,l) -> None:
      self.length = l

  def calculate_perimeter(self):
    return self.length*4

class Square(Shape):
  def __init__(self,l) -> None:
      self.length = l

  def calculate_perimeter(self):
    return self.length*4

  def change_size(self,n):
    self.length +=n


retage = Rectage(5)
print(retage.what_am_i())
square = Square(5)
print(square.what_am_i())
rectage = Rectage(3)
print(rectage.calculate_perimeter())
square = Square(6)
print(square.calculate_perimeter())
square.change_size(-2)
print(square.calculate_perimeter())