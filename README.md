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

  todo: shut down after all data from rosbag are published
        compare timestamp of vicon and camera data, synchronize them? there are some freeze frame, leads to outlier
    
  2. Image processing - Amr
    - Python class
    - Input: Camera frame
    - undistortion
    - color based filter 
    - find contour and center of circle only
    - Output: Array of 'green' pixels [center pixel location]       ---list of np array ([x1,y1],[x2,y2]...)
  
  todo: test filter and center locator (need modified) with other images, 
        including image without target, with multiple targets, and with incomplete targets
   
  3. Localization/clustering/outlier rejection - Demi
    - Python class
    - Input: Pixel values from image processing, vicon location/orientation
    - Output: np array, location estimates of the image       ---append to the list of np array in processor.py    
  
  todo: clustering - kmeans
        outlier rejection in image processing? remove images with no target or multiple targets?
        
  Current Results:
  -1.46     -0.68
  -1.06     1.28
  0.338     -0.256
  1.452     -1.487
  0.630     0.858
  0.143     -1.528
  
  
  Results from whatsup:
    -1.1       0.876
    -1.0       -0.73
    -0.03      -1.874
    0.257      -0.259
    0.663       0.869
    2.212       -1.65

  Results from other group:
    -1.12       0.94
    -1.02       -0.7
    0.049      -1.92
    0.31      -0.25
    0.62       0.86
    1.43       -1.47
