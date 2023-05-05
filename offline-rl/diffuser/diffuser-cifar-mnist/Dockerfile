# syntax=docker/dockerfile:1.3-labs
FROM episodeyang/pytorch
ENV DATASETS=/tmp/datasets

RUN python <<EOF
from torchvision import datasets

dataset = datasets.MNIST(root="/tmp/datasets", train=True, download=True)
print('finished downloading MNIST')

dataset = datasets.CIFAR10(root="/tmp/datasets", train=True, download=True)
print('finished downloading CIFAR10')
EOF

RUN pip install -U ml-logger params-proto cmx
