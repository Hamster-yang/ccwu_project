import tellopy #導入套件tellopy
from time import sleep
#help(tellopy) #觀看套件的詳細說明
drone = tellopy.Tello() #建立物件tellopy.Tello()
drone.connect() #使程式與tello建立連接
#drone.wait_fot_connection(3) #等待連接的時間, 秒數
#drone.get_video_stream()
drone.takeoff() #使tello起飛
sleep(3)
drone.forward(30)
sleep(10)
drone.clockwise(-90)
sleep(1)
drone.clockwise(0)
sleep(1)
drone.forward(30)
sleep(5)
drone.clockwise(-100)
sleep(1)
drone.clockwise(0)
sleep(1)
drone.forward(30)
sleep(11)
drone.clockwise(-100)
sleep(1)
drone.clockwise(0)
sleep(1)
drone.forward(30)
sleep(5)
drone.clockwise(-90)
sleep(1)
drone.clockwise(0)
sleep(1)
drone.backward(10)
sleep(3)
drone.land() #使tello降落
sleep(3)
drone.quit() #結束程式與tello的連接