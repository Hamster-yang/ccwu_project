# https://blog.hashteacher.com/?p=1048

from easytello import tello

myTello = tello.Tello()
myTello.takeoff() #起飛
myTello.forward(10) #前進
myTello.cw(90) #旋轉
myTello.land() #降落

