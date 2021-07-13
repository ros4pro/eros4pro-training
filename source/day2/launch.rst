Launch file
===========

When you just need to run one node, then it is easy to call `rosrun` on your node and it starts without problems.
Things get more complicated when you need to run several nodes.
While you could in theory just run them with `rosrun` one after the other, it will quickly get tedious, even more so when you need to supply some parameters to the nodes upon running them.

The solution to this problem are **launch files**. 
Launch files are useful for running multiple nodes simultaneously with a single ``roslaunch`` command.
They can also be used to read parameters into the parameter server.

.. note:: The `roslaunch` command automatically starts rosmaster if it isn't already running. This means you can skip the `roscore` command.

In the next sections of today's training we need to access the laptop's webcam and use `ar_track_alvar` to detect AR markers in the frame.
In this section we will be creating a launch file that we will need to accomplish that.
But first, we need to do some setup to get the webcam running properly.


Setup
-----

#. To access the laptop's webcam in ROS, we need to install an additional package. To do this, run the following command in a terminal window:

   .. code-block:: bash

      sudo apt install ros-noetic-usb-cam

#. In order to confirm that usb_cam has been properly installed, run:

   .. code-block:: bash

      roslaunch usb_cam usb_cam-test.launch

We should now see a new window with video feed from the camera. Open another terminal window and list all the available topics.

In the terminal window where we launched the camera feed, there is a yellow warning message telling us that the camera calibration file could not be found. Let's create this file. Ask an instructor for a checkered calibration target.

#. Use `rostopic list` to see what is the namespace for your camera.

#. Run the camera calibration node. Make sure to use the correct topic name and namespace. You can read more about camera calibration `here <https://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration>`_.

   .. code-block:: bash

      rosrun camera_calibration cameracalibrator.py --size 8x6 --square 0.0405 image:=/usb_cam/image_raw camera:=/usb_cam

#. Move the calibration target in front of the camera until you can press buttons for *calibrate*, *save*, and *commit*. Note that pressing *save* can freeze your computer for minutes. This is normal, just wait it out.

#. Install `ar_track_alvar` as follows:

  #. Navigate to ``catkin_ws/src`` folder.
  #. Clone the repository for ar_track_alvar and switch to the correct branch by running the terminal commands below

   .. code-block:: bash

      git clone https://github.com/rios-ai/ar_track_alvar.git
      cd ar_track_alvar
      git checkout feature/rios_bug_fix


Writing the launch file
-----------------------

The launch file will start four nodes, one of them our own to speed up the workflow later on.
The main structure of the launch file will be like this:

  .. code-block:: xml

    <launch>
      <node name="usb_cam" pkg="usb_cam" type="usb_cam_node" output="screen" >
        ...parameters...
      </node>

      <node name="image_view" pkg="image_view" type="image_view" respawn="false" output="screen">
        ...parameters...
      </node>
    
      ...more nodes...
    </launch>

1. Go through the `roslaunch wiki on nodes <https://wiki.ros.org/roslaunch/XML/node>`_ and `roslaunch wiki on parameters <https://wiki.ros.org/roslaunch/XML/node>`_ and get familiar with the syntax of a launch file.

2. From the wiki, find the information on:

  * how to use the ``<node />`` tag to run nodes within roslaunch file;
  * how to use the ``<param />`` tag and read parameters to the server.

3. Launch files typically go inside a folder named ``launch``. Create this folder inside your package alongside the src folder.

4. Your task is to create a launch file named ``ar_control.launch`` inside the ``ar_control_robotont`` package. Implement the following functionality in the launch file:

  #. Copy the contents of ``usb_cam/usb_cam-test.launch`` into your launch file;
  #. Integrate the contents of ``ar_track_alvar/pr2_indiv_no_kinect.launch`` into the launch file;
  #. Start the ``ar_control_robotont`` node.

.. note:: You can use the ``rospack find <package_name>`` command to find the required launch files.


To test your launch file, run the following command in a terminal window:

  .. code-block:: bash

    roslaunch ar_control_robotont ar_control.launch

As a result, a window showing the camera feed should open, and the lines your node prints out should appear in the terminal window.



Connect the topics
------------------

If we tried to detect AR markers at this point, it would not work because `ar_track_alvar` is currently looking for the camera image on the topic `/wide_stereo/left/image_color`. In order to let `ar_track_alvar` know where to find the camera frame, we need to change the following lines in the launch file:

  .. code-block:: xml

    <arg name="cam_image_topic" default="/wide_stereo/left/image_color" />
    <arg name="cam_info_topic" default="/wide_stereo/left/camera_info" />

Locate these lines in your launch file and figure out what topics we would need to listen to if our camera image comes from the `usb_cam` node started in the same launch file.

To get some hints, you can run the following commands in separate terminal windows:

  .. code-block:: bash

    roslaunch usb_cam usb_cam-test.launch
    rostopic list

The output will give you some ideas what topics exist when `usb_cam` is launched.


Help, errors!
-------------

If you found the correct topics and tested your launch file again, initially the output should look similar to what it was before.
However, there are now error messages present, telling us that '"torso_lift_link" passed to lookupTransform argument target_frame does not exist'.
This is because we do not have `torso_lift_link`.

To fix this, make sure that the `output_frame` value in your launch file is identical to `camera_frame_id`. If they are not, find out `camera_frame_id` and replace `torso_lift_link` with this more relevant output frame.


Visualise the result
--------------------

Next we will use RViz to visualize both the marker(s) in 3D space and the camera image. Open a new terminal window and run RViz for visualization. To do this, simply type ``rviz`` into the terminal

#. To visualize images from the camera, use the ``Add`` button to add an Image to your RViz configuration. Make sure to set the correct topic name for the Image.

#. Next, use the ``Add`` button to add a Marker.

#. Next, use the ``Add`` button to add a TF.

#. In the Displays panel of RViz, there is a section for Global Options. Change the Fixed Frame to the value specified in your launch file as the output_frame, e.g., usb_cam.

If everything is working, you should see images from the camera in a sub-window in RViz and when you place an AR tag in the camera's field of view, you should see marker(s) relative to the fixed frame.


