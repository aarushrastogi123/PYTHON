import math as m
class Sphere:
    def __init__(self,a):
        self.r=a
    def volume(self):
        answer=(4/3)* m.pi * (self.r ** 3)
        return answer

sphere=Sphere(6)

print(f'Volume={sphere.volume()}')