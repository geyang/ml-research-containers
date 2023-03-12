# syntax=docker/dockerfile:1.3-labs
FROM nvcr.io/nvidia/pytorch:21.09-py3
ENV DEBIAN_FRONTEND=noninteractive

# dependencies for gym
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
 libxcursor-dev \
 libxrandr-dev \
 libxinerama-dev \
 libxi-dev \
 mesa-common-dev \
 zip \
 unzip \
 make \
 gcc-8 \
 g++-8 \
 vulkan-utils \
 mesa-vulkan-drivers \
 pigz \
 git \
 libegl1 \
 git-lfs

# Force gcc 8 to avoid CUDA 10 build issues on newer base OS
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8

# WAR for eglReleaseThread shutdown crash in libEGL_mesa.so.0 (ensure it's never detected/loaded)
# Can't remove package libegl-mesa0 directly (because of libegl1 which we need)
RUN rm /usr/lib/x86_64-linux-gnu/libEGL_mesa.so.0 /usr/lib/x86_64-linux-gnu/libEGL_mesa.so.0.0.0 /usr/share/glvnd/egl_vendor.d/50_mesa.json

COPY nvidia_icd.json /usr/share/vulkan/icd.d/nvidia_icd.json
COPY 10_nvidia.json /usr/share/glvnd/egl_vendor.d/10_nvidia.json

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
 x11-apps

# pip
RUN pip install -U pip
ENV PIP_NO_CACHE_DIR=1

COPY ./third_party/IsaacGym_Preview_4_Package.tar.gz /opt/

ENV PATH="/root/.local/bin:$PATH"
RUN cd /opt && tar -xvzf IsaacGym_Preview_4_Package.tar.gz
RUN rm /opt/IsaacGym_Preview_4_Package.tar.gz
RUN cd /opt/isaacgym/python && pip install -e .

ENV NVIDIA_VISIBLE_DEVICES=all NVIDIA_DRIVER_CAPABILITIES=all

## install packages that are easier to install via conda
RUN conda install pycurl pandas
RUN pip install opencv-python

RUN pip install gym==0.19.0
RUN pip install gym3

RUN pip install scikit-build
RUN pip install kornia
RUN pip install filelock

RUN pip install jaynes ml_logger waterbear params-proto functional-notations cmx

## run once to build ninja
RUN <<EOF
python -c "
from isaacgym import gymapi
from isaacgym import gymutil
from isaacgym import gymtorch

import torch
print('finished build')
"
EOF
