Teleoperation using a remote ROS Master
---------------------------------------

#. The robot driver subscribes to a specific type of messages called *velocity commands*. The standard name for this topic is :code:`/cmd_vel`.

#. The message is of type :code:`geometry_msgs/Twist` and it's structure can be found from `ROS wiki <https://docs.ros.org/api/geometry_msgs/html/msg/Twist.html>`_.

To set and control the robot speed, we need to continuously publish the velocity commands. Tomorrow we look how to write the publishers from scratch, but for now let's use a package that listens keyboard events and publishes them as :code:`Twist` messages.

    .. Note:: In video you are going to see that in addition to the teleop_twist_keyboard.py there is "cmd_vel:=robotont/cmd_vel", but we don't have to use this kind of ending.


And now Follow the video to get your robot moving remotly:

.. nugget::
  :id: 30a484cbb65249828887d1055dd87278
  :name: Distributed ROS


.. hint:: Notice that the teleop node only receives keypresses only when the terminal window is active.

.. tip:: Use :code:`CTRL + C` to stop the node.

In addition to the nodes let's see which topics are published during the teleopartion. Just to make things a bit more interesting, let's use the capabilites of distributed ROS. As by default the computer would like to use hostnames, we have to make sure that it uses ip-addressis, because for robot the laptop-2, laptop-3 are not added into hosts file and they are unknown for a robot.

For that we are going to connect another laptop into the same robot. Both of you have to make:

   .. code-block:: bash

      export ROS_MASTER_URI=http://<robot ip>:11311
      export ROS_IP=<your computer ip>

Now try to run teleop_twist_keyboard from one computer and try to listen the topic from another computer by:

First laptop:

   .. code-block:: bash

      rosrun teleop_twist_keyboard teleop_twist_keyboard.py

Second laptop:

   .. code-block:: bash

      rostopic list

With this command you are going to see all the topics which are published and with the following command you will get more precise information what's going on:

   .. code-block:: bash
   
      rostopic echo /cmd_vel

If everything went correctly, then you should see the odometry of the robot.





