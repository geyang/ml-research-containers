# Docker Image

This folder contains the docker image for these custom environments. To re-build the docker image, rum

```bash
make build
```

And to release this image to docker hub, so that our ec2 instances can read from it, run

```bash
make release
```

## ToDos

you need to fill in the [./Dockerfile](Dockerfile),  make build and make release script.



Content of the Makefile:

```makefile
#! Makefile
default: build release
build:
	docker build --progress plain -t pytorch20-stablediffusion .
run:
	docker run pytorch20-stablediffusion
release:
	docker tag pytorch20-stablediffusion episodeyang/pytorch20-stablediffusion:"`date "+%F"`"
	docker tag pytorch20-stablediffusion episodeyang/pytorch20-stablediffusion:latest
	docker push episodeyang/pytorch20-stablediffusion:"`date "+%F"`"
	docker push episodeyang/pytorch20-stablediffusion:latest
```

