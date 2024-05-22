#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Gazebo models
    models_dir = get_package_share_directory('my_custom_world') + '/models'

    my_env_model_path = os.path.join(models_dir, 'my_env', 'model.sdf')
    my_env_position = [1.0, 0.0, 0.3] 
    my_env_orientation = [-1.9, 0.0, 1.57]
 
    # Spawn custom environment
    spawn_my_env = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            arguments=['-entity', 'my_env', '-file', my_env_model_path, '-x', str(my_env_position[0]), '-y', str(my_env_position[1]), '-z', str(my_env_position[2]),
            '-R', str(my_env_orientation[0]), '-P', str(my_env_orientation[1]), '-Y', str(my_env_orientation[2])],
            output='screen'
        )
    
    # create and return launch description object
    return LaunchDescription(
        [
            spawn_my_env
        ]
    )
