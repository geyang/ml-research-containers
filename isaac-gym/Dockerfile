# syntax=docker/dockerfile:experimental
FROM nvidia/cuda:11.7.0-devel-ubuntu22.04

# install package
ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN pip install -U pip
ENV PIP_NO_CACHE_DIR=1

# make sure python is 3.8 by default `python`
COPY ./third_party/IsaacGym_Preview_4_Package.tar.gz /home/$USERNAME/
RUN cd $HOME && tar -xvzf IsaacGym_Preview_4_Package.tar.gz
RUN rm $HOME/IsaacGym_Preview_4_Package.tar.gz
RUN cd /home/$USERNAME/isaacgym/python && pip3 install -e .

RUN pip install conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia --no-cache
RUN conda install -y opencv-python

#RUN apt-get -y update && apt-get install -y git vim tree curl unzip xvfb patchelf ffmpeg cmake swig
#RUN apt-get install -y libssl-dev libcurl4-openssl-dev  # Needed for pyCurl
#RUN apt-get install -y libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev
#RUN apt-get install -y cmake libopenmpi-dev python3-dev zlib1g-dev
#RUN apt-get install -y qtbase5-dev
#RUN apt-get install -y qtdeclarative5-dev
#RUN apt-get install -y libglib2.0-0
#RUN apt-get install -y tcl-dev tk-dev

#RUN pip install tensorboard
#RUN pip install cycler python-dateutil kiwisolver pyparsing matplotlib

RUN pip install gym==0.19.0
#RUN pip install pytest pytest-forked lz4 pyyaml qt5-py
RUN pip install gym3

#RUN pip install scikit-build
#RUN pip install kornia opencv-python
#RUN pip install filelock
#
## RUN apt-get install -y software-properties-common
#RUN apt-get install -y libgl1-mesa-glx libosmesa6
#RUN apt-get install -y libglew-dev
## used for egl rendering
#ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libGLEW.so
#:/usr/lib/x86_64-linux-gnu/libGL.so.1

#RUN conda install pycurl pandas
RUN pip install pycurl pandas opencv-python
RUN pip install jaynes ml_logger waterbear params-proto functional-notations cmx


RUN pip install lcm
RUN apt-get install htop

RUN pip install scikit-image
RUN apt-get install -y python3-tk

# LCM
#RUN cd /home/$USERNAME && git clone https://github.com/lcm-proj/lcm.git && cd lcm && mkdir build && cd build && cmake .. && make -j && make install
#RUN apt-get install -y net-tools && pip install netifaces