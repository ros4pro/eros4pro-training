Find the Robot
==============

The robots have been placed in a secluded area in the classroom.
You are not allowed to enter said area.

However, you are allowed to connect to the robot's wifi network. The wifi password is the same as usual.

The robot's own password has been changed, so you cannot `ssh` into the robot directly.

Your task is to use ROS2 tools to find a theoretical way how you could move the robot.

The next task is to write code to actually move the robot out of the secluded area, to you.
But first, find a way and make a plan.

Install ROS2
------------

You will need to install ROS2 on your system.

Start by authorizing an appropriate GPG key.

   :code:`$ sudo apt update && sudo apt install curl gnupg2 lsb-release`
   :code:`$ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg`
   
Then add the repository to sources list.

.. code-block:: bash

   $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

Now update the apt repository caches.

   :code:`$ sudo apt update`

Install ROS2 and argcomplete.

   :code:`$ sudo apt install ros-foxy-desktop`
   :code:`$ sudo apt install -y python3-argcomplete`

Source the environment. It will complain a bit.

   :code:`$ source /opt/ros/foxy/setup.bash`

To get rid of the complaints, you'll need to modify the ``.bashrc`` file a bit.
Open up the ``~/.bashrc`` file using your favourite test editor (ask an instructor if you have trouble finding it), comment out the line that sources ``/opt/ros/noetic/setup.bash`` and instead add the following line to the end:

   :code:`$ source /opt/ros/foxy/setup.bash`

Then you can close and re-open a terminal. It should not complain anymore.

Hack the robot
--------------

Now find a way to take over control of the robot. Use ROS2 tools for this.
