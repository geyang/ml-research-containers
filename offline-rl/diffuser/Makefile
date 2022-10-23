DOCKER_BUILDKIT=1

default: build release
build:
	sudo docker build --progress=plain -t diffuser .
run:
	docker run diffuser
test:
	docker run -i --rm -w /test-script/ diffuser bash -c "python test.py"
release:
	docker tag diffuser episodeyang/diffuser
	docker push episodeyang/diffuser
