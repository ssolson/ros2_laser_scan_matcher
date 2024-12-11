import os
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration



def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    odometry_node = Node(
        package='ros2_laser_scan_matcher',
        parameters=[{
            'base_frame': 'base_link',
            'odom_frame': 'odom_matcher',
            'laser_frame': 'laser_frame',
            'publish_odom': '/odom_matcher',
            'publish_tf': True
        }],
        executable='laser_scan_matcher',
        name='odometry_publisher',
    )

    # Create and return the Launch description
    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='True',
                                             description='Flag to enable use_sim_time'),
        odometry_node
    ])
