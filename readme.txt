# ----------- How to run the package -------------

1. Add "<path>/aer1217-lab3/src" to $ROS_PACKAGE_PATH
2. Put the bag file, "lab3.bag" in "<path>/aer1217-lab3/src/publisher/"
3. Run "roslaunch <path>/aer1217-lab3/src/publisher/launch/publisher.launch"

# -------------- Code Structure ----------------

1. Publisher
  - publisher.py

2. Processor 
  - processor.py
  
  
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
