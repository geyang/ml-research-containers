default: build release
build:
	docker build --progress plain -t pytorch20-mnist-cifar .
run:
	docker run instant-feature-t20
release:
	docker tag instant-feature-t20 episodeyang/pytorch20-mnist-cifar:"`date "+%F"`"
	docker tag instant-feature-t20 episodeyang/pytorch20-mnist-cifar:latest
	docker push episodeyang/pytorch20-mnist-cifar:"`date "+%F"`"
	docker push episodeyang/pytorch20-mnist-cifar:latest
