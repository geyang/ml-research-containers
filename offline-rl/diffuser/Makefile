DOCKER_BUILDKIT=1

default: build release
build:
	docker build --progress=plain -t diffuser .
run:
	docker run diffuser
test:
	# docker run -i --rm -w /test-script/ diffuser bash -c "python test.py"
	docker run -it --rm \
            --env="XAUTHORITY=${XAUTH}" \
            --volume="${XAUTH}:${XAUTH}" \
            --volume="$(PWD):/test_scripts" \
            --net=host \
            --workdir="/test_scripts" \
            diffuser /bin/bash -c "python /test_scripts/test.py"
            #diffuser python /test_scripts/test.py
release:
	docker tag diffuser episodeyang/diffuser
	docker push episodeyang/diffuser

