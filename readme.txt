# ----------- How to run the package -------------

1. Add "<path>/aer1217-lab3/src" to $ROS_PACKAGE_PATH
2. Put the bag file, "lab3.bag" in "<path>/aer1217-lab3/src/publisher/"
3. Run "roslaunch <path>/aer1217-lab3/src/publisher/launch/publisher.launch"


# -------------- Code Structure ----------------

1. Publisher (intended to be removable when data is being provided by the vicon simulator)
  - publisher.launch
    File to be launched to run the simulation
    Launches processor.launch
  - package.xml
  - publisher.py
    Initializes node
    Plays the .bag file
    Handles exceptions and shuts down publisher node

2. Processor 
  - procesor.launch
  - package.xml
    Requires publisher node to be active
  - processor.py
    Initializes node
    Subscribes to image and position feed
    Filters certain frames
    Calls target_identifier.py on quality frames
    Calls localization.py on target_identifier.py results
    Calls cluster.py to determine the final target guesses
  
  - target_identifier.py
    Given araw image, undistort the image, identify pixel coordinates of targets. 
    Input: raw image
    Output: list of pixel coordinates of targets
      
  - localization.py
    Transform the pixel coordinates of undistorted image to points location in the global reference frame (vicon frame)
    Input: list of pixel coordinates
    Output: list of locations of targets
    
  - cluster.py
    Cluster points based on their relative distance and find the clusters with sufficient number of points
    Input: list of locations of targets
    Output: estimated locations of ground targets
