# syntax=docker/dockerfile:experimental
#FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3
FROM nvcr.io/nvidia/l4t-pytorch:r35.1.0-pth1.13-py3

# Comment these out, since they will break pip install.
# ENV http_proxy="http://192.168.123.161:3128"
# ENV https_proxy="http://192.168.123.161:3128"
# ENV ftp_proxy="http://192.168.123.161:3128"

# install package
ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt update -y
RUN apt install -y --no-install-recommends \
        build-essential \
        vim \
        tree \
        curl \
        sudo \
        less \
        emacs \
        apt-utils \
        tzdata \
        git \
        tmux \
        bash-completion \
        command-not-found \
        libglib2.0-0 \
        liblcm-dev

# Install ROS
ENV ROS_DISTRO focal
RUN apt-get install -y gnupg
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list
RUN apt update -y
RUN apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential \
                   python3-catkin-tools python3-osrf-pycommon

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# bootstrap rosdep
RUN pip install rospkg wstool vcstools catkin_pkg rosdep
#RUN rm /etc/ros/rosdep/sources.list.d/20-default.list
RUN rosdep init
RUN rosdep update
RUN pip install --user git+https://github.com/catkin/catkin_tools.git

# turn off caching
ENV PIP_NO_CACHE_DIR=1

# Update PIP then turn off the caching.
RUN rm /usr/bin/pip
RUN rm /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip install -U pip
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update -y
RUN apt-get install -y freeglut3-dev libudev-dev libgl1-mesa-dev libudev1 libudev-dev libgtk2.0-dev pkg-config

## Install LCM
RUN apt-get -y update && apt-get install -y make gcc-8 g++-8
RUN cd /root &&  \
    git clone https://github.com/lcm-proj/lcm.git &&  \
    cd lcm && mkdir build && cd build &&  \
    cmake .. -DPython_INCLUDE_DIR=/usr/include/python3.8 -DPython_LIBRARY=/usr/lib -DLCM_ENABLE_JAVA=OFF -DLCM_ENABLE_LUA=OFF -DLCM_ENABLE_GO=OFF &&  \
    make -j && make install
RUN ls /root/lcm/lcm-python
RUN cd /root/lcm/lcm-python && pip install -e .

RUN apt-get install -y libcurl4-openssl-dev libssl-dev
RUN apt autoremove -y
RUN pip install pycurl pandas
RUN pip install ml-logger jaynes params-proto functional_notations cloudpickle==1.3.0

RUN apt clean
RUN rm -rf /var/lib/apt/lists/*
