# syntax=docker/dockerfile:1.3-labs
FROM episodeyang/diffuser:2023-05-09
ENV DATASETS=/tmp/datasets

RUN python <<EOF
from torchvision import datasets

dataset = datasets.MNIST(root="/tmp/datasets", train=True, download=True)
print('finished downloading MNIST')

dataset = datasets.CIFAR10(root="/tmp/datasets", train=True, download=True)
print('finished downloading CIFAR10')
EOF

RUN pip install ml-logger==0.10.15 params-proto cmx
