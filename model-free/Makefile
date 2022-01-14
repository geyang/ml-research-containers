HUB_USER=episodeyang

default: build release
build:
	docker build -t model-free .
clean-build:
	docker build -t model-free . --no-cache=true
run:
	docker run model-free
release:
	docker tag model-free $HUB_USER/model-free
	docker push $HUB_USER/model-free
