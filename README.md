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
# rostopic echo
```bash
rostopic echo /turtle1/pose
x 값 :가로
y 값 : 세로
theta : 거북이 방향
linear_velocity : 거북이가 움직이는 속도
angular_velocity : 회전 속도
```
# rostopic 토픽정리
```bash
토픽 목록 확인
rostopic list

/turtle1/cmd_vel(거북이 움직임 명령)

/turtle1/color_sensor(배경색을 감지)

/turtle1/pose(거북이 실시간 위치 방향)

```
``` bash
토픽의 메시지 타입확인
rostopic type /turtle1/cmd_vel

geometry_msgs/Twist
```
```bash
메시지 구조 확인


$ rosmsg show geometry_msgs/Twist(앞뒤,회전)

geometry_msgs/Vector3 linear(앞,뒤(선속도))
geometry_msgs/Vector3 angular(회전)
   
```