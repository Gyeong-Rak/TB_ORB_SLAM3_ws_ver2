from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    # Declare arguments
    vocabulary_file_arg = DeclareLaunchArgument(
        'vocabulary_file',
        default_value='/home/gyeongrak/TB_ORB_SLAM3_ws_ver2/src/ORB_SLAM3/Vocabulary/ORBvoc.txt',
        description='Path to the ORB-SLAM3 vocabulary file'
    )

    config_file_arg = DeclareLaunchArgument(
        'config_file',
        default_value='/home/gyeongrak/TB_ORB_SLAM3_ws_ver2/src/orbslam3_ros2/config/stereo-inertial/ZED2i.yaml',
        description='Path to the ORB-SLAM3 configuration file'
    )

    bool_rectify_arg = DeclareLaunchArgument(
        'bool_rectify',
        default_value='true',
        description='Enable or disable rectification'
    )

    bool_equalize_arg = DeclareLaunchArgument(
        'bool_equalize',
        default_value='false',
        description='Enable or disable histogram equalization'
    )

    # ORB-SLAM3 Node
    orb_slam3_node = Node(
        package='orbslam3',
        executable='stereo',
        name='orb_slam3',
        output='screen',
        arguments=[
            LaunchConfiguration('vocabulary_file'),
            LaunchConfiguration('config_file'),
            #LaunchConfiguration('bool_rectify'),
            LaunchConfiguration('bool_equalize'),
        ],
        remappings=[
            ('/imu', '/zed/zed_node/imu/data'),
            ('/camera/left', '/zed/zed_node/left/image_rect_color'),
            ('/camera/right', '/zed/zed_node/right/image_rect_color'),
            ('/camera/depth', '/zed/zed_node/depth/depth_registered'),
            ('/camera/rgb', '/zed/zed_node/left/image_rect_color')
        ]
    )

    return LaunchDescription([
        vocabulary_file_arg,
        config_file_arg,
        bool_rectify_arg,
        bool_equalize_arg,
        orb_slam3_node
    ])
