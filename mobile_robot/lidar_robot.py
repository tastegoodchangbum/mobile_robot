import rospy
from sensor_msgs.msg import LaserScan
from mobile_robot import MobileRobot
from motor_controller import MotorController

class LidarRobot(MobileRobot):
    def __init__(self, name):
        super().__init__(name)
        self.__motor = MotorController()
        self.__lidar_sub = rospy.Subscriber("/scan", LaserScan, self.__lidar_callback)

        # 3D 좌표 초기화
        self.position = [0.0, 0.0, 0.0]  # [x, y, z]
        self.rate = rospy.Rate(1)  # 1Hz

    def __lidar_callback(self, data):
        min_distance = min(data.ranges)
        if min_distance < 0.6:
            self.set_obstacle_detected(True)
        else:
            self.set_obstacle_detected(False)

    def move(self):
        while not rospy.is_shutdown():
            if self.is_obstacle_detected():
                rospy.loginfo("⚠ 장애물 감지! 좌회전 수행")
                self.__motor.turn_left()
            else:
                rospy.loginfo("🚗 직진 중...")
                self.__motor.move_forward()
                self.update_position()  # 위치 업데이트

            # 현재 위치 로그 출력
            rospy.loginfo(f"현재 위치: {self.position}")

            self.rate.sleep()  # 1초마다 반복

    def update_position(self):
        # 직진할 때 x좌표를 증가시키고, y좌표는 변하지 않는다고 가정
        self.position[0] += 1.0  # x축 방향으로 1.0 단위 이동
        # y축이나 z축 이동 로직이 필요하면 추가할 수 있음
