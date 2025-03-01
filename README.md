# TB_ORB_SLAM3_ws_ver2

This project uses [jnskkmhr's ORB-SLAM3](https://github.com/jnskkmhr/orbslam3).

---

## Installation

### Clone this repository
```
git clone https://github.com/Gyeong-Rak/TB_ORB_SLAM3_ws_ver2.git
```

### Check following lines
src/orbslam3_ros2/CMakeLists.txt/Line5
src/orbslam3_ros2/CMakeModules/FindORB_SLAM3.cmake/Line8
src/orbslam3_ros2/launch/orb_slam3_ver2.launch.py/Line10,16

### Install dependencies
```
cd
sudo apt update
sudo apt install libepoxy-dev
sudo apt install ros-foxy-vision-opencv
export cv_bridge_DIR=/opt/ros/foxy/share/cv_bridge
```

```
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
export Pangolin_DIR=/usr/local/lib/cmake/Pangolin
```

<details> <summary>🛠 Fix 'Werror' Issues (Click to Expand)</summary>
sudo apt remove libopenexr-dev
sudo apt install libopenexr-dev openexr
cd ~/Pangolin
sed -i 's/-Werror//' CMakeLists.txt
sed -i 's/-Wno-deprecated-register//' CMakeLists.txt
sed -i 's/-Wno-null-pointer-subtraction//' CMakeLists.txt
sed -i 's/-Wno-null-pointer-arithmetic//' CMakeLists.txt
rm -rf build
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
</details>

```
cd ~/TB_ORB_SLAM3_ws_ver2
chmod +x AutoBuild.sh
./AutoBuild.sh
```

---

## Launch Camera
```
rosfoxy
ros2 launch zed_wrapper zed_camera.launch.py camera_model:=zed2i
```

## ORB-SLAM3
```
cd ~/TB_ORB_SLAM3_ws_ver2
rosfoxy
ros2 launch orbslam3 orb_slam3_ver2.launch.py
```
