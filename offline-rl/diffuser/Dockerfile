FROM nvidia/cuda:11.1.1-runtime-ubuntu18.04
ENV LANG=C.UTF-8

RUN apt-get -y update && apt-get install -y git vim tree curl wget unzip xvfb patchelf ffmpeg cmake swig
RUN apt-get install -y libssl-dev libcurl4-openssl-dev  # Needed for pyCurl
RUN apt-get install -y libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev
RUN apt-get install -y cmake libopenmpi-dev python3-dev zlib1g-dev
RUN apt-get install -y qtbase5-dev
RUN apt-get install -y qtdeclarative5-dev
RUN apt-get install -y libglib2.0-0


RUN mkdir /root/.mujoco && \
    cd /root/.mujoco && \
    wget https://www.roboti.us/download/mujoco200_linux.zip && \
    unzip ./mujoco200_linux.zip
RUN wget https://www.roboti.us/file/mjkey.txt -P /root/.mujoco/

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/root/.mujoco/mujoco200_linux/bin
ENV MUJOCO_PY_MUJOCO_PATH /root/.mujoco/mujoco200_linux
ENV MUJOCO_PY_MJKEY_PATH /root/.mujoco/mjkey.txt
ENV MJLIB_PATH /root/.mujoco/mujoco200_linux/bin/libmujoco200.so
ENV MJKEY_PATH ${MUJOCO_PY_MJKEY_PATH}

RUN apt-get install -y libssl-dev libcurl4-openssl-dev
RUN apt-get update && apt-get install -y python3.8-dev python3-pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN ln -s /usr/bin/python3.8 /usr/bin/python
RUN python -m pip install --upgrade pip

ENV PIP_NO_CACHE_DIR=off

RUN pip install pytest pytest-forked lz4 pyyaml qt5-py
RUN pip install google-cloud-storage

RUN pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install matplotlib==3.3.4 scikit-image==0.17.2 scikit-video==1.1.11 gitpython einops pillow tqdm pandas wandb
RUN pip install ray==1.9.1 crcmod
RUN pip install jax==0.2.21 flax==0.3.5
RUN pip install typed-argument-parser

#RUN apt-get install software-properties-common
RUN apt-get install -y libgl1-mesa-glx libosmesa6
RUN apt-get install -y libglew-dev

ENV MUJOCO_GL egl
#ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libGLEW.so
#:/usr/lib/x86_64-linux-gnu/libGL.so.1

RUN pip install mujoco-py==2.0.2.13
RUN pip install git+https://github.com/deepmind/dm_control@41d0c7383153f9ca6c12f8e865ef5e73a98759bd#egg=dm_control
RUN pip install git+https://github.com/JannerM/d4rl.git@13fc08c198d17ac627f528aedc70843e8f86bb71 --no-deps

RUN pip install h5py git+https://github.com/aravindr93/mjrl@master#egg=mjrl pybullet termcolor click

RUN pip install gym==0.18.0

RUN pip install jaynes ml_logger waterbear params-proto functional-notations --no-cache-dir
