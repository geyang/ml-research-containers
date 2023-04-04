# A Dockerfile that sets up a full Gym install with test dependencies
FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y \
    git \
    cmake \
    build-essential \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-system-dev \
    libboost-test-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libmetis-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev
RUN apt -y install libcgal-qt5-dev

RUN apt -y install libatlas-base-dev libsuitesparse-dev
RUN apt -y install colmap

RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.8 python3.8-dev python3.8-distutils
RUN apt-get install -y python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install --upgrade pip

ENV PIP_NO_CACHE_DIR=1
RUN pip install pytest pytest-forked lz4 pyyaml

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

ARG CUDA_ARCHITECTURES=90;89;86;80;75;70;61;52;37

RUN git clone --recursive https://github.com/nvlabs/tiny-cuda-nn
RUN cd tiny-cuda-nn && \
    export TCNN_CUDA_ARCHITECTURES=${CUDA_ARCHITECTURES} && \
    cmake . -B build && \
    cmake --build build --config RelWithDebInfo -j && \
    cd bindings/torch && \
    python setup.py install

RUN pip install aiohttp==3.8.1 aiortc==1.3.2 appdirs>=1.4 av==9.2.0 cmx cryptography==38.0.4 einops ftfy functorch==0.2.1
RUN pip install gdown==4.6.0 h5py>=2.9.0 imageio==2.21.1 ipywidgets>=7.6 ninja==1.10.2.3
RUN pip install msgpack==1.0.4 msgpack_numpy==0.4.8 nerfacc==0.2.1 open3d>=0.16.0 protobuf==3.20.0
RUN pip install python-socketio==5.7.1 regex requests rich==12.5.1 scikit-image==0.19.3 torchmetrics[image]>=0.9.3
RUN pip install torchtyping>=0.1.4 tyro>=0.3.31 u-msgpack-python>=2.4.1 nuscenes-devkit>=1.1.1 xatlas

RUN apt install -y libcurl4-openssl-dev libssl-dev
RUN pip install pycurl
RUN pip install jaynes ml_logger waterbear params-proto functional_notations cloudpickle==1.3.0

# needed for dpvo
RUN pip install yacs lietorch torch_scatter

#RUN pip uninstall torch torchvision
#RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117