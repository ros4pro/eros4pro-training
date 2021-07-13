Action Client for opening/closing the gripper
=============================================

While there are robots that enable gripper control through MoveIt, it is quite often we find that robot manufacturers have opted for an alternative approach, e.g. ROS actions. For that reason, it is important to carefully read any documentation provided by the manufacturer. From the xarm_ros `README <https://github.com/xArm-Developer/xarm_ros#gripper-control>`_, we can find that xArm gripper is, indeed, controlled via ROS action. Luckily, the manufacturer has even provided the sample code for programming an Action Client for the Action Server that controls the gripper. We can find this sample code in the `xarm_gripper <https://github.com/xArm-Developer/xarm_ros/tree/master/xarm_gripper>`_ package which is already installed with the rest of the xarm_ros software.

In order to first test the sample node, we again need to connect with the xArm7 and launch the familiar file:

.. code-block:: bash

  roslaunch xarm7_gripper_moveit_config realMove_exec.launch robot_ip:=<your controller box LAN IP address> 

Next, we run the provided action client node as instructed in the xarm_ros README.

.. code-block:: bash

  rosrun xarm_gripper gripper_client 500 1500

The first numeric argument describes how open (on the scale from 0 to 850) the gripper is requested to become. The second numeric argument describes the speed of gripper fingers. Let’s try to run the gripper_client with different values from 0 to 850 while keeping the speed at 1500. Figure out what would be the optimal value for holding the sponge we use for our pick-and-place task.

Investigate the source code in gripper_client.cpp. When we wish to create our own node for controlling the xArm7’s gripper, we can make use of this sample code by copying the relevant parts.
