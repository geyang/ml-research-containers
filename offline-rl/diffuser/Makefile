.PHONY: build
# shell option to use extended glob from from https://stackoverflow.com/a/6922447/1560241
SHELL:=/bin/bash -O extglob

VERSION=`< VERSION`

DOCKER_BUILDKIT=1

default: build release
build:
	docker build --progress=plain -t diffuser .
run:
	docker run diffuser
test:
	docker run -it --rm \
            --env="XAUTHORITY=${XAUTH}" \
            --volume="${XAUTH}:${XAUTH}" \
            --volume="$(PWD):/test_scripts" \
            --net=host \
            --workdir="/test_scripts" \
            diffuser python /test_scripts/test.py
release:
	docker tag diffuser episodeyang/diffuser:v$(VERSION)
	docker push episodeyang/diffuser:v$(VERSION)
