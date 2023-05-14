# A Dockerfile that sets up a full Gym install with test dependencies
FROM episodeyang/instant-feature-t20

RUN python <<EOF
from torchvision import datasets

dataset = datasets.MNIST(root="/tmp/datasets", train=True, download=True)
print('finished downloading MNIST')

dataset = datasets.CIFAR10(root="/tmp/datasets", train=True, download=True)
print('finished downloading CIFAR10')
EOF

RUN pip install jaynes ml_logger waterbear params-proto functional_notations cloudpickle==1.3.0
