#!/usr/bin/python3

import rclpy
from rclpy.node import Node

from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)

        self.declare_parameter('v', rclpy.Parameter.Type.DOUBLE)
        self.declare_parameter('d', rclpy.Parameter.Type.DOUBLE)

        self.timer = self.create_timer(0, self.timer_callback)

    def timer_callback(self):
        speed = self.get_parameter('v').value
        steering_angle = self.get_parameter('d').value

        msg = AckermannDriveStamped()
        msg.drive.speed = float(speed)
        msg.drive.steering_angle = float(steering_angle)
        
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing Speed: {msg.drive.speed} | Steering Angle: {msg.drive.steering_angle}")
        

def main(args=None):
    rclpy.init(args=args)

    talker = Talker()
    
    rclpy.spin(talker)

    rclpy.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
