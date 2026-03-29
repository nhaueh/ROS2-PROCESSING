#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0 # Tạo một biến đếm để theo dõi số lần in
        
        # 1. Tạo một Timer: Cứ 1.0 giây thì gọi hàm timer_callback một lần
        self.create_timer(1.0, self.timer_callback)
        
        self.get_logger().info("Node py_test đã bắt đầu chạy với Timer!")

    # 2. Định nghĩa hàm Callback - Đây là hành động sẽ lặp lại mãi mãi
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("rfffffff: " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) # Lệnh spin cực kỳ quan trọng ở đây
    rclpy.shutdown()

if __name__ == "__main__":
    main()