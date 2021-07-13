Creating Packages
=================

In this exercise, we will create our own ROS package which we will continuously improve during today's training. Eventually it will enable us to control the Robotont robot with the help of AR markers in the environment.

We already have a workspace, and have even used ``catkin build`` a few times. Now we will create our own package to run some custom code in the later parts of this training.

#. Your goal is to create a Catkin package that:

   * has the name ``ar_control_robotont``
   * has the following dependencies:

       - ar_track_alvar_msgs
       - geometry_msgs
       - rospy
       - tf

#. To find out how to create a Catkin package, visit the ROS Wiki: `Create a Package <http://wiki.ros.org/ROS/Tutorials/CreatingPackage>`_ section and `catkin_tools <https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_create.html>`_  documentation.

   .. note:: Remember that all packages should be created inside a workspace's src directory.
  
#. If you were successful at creating the package then there will be a folder named ``ar_control_robotont`` inside the src directory. Navigate into that folder and open the ``package.xml`` file for editing.
   
#. Change the description, version, author and other information as you like.

#. Finally, build the package with:

   .. code-block:: bash

      catkin build

#. Show the created package to the instructor.

.. hint:: If you forgot to add a dependency when creating a package, you can add additional dependencies in the ``package.xml`` file.

