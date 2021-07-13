Pick-and-place task
===================

As a final task, let’s create a node that commands the xArm to complete a skeleton pick-and-place routine, which would consist of the following steps:

#. Robot approaches the pickup station, stops right on top of it
#. Robot opens the gripper
#. Robot moves only downward to the pickup station
#. Robot closes the gripper
#. Robot moves to the place station
#. Robot opens the gripper

Since currently, we can test the code that uses the MoveGroup C++ interface even with the digital twin, it is probably easiest to first program the sequence of all the movements of the manipulator. And then add lines for controlling the gripper and test it using the physical robot.
