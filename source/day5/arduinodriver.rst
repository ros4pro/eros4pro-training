Driver for Ultrasonic Sensor
============================

In this exercise we will write a driver for an ultrasonic sensor using the ``rosserial`` software package.

Communicating with Arduino
--------------------------

Install Arduino IDE on your system. You can find the IDE here_.

Then download this_ sample code, compile it and upload it to Arduino. If you have never used Arduino before then ask for an instructor's help with this part.

Back to ROS
-----------

In this lab we are using rosserial package to relay data from Arduino Nano to our ROS-based computer over a serial (USB) interface.

Install ``rosserial`` using apt.

   :code:`$ sudo apt install ros-noetic-rosserial-arduino ros-noetic-rosserial`

Then build the necessary libraries for Arduino.

   :code:`$ cd ~/Arduino/libraries/`
   
   :code:`$ rosrun rosserial_arduino make_libraries.py ./`

Now open the Arduino IDE again and open up ``File > Examples > ros_lib > HelloWorld`` from the menus.

Upload this piece of code to the Arduino as is.

Then open up a terminal window and run ``serial_node.py`` from ``rosserial``.

   :code:`$ rosrun rosserial_python serial_node.py /dev/ttyUSB0`

If your Arduino is connected to some other port than ``/dev/ttyUSB0`` then modify the command accordingly.

These commands started a ROS node. Use the regular ROS commands to find out which node it started, what does it publish and observe the published data.

Read the Arduino code that produced this result and try to understand as much of it as you can. Ask the instructors about parts that you do not understand.

Integrating two pieces of code
------------------------------

Now it is time to put the previous two Arduino codes together.

Integrate the ultrasonic sensing code and the ``HelloWorld`` example into one file.

Then modify the code such that the data published by the node would be data obtained from the ultrasonic sensor instead.

Optional: visualize data
------------------------

Visualize the ultrasonic data in Rviz.

Optional: move robot
--------------------

Make a robot move back and forth according to how you hold something (your hand, a piece of cardboard, or something) in front of the robot.
You can either make the robot just move forward when the hand is closer and backward when it is further away from the sensor, or you can try to mimic the hand's position using the robot (the distance from the hand to sensor is proportional to the distance from robot to wall).

.. _here: https://www.arduino.cc/en/software
.. _this: https://github.com/unitartu-edu/ultrasonic_ranger_arduino.git
