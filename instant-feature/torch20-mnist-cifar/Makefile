default: build release
build:
	docker build --progress plain -t pytorch20-mnist-cifar .
run:
	docker run pytorch20-mnist-cifar
release:
	docker tag pytorch20-mnist-cifar episodeyang/pytorch20-mnist-cifar:"`date "+%F"`"
	docker tag pytorch20-mnist-cifar episodeyang/pytorch20-mnist-cifar:latest
	docker push episodeyang/pytorch20-mnist-cifar:"`date "+%F"`"
	docker push episodeyang/pytorch20-mnist-cifar:latest
