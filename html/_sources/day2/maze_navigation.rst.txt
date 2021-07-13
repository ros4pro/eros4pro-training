Advanced task: Maze Navigation using AR Markers
===============================================

There is a maze in the middle of the classroom.
In this task we will be navigating a robot through this maze based on AR markers on the walls.

In the previous task we used a single AR marker to control the robot, so it made no difference what marker it was.
In this task the robot will see many AR markers, each of them different.

The core principle of this task is to move from one AR marker to another, so the code will need to keep track of which AR marker to search for.
Additionally, it is possible that at any given time point there are several AR markers in the camera frame-
The robot should ignore every marker that is not the one it is currently following.

You can find a simulated maze by running the following in a terminal:

   .. code-block:: bash

      roslaunch robotont_gazebo world_minimaze_ar.launch


Differentiate between markers
-----------------------------

If there is not already a method for determining AR marker ID in your code, add it now. 

Add a variable to your code that determines which marker the robot is currently following (the target marker). Print out something when the robot sees this marker and make it so the robot ignores all other markers.


Follow one marker
-----------------

Once your robot is capable of focusing on a single AR marker, turn towards the marker and get close to it.
You will need to use the marker's position information to center the robot towards the marker and to stop a reasonable distance from it.

Your robot should turn on the stop until it finds the marker it is searching for, center itself, and drive to the marker.


Find and follow next marker
---------------------------

Now that your robot has arrived at the first marker, the identificator of the target marker should be changed in the code.
Repeat the actions done for the previous marker - find it, center towards it and follow it.


Navigate the maze
-----------------

Find out the ID's of the markers on the walls of the maze and their order.
Use your program to follow the AR markers in the order in which they are in the maze to navigate from start to finish.

