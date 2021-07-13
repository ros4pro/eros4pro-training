MoveGroup C++ interface for programming the manipulator
=======================================================

Brief introduction to MoveGroup C++ interface
---------------------------------------------
.. nugget::
  :id: 759fac38502a42d7bbf93105e8b38be8
  :name: MoveGroup C++ interface
  :activity: RoboNuggets

Before we start coding
----------------------
In this section we are going to learn how to program a manipulator robot using the MoveGroup C++ interface. For practicing how to program robot manipulators by using MoveGroup C++ interface, let’s use the digital twin by launching the demo.launch. The following list of nuggets explain different ways we can program robot manipulators using MoveGroup C++ interface. All the example code solutions can be found in the repository for `movegroup_interface_demo <https://github.com/ut-ims-robotics/movegroup_interface_demo>`_. Clone it and build it.

The API refrence can be found `here <http://docs.ros.org/noetic/api/moveit_ros_planning_interface/html/classmoveit_1_1planning__interface_1_1MoveGroupInterface.html>`_

Keep in mind that in the example code, the execute function has been commented out for safety reasons. When working with a digital twin it is safe to uncomment the line.

Planning to a Pose Goal
-----------------------

.. nugget::
  :id: 579c5c52952f49eda08229beef7b1d5c
  :name: MoveGroup C++ interface: planning to a pose goal
  :activity: RoboNuggets

Planning to a Joint Value Goal
------------------------------

.. nugget::
  :id: e42cbc47f95843f2bb38286b53daa41a
  :name: MoveGroup C++ interface: planning to a joint value goal
  :activity: RoboNuggets

Planning to a Named Goal
------------------------

.. nugget::
  :id: e32cef73d12c42beafcff210d20448ed
  :name: MoveGroup C++ interface: planning to a named goal
  :activity: RoboNuggets

Computing a Cartesian Path
--------------------------

.. nugget::
  :id: 5010ab1c38df48258ea2522284565686
  :name: MoveGroup C++ interface: planning a Cartesian path
  :activity: RoboNuggets
