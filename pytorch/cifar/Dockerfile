# syntax=docker/dockerfile:1.3-labs
FROM episodeyang/pytorch
ENV DATASETS=/tmp/datasets

RUN python <<EOF
from torchvision import datasets

dataset = datasets.CIFAR10(root="/tmp/datasets", train=True, download=True)
print('finished download')
EOF