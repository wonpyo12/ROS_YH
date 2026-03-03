# ROS devalopment
- ubuntu 20.04
- Ros notic
# ROS install
1. source list
``` bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
```bash
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
```bash
sudo apt update
sudo apt install ros-noetic-desktop-full
```
```bash
source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
5. Create a ROS Workspace
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
```
# rospack
```bash
rostopic echo /turtle1/pose
x 값 :가로
y 값 : 세로
theta : 거북이 방향
linear_velocity : 거북이가 움직이는 속도
angular_velocity : 회전 속도
```

