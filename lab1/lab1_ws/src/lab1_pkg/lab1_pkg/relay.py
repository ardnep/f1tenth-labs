#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.relay_callback,
            10
        )
        self.publisher_ = self.create_publisher(
            AckermannDriveStamped,
            'drive_relay',
            10
        )

    def relay_callback(self, msg):
        speed = msg.drive.speed * 3
        steering_angle = msg.drive.steering_angle * 3

        relay_msg = AckermannDriveStamped()
        relay_msg.drive.speed = speed
        relay_msg.drive.steering_angle = steering_angle

        self.publisher_.publish(relay_msg)
        self.get_logger().info(f"Relaying Speed: {speed} | Steering Angle: {steering_angle}")


def main(args=None):
    rclpy.init(args=args)

    relay = Relay()

    rclpy.spin(relay)

    relay.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
