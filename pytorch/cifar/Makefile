DOCKER_BUILDKIT=1

default: build release
build:
	sudo docker build --progress=plain -t torch-cifar .
run:
	docker run torch-cifar
release:
	docker tag torch-cifar episodeyang/torch-cifar
	docker push episodeyang/torch-cifar
