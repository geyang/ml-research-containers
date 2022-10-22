FROM nvidia/cuda:11.3.1-runtime-ubuntu20.04
ENV LANG=C.UTF-8

RUN apt update && apt install -y tzdata

RUN apt-get update && apt-get install -y git vim tree curl unzip xvfb patchelf ffmpeg cmake swig wget
RUN apt-get update && apt-get install -y libssl-dev libcurl4-openssl-dev  # Needed for pyCurl
RUN apt-get update && apt-get install -y \
    libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev \
    cmake libopenmpi-dev python3-dev zlib1g-dev \
    qtbase5-dev qtdeclarative5-dev libglib2.0-0

# Download mujoco
RUN mkdir /root/.mujoco && \
    cd /root/.mujoco  && \
    curl -O http://www.roboti.us/download/mujoco200_linux.zip  && \
    unzip mujoco200_linux.zip
RUN wget http://roboti.us/file/mjkey.txt -P /root/.mujoco/

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/root/.mujoco/mujoco200_linux/bin
ENV MUJOCO_PY_MUJOCO_PATH /root/.mujoco/mujoco200_linux
ENV MUJOCO_PY_MJKEY_PATH /root/.mujoco/mjkey.txt
ENV MJLIB_PATH /root/.mujoco/mujoco200_linux/bin/libmujoco200.so
ENV MJKEY_PATH ${MUJOCO_PY_MJKEY_PATH}

RUN apt-get update && apt-get install -y python3.8-dev python3-pip
# RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN ln -s /usr/bin/python3.8 /usr/bin/python 
RUN python -m pip install --upgrade pip

ENV PIP_NO_CACHE_DIR=off

RUN pip install pytest pytest-forked lz4 pyyaml qt5-py
RUN pip install gym3
RUN pip install --pre torch torchvision torchaudio -f https://download.pytorch.org/whl/nightly/cu113/torch_nightly.html
RUN pip install kornia opencv-python
# RUN pip install tensorflow tensorboard
# RUN git clone https://github.com/openai/baselines.git
# RUN cd baselines && pip install -e .
RUN pip install filelock

#RUN apt-get install software-properties-common
RUN apt-get update && apt-get install -y libgl1-mesa-glx libosmesa6
RUN apt-get update && apt-get install -y libglew-dev
# Latest commit assumes mujoco v2.1, whereas we use mujoco v2.0
RUN pip install git+https://github.com/deepmind/dm_control.git@ff8a9caac9d845c1e1f669c272294b3355d6d855
RUN pip install gym-dmc
# used for egl rendering
ENV MUJOCO_GL egl
#ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libGLEW.so
#:/usr/lib/x86_64-linux-gnu/libGL.so.1


# Lacking dependencies
RUN pip install pandas scikit-image  # ml-logger dependency
# RUN pip install 'git+http://github.com/geyang/gym-distracting-control.git@ae4ab85599e084849397f6c7731c632f1c130e12#egg=distracting_control'
RUN pip install -I gym==0.19.0
RUN pip install xmltodict  # Nick Hansen's generalization-benchmark env dependency