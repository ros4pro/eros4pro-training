Creating Nodes
==============

In this exercise, you will create a simple ROS node inside your new ``ar_control_robotont`` package.
A ROS node is an executable code file inside a ROS package.
Nodes can exchange information with other nodes.

For reference, take a look at `Understanding Nodes <http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes>`_.

#. Create a new folder named ``scripts`` inside the package. We will add our Python code files there.

#. In the scripts folder, create a file ``ar_control_node.py`` and open it in a text editor or an IDE of your choice.

#. Add the shebang and ROS import.

   .. code-block:: python

      #!/usr/bin/python3
      import rospy

#. Add a main function.

   .. code-block:: python
      
      #!/usr/bin/python3
      import rospy

      def main():
            pass

      if __name__ == "__main__":
            main()

#. Initialize your ROS node (within the main function).

   .. code-block:: python

      #!/usr/bin/python3
      import rospy

      def main():
            # Creating a node must happen before anything else ROS-related
            rospy.init_node("ar_control")

      if __name__ == "__main__":
            main()


#. Print a "Hello World" message using ROS print tools.

   .. code-block:: python

      #!/usr/bin/python3
      import rospy

      def main():
            # Creating a node must happen before anything lse ROS-related
            rospy.init_node("ar_control")

            # Print out a message
            rospy.loginfo("Hello world!")

      if __name__ == "__main__":
            main()


#. Do not exit the program automatically - keep the node alive.

   .. code-block:: python

      #!/usr/bin/python3
      import rospy

      def main():
            # Creating a node must happen before anything lse ROS-related
            rospy.init_node("ar_control")

            # Print out a message
            rospy.loginfo("Hello world!")

            # Keep the program running
            rospy.spin()

      if __name__ == "__main__":
            main()


   ``ROS_INFO`` is one of the many `logging methods <http://wiki.ros.org/rospy/Overview/Logging>`_.

   * It will print the message to the terminal output, and send it to the ``/rosout`` topic for other nodes to monitor.
   * There are 5 levels of logging: ``DEBUG, INFO, WARNING, ERROR, FATAL``.
   * To use a different logging level, use ``rospy.logdebug(msg)``, ``rospy.loginfo(msg)``, ``rospy.logwarn(msg)``, ``rospy.logerr(msg)`` or ``rospy.logfatal(msg)`` to set the appropriate level.


#. Build your program (node), by running ``catkin build`` in a terminal window

   * Remember that you must run `catkin build` from within your `catkin_ws` (or any subdirectory)
   * This will build all of the programs, libraries, etc in ``ar_control_robotont`` package.
   * In this case, it's just a single ROS node ``ar_control_node``.


Running a Node
--------------

#. Open a terminal and start the ROS master.

   .. code-block:: bash

      roscore
   .. note:: The ROS Master must be running before any ROS nodes can function.

#. Open a second terminal to run your node.

   * In a previous exercise, we added a line to our `~/.bashrc` file to automatically source `devel/setup.bash` in new terminal windows. This will automatically export the results of the build into your new terminal session.
   * If you're reusing an existing terminal, you'll need to manually source the setup files (since we added a new node):

     .. code-block:: bash

        source ~/catkin_ws/devel/setup.bash

#. Make the node executable

   .. code-block:: bash

        chmod u+x ~/catkin_ws/src/ar_control_robotont/scripts/ar_control_node.py

#. Run your node.

   .. code-block:: bash

      rosrun ar_control_robotont ar_control_node.py

   .. tip:: This runs the program we just created. Remember to use TAB to help speed up typing and reduce errors.

#. In a third terminal, check which nodes are running.

   .. code-block:: bash

      rosnode list
      
   In addition to the ``/rosout`` node, you should now see a new ``/ar_control`` node listed.

#. Enter :code:`rosnode kill /ar_control`. This will stop the node.

   .. note:: It is more common to stop a running node by using :kbd:`Ctrl+C` in the terminal window where the node was started.


Challenge
---------

#. Modify the node so that it prints something as a warning and your name as an error message.

#. Demonstrate the working node to an instructor.

