Catkin Workspaces
=======================

In this exercise, we will create a ROS catkin workspace. We will also see how to manage larger workspaces with the help of simple automation.

Any ROS project begins with making a workspace. The workspace will contain all the things related to this project. Typically you would have multiple workspaces and switch between them or combine them by extending one from another. 

We will consider this training as one project and create a single workspace that will be used throughout the training. All your developed packages will be developed in this workspace. To keep consistency with other ROS tutorials, we name the workspace ``catkin_ws`` and place it under the home directory.

Further information
-------------------

* Steps to creating a workspace:  `Creating a Workspace <http://wiki.ros.org/catkin/Tutorials/create_a_workspace>`_
* Using a catkin workspace:  `Using a workspace <http://wiki.ros.org/catkin/Tutorials/using_a_workspace>`_


Video tutorial
--------------

Introduction to catkin workspaces and instructions on how to create one are available in video format.
The terminal commands described in the video tutorial are also presented below the video in text format.

.. nugget::
  :id: e1485b821400482794e32613024a0288
  :name: Setting up catkin workspaces


Create a Catkin Workspace
-------------------------

#. Start by creating a root directory for the workspace:

   .. code-block:: bash

      cd 
      mkdir -p catkin_ws/src

#. Next, we need to initialize the workspace. But before doing that, we have to make sure which workspace our new `catkin_ws` is going to extend. The rule is that the new initialized workspace will always extend the workspace that is currently sourced.

#. Since we do not yet have any workspaces created, we will initialize our new ``catkin_ws`` so that it extends the default workspace already present in the ROS installation. The only thing we need to do is make sure we have sourced the default workspace before using the init command:

   .. code-block:: bash

      source /opt/ros/noetic/setup.bash
      cd ~/catkin_ws
      catkin init
      
#. The output of the ``catkin init`` command tells you which workspaces were extended:
   
   .. code-block:: bash

      ...
      Extending:             [cached] /opt/ros/noetic
      ...

  .. note:: Look for the statement "Workspace configuration appears valid", showing that your catkin workspace was created successfully. If you forgot to create the ``src`` directory, or did not run `catkin init` from the workspace root (both common mistakes), you'll get an error message like "WARNING: Source space does not yet exist".

#. Build the workspace. This command may be issued anywhere under the workspace root-directory (i.e. ``catkin_ws``).

   .. code-block:: bash

      catkin build
      ls

   * See that the ``catkin_ws`` directory now contains additional directories (build, devel, logs).

#. These new directories can be safely deleted at any time (either manually or using ``catkin clean``). Re-run ``catkin build`` to re-create the build/devel/logs directories.

   .. code-block:: bash

      catkin clean
      ls
      catkin build
      ls


   .. note:: Catkin never changes any files in the ``src`` directory. 

#. Make the workspace visible to ROS. Source the setup file in the devel directory.

   .. code-block:: bash

      source ~/catkin_ws/devel/setup.bash


   * This file MUST be sourced for every new terminal. Add this to your ``~/.bashrc`` file to source your new workspace automatically each time a new terminal is opened:

     .. code-block:: bash

        echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc


Now you have successfully created a Catkin workspace.
This workspace will be used throughout this training to get familiar with ROS.
Everything we do in ROS must be inside the workspace.


Automating workspace management
-------------------------------

The src directory inside a Catkin workspace contains all the packages needed for a project.
In the coming parts of this training, we will be working with the Robotont robot.
To easily handle all the packages required to use the Robotont and run simulations containing a Robotont, follow the steps described in the video tutorial below.

.. note:: The .rosinstall file you will need is available `here <https://github.com/robotont/robotont-setup/blob/noetic-devel/ansible/roles/catkin/files_for_laptops/.rosinstall>`_.

.. nugget::
  :id: 6e5d2b1148304fc0940743cade90dc8f
  :name: Managing large catkin workspaces


By this point, you should have a Catkin workspace that contains the Robotont packages.
While many things can be accomplished by simply downloading ROS packages from the Internet, it is important to know how to create your own packages from scratch.
In the next section we will see how to create a ROS package inside the workspace's src directory.


