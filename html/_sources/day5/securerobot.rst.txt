Where Is That Security?
=======================

Getting the robot out of the enclosure was easy enough. So where is that security that ROS2 should be famous for?

For this we will be using commands that belong to the category ``ros2 security``.

First, we need to turn on the security using environment variables. For this, actually log in to the robot (ask the instructors for password), stop the driver node and set the following environment variables:

   .. code-block:: bash
      
      export ROS_SECURITY_ENABLE=true
      export ROS_SECURITY_STRATEGY=Enforce

This means that the security will be enforced: a node will not be able to subscribe or publish unless the security policy allows it and it has the means to authenticate itself. There is also a ``Permissive`` policy that will simply run a node without encryption if something is wrong.

Now we need to create some security keys. For this, use the following commands.

   .. code-block:: bash
     
     cd ~/dev_ws   
     ros2 security create_keystore demo_keystore
     export=~/dev_ws/demo_keystore

This creates a keystore for storing the keys.

   .. code-block:: bash
     
     ros2 security create_key demo_keystore /clearbot_driver

This creates some demo keys for running the clearbot driver.

   .. code-block:: bash
   
      ros2 run clearbot_driver clearbot_driver --ros-args --enclave /clearbot_driver

This runs the driver node with the created keys.

Now we need something that would try to publish to it. Try running a publisher from your computer to publish velocity commands to it. Verify that the robot does not work.

The easiest way to get things to work is also the nastiest, but in the interest of time we shall use it.

Copy the entire keystore to your computer, export the location as ``ROS_SECURITY_KEYSTORE``, set ``ROS_SECURITY_ENABLE`` and ``ROS_SECURITY_STRATEGY`` as well and run the node with ``--ros-args --enclave /clearbot_driver`` in the end of the command. Ask for an instructor's help if you need assistance with the copying part.

You should now be able to move the robot.
