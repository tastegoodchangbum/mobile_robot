# main.py
import rospy
from lidar_robot import LidarRobot

if __name__ == "__main__":
    try:
        rospy.init_node("lidar_robot", anonymous=True)
        lidar_bot = LidarRobot("LidarBot")
        lidar_bot.move()
    except rospy.ROSInterruptException:
        pass
    finally:
        import RPi.GPIO as GPIO
        GPIO.cleanup()  # 프로그램 종료 시 GPIO 정리
