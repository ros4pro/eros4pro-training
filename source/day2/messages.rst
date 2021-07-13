Publisher & Subscriber
======================

In this exercise, we will explore the concept of ROS messages and topics. The first type of ROS communication that we will explore is a one-way communication called **messages** which are sent over channels called **topics**. Typically one node publishes messages on a topic and another node subscribes to messages on that same topic.
The construct that can publish messages is called a publisher, and the one receiving messages is called a subscriber.


Writing a Publisher
-------------------

Work your way through the video tutorials in the window below to learn how to write a simple ROS publisher.
The videos will also introduce you to controlling the Robotont robot.
To move to the next video, click on the arrow buttons next to the percentage above the video's top right corner.

.. nugget::
  :id: 470c9b7fc65c4dc783c255b449e8386f
  :name: Writing a ROS Publisher in Python


Let's add a publisher to the same `ar_control_node.py` file we created earlier. We will add a publisher that will publish messages of type Twist - the messages used for making Robotont drive. Once we are done writing the code, we will try it out on the actual Robotont robot. Take a look at the documentation of the `geometry_msgs/Twist <https://docs.ros.org/en/noetic/api/geometry_msgs/html/msg/Twist.html>`_ message.

Below is an overview of the steps detailed in the video tutorial. For more details, refer back to the videos.

#. First, add an import to `ar_control_node.py` to be able to use Twist messages.

   .. code-block:: python

      from geometry_msgs.msg import Twist

#. Add the publisher by calling `rospy.Publisher()` and specifying the name of the topic where the publisher will publish its messages, message type, and queue size. Do it before calling `rospy.spin()` in the code.

   .. code-block:: python

      # Create a publisher for publishing Twist messages
      velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

#. Create a Twist message that tells the robot to go forward.

#. Make the code keep running and publishing the Twist message at a rate of 1 Hz. In most applications, we would set the frequency higher, such as 10 Hz or even more, but here we will set it slow enough to be able to read the terminal output. Refer back to the video tutorial above on how to do this. Print out a log message every time you publish a new message.

#. Run the code by typing the following commands in separate terminal windows. The output should be your created Twist message being printed out in the terminal at a rate of 1 Hz.

   .. code-block:: bash

      roscore
      rosrun ar_control_robotont ar_control_node.py

#. Take a look at what your publisher is doing. To do this, open another terminal window and look at the topic where the publisher is publishing its Twist messages.

   .. code-block:: bash

      rostopic echo /cmd_vel


Running the code in simulation
------------------------------

Before you run your code on a physical robot, it is always a good idea to try it out in simulation first to catch potentially dangerous bugs.

We will use a simnulation environment called Gazebo to visualise Robotont and its movements.
Running the code will happen exactly as with a real robot, and the code is exactly the same.
The only difference is that the robot will move in simulation, not in the real world.

#. Open Gazebo with a model of Robotont already in it:

   .. code-block:: bash

      roslaunch robotont_gazebo world_minimaze.launch

#. Run your node with Gazebo open in the background. The model Robotont should move according to your Twist message.

#. **Edit the Twist message to add a turning component and show the messages published to /cmd_vel topic to an instructor.**



Running the code on a Robotont
------------------------------

1. Ask an instructor for a Robotont robot. Turn it on. Every Robotont has its own Wi-Fi access point, which means that in order to connect to the Robotont, you will need to connect your laptop to the same network your Robotont is broadcasting. You will find the number of your robot on its onboard computer. Your robot's Wi-Fi network will be named ``robotont-X``, where X is the number of your Robotont. Ask an instructor for the Wi-Fi password.

2. To make the robot move according to our Twist message, we will be using something called distributed ROS. Distributed ROS allows us to keep running the code in the laptop as we have been doing so far, but makes it so the laptop and the Robotont share a ROS environment. This means that if we publish moving commands to the `cmd_vel` topic, the robot will move because it is listening to the `cmd_vel` topic.

Find out how to make the connection between the laptop and the Robotont from the following video tutorial.

.. nugget::
  :id: 30a484cbb65249828887d1055dd87278
  :name: Distributed ROS

3. If you have successfully set up distributed ROS, you can now run your code on the laptop and the Robotont will move. Rosmaster is already running on the robot, so you can simply use the `rosrun` command as before.

4. Play around with different Twist messages and make your robot drive in either a square, circle or triangle.

**Show the robot driving the geometric shape to an instructor.**



Writing a Subscriber
--------------------

In order to receive messages published by a publisher, we need to add a subscriber to our code.
We will implement a very simple subscriber that can receive information about AR markers published by the `ar_track_alvar` node.

#. In the laptop (not on the robot), start the launch file created in the previous section, ``camera_ar_track.launch`` to start the laptop's webcam and launch `ar_track_alvar`.

   .. code-block:: bash

      roslaunch ar_control_robotont ar_control.launch

#. Now `ar_track_alvar` is publishing information about AR markers detected in the laptop's webcam frame.

Now we can move on to writing the subscriber. We will be adding more code to `ar_control_node.py`.

#. First, add an import to be able to recognise the message type published by `ar_track_alvar`, AlvarMarkers.

   .. code-block:: python

      from ar_track_alvar_msgs.msg import AlvarMarkers

#. We will first add the subscriber and then add the other code necessary to make it run. To create a subscriber, simply call ``rospy.Subscriber()`` and specify the name of the topic the subscriber should listen to, the message type to expect, and the callback that handles the messages once they are received. Create the subscriber after creating the node but before calling rospy.spin().

   .. code-block:: python

      # Creating a node must happen before anything else ROS-related
      rospy.init_node("ar_control")
	
      # Create a subscriber to listen to messages published on the ar_pose_marker topic
      rospy.loginfo("Subscribing to ar_pose_marker")
      rospy.Subscriber("ar_pose_marker", AlvarMarkers, ar_message_handler)

#. Add a callback function for handling AlvarMarkers messages. The input parameter to the callback function contains the last message of type AlvarMarkers that our subscriber received. This callback prints out the ID's of all detected markers if any are detected in the webcam's frame, or an informative message if none are detected.

   .. code-block:: python

      def ar_message_handler(data):
         if len(data.markers) > 0:
            for marker in data.markers:
               rospy.loginfo("Detected marker with ID " + str(marker.id))

         else:
            rospy.loginfo("No AR markers detected.")
	    
That's it, the subscriber is now complete. In this example, we only printed out the ID's of detected markers. The other components of the AlvarMarkers message can be accessed in a similar manner. Spend some time experimenting with printing out different components of the AlvarMarkers message.

Remember, you can see the messages being published on the `ar_pose_marker` topic by running the following in a new terminal window:

   .. code-block:: bash

      rostopic echo /ar_pose_marker

**Figure out how to print out the x component of the marker's position, print it out, and show the result to an instructor.**
