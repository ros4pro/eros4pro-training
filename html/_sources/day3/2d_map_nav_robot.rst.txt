.. role:: bash(code)
   :language: bash

2D mapping and navigation on Robotont
-------------------------------------

Now that we have tested some SLAM and navigation packages in a simulation, let's try them out on a real robot - Robotont.

Establish connection to the robot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since in this section we would need to open serveral terminals, let's use the distributed ROS advantages and add the :bash:`export ROS_MASTER_URI=....` command to the end of the :bash:`.bashrc` file. So that every time you open a new terminal it will be configured to connect to the robot.

#. Open :bash:`.bashrc` for editing:



.. code-block:: bash

   gedit ~/.bashrc



#. Add the line :bash:`export ROS_MASTER_URI=http://192.168.200.XXX:11311` to the end of the file. NB! substitute the **XXX** with your robot number!


#. First, log into the robot using an SSH connection and start the mapping and localization (gmapping):

   .. code-block:: bash

      roslaunch robotont_demos 2d_slam_create_map.launch

#. Now let's open up another terminal and start the teleoperation node. When ROS_MASTER_URI is succesfully set in the .bashrc file, you should be able to control the robot now.

   .. code-block:: bash

      rosrun teleop_twist_keyboard teleop_twist_keyboard.py



#. To visualize the mapping, you can open up rviz and manually add displays as we did for simulated robot, or you can also use a preconfigured launch file:


   .. code-block:: bash

      roslaunch robotont_demos 2d_mapping_display.launch


#. To save the map and run amcl, use the same commands as you did with simulated robot.

#. To run the navigation on the Robotont, we have prepared a custom launch file. So, instead of the move_base.launch, we run:

   .. code-block:: bash

      roslaunch robotont_demos 2d_slam_navigation.launch


 
Tweaking ROS Navigation parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have the experience of how navigation works in ROS,
let's try tuning some parameters to improve (or not) the navigation software.

In your robotont\_navigation configuration folder,
the relevant files are those that begin with *costmap_* and *planner_*.

From these files, you can configure
how your robot uses the navigation stack.
The most important file here for you is *planner_local_params.yaml*.
From this file, you can tune the parameters for the planner.
Reference can be found here: http://wiki.ros.org/base_local_planner and here: http://wiki.ros.org/teb_local_planner.

1.  Open a new terminal and log into the robot via SSH. Use roscd to go to the :bash:`robotont_navigation/config` package.


2.  Now use :bash:`nano` to edit some of the configuration files to configure the planners
    and make it work better.

    What if you would change acceleration limits?
    What if you would try to increase or decrease the goal tolerance?
    What if you changed local and global map sizes in the launch file?
    You can use ROS Wiki to see what the parameters do and make the
    robot navigate more accurately.

3.  To test your new configuration, relaunch the :bash:`2d_slam_navigation.launch`.

4.  If you are satisfied with the performance of your navigation,
    congratulations!
