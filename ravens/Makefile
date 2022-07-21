HUB_USER=episodeyang

default: build release
build:
	docker build --progress plain -t ravens .
clean-build:
	docker build -t ravens . --no-cache=true
run:
	docker run model-free
release:
	docker tag model-free $(HUB_USER)/ravens
	docker push $(HUB_USER)/ravens
