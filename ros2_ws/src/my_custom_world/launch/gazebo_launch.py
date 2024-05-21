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
