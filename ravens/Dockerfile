# Based on https://github.com/geyang/jaynes-starter-kit/blob/master/docker/pytorch/Dockerfile
FROM nvidia/cudagl:11.4.0-devel-ubuntu20.04

ENV PIP_NO_CACHE_DIR=1
RUN apt update
RUN yes | apt install \
    tree \
    zsh  \
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

RUN yes | apt install libcgal-qt5-dev
RUN pip install --upgrade pip
RUN pip install pytest pytest-forked lz4 pyyaml
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install datasets einops sklearn torchinfo tqdm

# install GLX-Gears (for debugging)
RUN apt-get update && apt-get install -y --no-install-recommends \
   mesa-utils \
   python3-setuptools \
   && rm -rf /var/lib/apt/lists/*


RUN pip install \
   tdqm \
   wandb \
   kornia \
   ffmpeg \
   imageio-ffmpeg

RUN git clone https://github.com/google-research/ravens.git
RUN cd ravens && pip install -e .
# RUN pip install git+https://github.com/google-research/ravens.git

# Always install geyang products at last
RUN pip install jaynes ml-logger waterbear params-proto functional-notations