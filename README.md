# Create-ROS2-World

# Step 1: Launch Gazebo Empty World

**1. Create a ROS 2 package (if you don't already have one):**

```bash
cd /ros2_ws/src/
ros2 pkg create my_custom_world --build-type ament_cmake
```

**2. Create a launch file:**

```bash
cd /ros2_ws/src/my_custom_world
mkdir launch
touch launch/gazebo_launch.py
```

**3. Edit the launch file (gazebo_launch.py):**

```bash
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    gazebo_pkg_share = FindPackageShare(package='gazebo_ros').find('gazebo_ros')

    # Include the Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution([gazebo_pkg_share, 'launch', 'gzserver.launch.py'])])
    )

    # Optionally, include the Gazebo client (GUI)
    gzclient = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([PathJoinSubstitution([gazebo_pkg_share, 'launch', 'gzclient.launch.py'])])
    )

    return LaunchDescription([
        gazebo,
        gzclient
    ])
```
**4. Modify CMakeLists.txt:**

```bash
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

```

**5. Build your package and source workspace**

```bash
cd /ros2_ws
colcon build --packages-select my_custom_world
source /ros2_ws/install/setup.bash
```
**6. Launch Gazebo using the launch file:**

```bash
ros2 launch my_custom_world gazebo_launch.py
```