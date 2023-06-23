# Lab 0: Docker and ROS 2

## Docker Hub ID
[ardnep/f1tenth_lab1](https://hub.docker.com/r/ardnep/f1tenth_lab1)

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: ```source /opt/ros/foxy/setup.bash``` sources the ROS2 installation which adds ROS2's packages to the environment. Without this, we cannot access ROS2's packages in the terminal. 

```source install/local_setup.bash``` on the other hand is responsible for adding the packages available in the workspace to the environment. 

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: In the case that a subscriber is not receiving messages fast enough, the queue size limits the amount of queued messages. 

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: If ```ros2 launch``` is called from within the directory where the launch file is ```colcon build``` doesn't need to be called again. But, calling it when it is installed within the package requires ```colcon build``` since the launch file installed in the previous build will not reflect the changes.

### Q4 (optional): While completing this lab, are there any parts of the tutorial and lab instruction that could be improved?

Anwer: (FILL ME IN)
