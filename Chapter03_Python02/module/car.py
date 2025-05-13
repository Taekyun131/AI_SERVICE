# File name: car.py

class Car():
    def __init__(self, size, color):
        self.size=size
        self.color=color
        
    def move(self):
        print("자동차({0}&{1})가 움직입니다.".format(self.size, self.color))
