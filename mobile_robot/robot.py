# robot.py
import rospy
from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name):
        self._name = name  # 보호된 변수
        self.__obstacle_detected = False  # 장애물 감지 여부

    @abstractmethod
    def move(self):
        pass

    def stop(self):
        rospy.loginfo(f"{self._name} 정지")

    def get_name(self):
        return self._name

    def set_obstacle_detected(self, status):
        self.__obstacle_detected = status

    def is_obstacle_detected(self):
        return self.__obstacle_detected
