#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # Gazebo models
    models_dir = get_package_share_directory('my_custom_world') + '/models'

    banana_model_path = os.path.join(models_dir, 'banana', 'model.sdf')
    banana_position = [1.0, 0.0, 0.3] 
    banana_orientation = [-1.9, 0.0, 1.57]
 

    apple_model_path = os.path.join(models_dir, 'apple', 'model.sdf')
    apple_position = [-1.0, 0.0, 0.3]
    apple_orientation = [-1.9, 0.0, 1.57]

    # Spawn banana
    spawn_banana = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            arguments=['-entity', 'banana', '-file', banana_model_path, '-x', str(banana_position[0]), '-y', str(banana_position[1]), '-z', str(banana_position[2]),
            '-R', str(banana_orientation[0]), '-P', str(banana_orientation[1]), '-Y', str(banana_orientation[2])],
            output='screen'
        )
    
    # Spawn apple
    spawn_apple = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            arguments=['-entity', 'apple', '-file', apple_model_path, '-x', str(apple_position[0]), '-y', str(apple_position[1]), '-z', str(apple_position[2]),
            '-R', str(apple_orientation[0]), '-P', str(apple_orientation[1]), '-Y', str(apple_orientation[2])],
            output='screen'
        )
    # create and return launch description object
    return LaunchDescription(
        [
            spawn_banana,
            spawn_apple
        ]
    )
