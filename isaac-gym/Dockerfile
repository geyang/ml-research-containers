# syntax=docker/dockerfile:experimental
FROM nvidia/cuda:11.7.0-devel-ubuntu22.04

# install package
ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get clean && apt-get update -y -qq
RUN apt-get install -y build-essential git vim tree curl unzip xvfb patchelf ffmpeg cmake swig

RUN apt-get install -y software-properties-common
RUN apt-get install -y libgl1-mesa-glx libosmesa6
RUN apt-get install -y libglew-dev
## used for egl rendering
#ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libGLEW.so
#:/usr/lib/x86_64-linux-gnu/libGL.so.1

# install conda

ENV PATH="/root/anaconda3/bin:${PATH}"

RUN curl --silent -O https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh \
    && bash Miniconda3-py38_23.1.0-1-Linux-x86_64.sh -b -p /root/anaconda3

RUN conda update -n base -c defaults conda

# install packages that are easier to install via conda
RUN conda install pycurl pandas
RUN conda install -c conda-forge libopencv opencv py-opencv


# pip
RUN pip install -U pip
ENV PIP_NO_CACHE_DIR=1

# install pytorch
# 1.13.1+cu117'
RUN pip install torch torchvision torchaudio --no-cache

ENV LD_LIBRARY_PATH="/root/anaconda3/lib:${LD_LIBRARY_PATH}"

COPY ./third_party/IsaacGym_Preview_4_Package.tar.gz /home/$USERNAME/
RUN cd /home/$USERNAME && tar -xvzf IsaacGym_Preview_4_Package.tar.gz
RUN rm /home/$USERNAME/IsaacGym_Preview_4_Package.tar.gz
RUN cd /home/$USERNAME/isaacgym/python && pip3 install -e .

RUN pip install gym==0.19.0
RUN pip install gym3

RUN pip install scikit-build
RUN pip install kornia
RUN pip install filelock

RUN pip install jaynes ml_logger waterbear params-proto functional-notations cmx
