# aer1217-lab3
Georeferencing 


Tasks:
  1. ROS Structure - Charlie
    - read .bag file
    - publish vicon data at desired frequency
    - publish camera at desired frequency
    - Create a node to listen to the camera feed
      - For each camera frame, pull the associated vicon reading
    - Call image processing class
    - Call localization/clustering and outlier rejection
    
  2. Image processing - Amr
    - Python class
    - Input: Camera frame,
    - Output: Array of 'green' pixels [pixel values]
   
  3. Localization/clustering/outlier rejection - Demi
    - Python class
    - Input: Pixel values from image processing, vicon location/orientation
    - Output: Current best estimates for 6 landmarks (2x6 array)
