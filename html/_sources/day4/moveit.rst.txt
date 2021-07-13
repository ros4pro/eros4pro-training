Motion planning and MoveIt, MoveIt GUI
======================================

.. nugget::
  :id: 3956ed745d2641ed9d1c821f63d3973c
  :name: Motion Planning and ROS MoveIt
  :activity: RoboNuggets

Let’s learn the specifics of the MoveIt GUI on a digital twin of the robot. We can start the digital twin with the following launch-file.

.. code-block:: bash

  roslaunch xarm7_gripper_moveit_config demo.launch

The following learning nugget demonstrates the main features of MoveIt GUI. Even though everything is exemplified using a Franka Emika Panda manipulator, MoveIt is universal to all robot manipulators, so we can practice the same concepts with the digital twin of the xArm7.

.. nugget::
  :id: a9a1349f5c4f456b9c699c0264121233
  :name: MoveIt GUI
  :activity: RoboNuggets

Next let’s start MoveIt GUI for controlling the real xArm7:

.. code-block:: bash

  roslaunch xarm7_gripper_moveit_config realMove_exec.launch robot_ip:=<your controller box LAN IP address>

As a first step we need to make sure that the robot would not collide with the desk/cart it is mounted to. We can use the Scene Objects tab in RViz Motion Planning to add a box (size 2,0; 0,2; 2,0) to represent the cart that the xArm7 should avoid when planning its motions. Use the ”+” button to add the box, slide it into place, and hit “publish” to make the box truly a component of the robot’s environment. The final view of the robot and its environment should look similar to this figure.

.. figure:: ../_static/pics/xarm_platform.png
  :width: 600pt

Try planning to different poses for the manipulator and get a feel of how the robot behaves in the real world.

Enable E-stop, shut down the MoveIt GUI, and shut down the robot.
