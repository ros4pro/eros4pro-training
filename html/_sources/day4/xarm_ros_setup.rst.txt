Installing xArm7 packages for ROS Noetic
========================================

In the src folder of the catkin workspace:

.. code-block:: bash

  git clone https://github.com/xArm-Developer/xarm_ros.git
  cd xarm_ros
  git checkout eb2a4a14144a700ab1d64ef755dc8229cbe6553b
  catkin build
  sudo apt install ros-noetic-moveit-resources-prbt-moveit-config
