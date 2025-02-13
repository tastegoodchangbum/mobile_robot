# mobile_robot.py
import rospy
from robot import Robot

class MobileRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self._speed = 1  # 속도 변수

    def move(self):
        rospy.loginfo(f"{self.get_name()} 이동 중...")

    def set_speed(self, speed):
        if speed > 0:
            self._speed = speed
        else:
            rospy.logwarn("⚠ 속도는 0보다 커야 합니다.")

    def get_speed(self):
        return self._speed
