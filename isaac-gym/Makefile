default: build release
build:
	echo "requires the docker buildkit"
	DOCKER_BUILDKIT=1 docker build --progress=plain -t gait-conditioned .
clean-build: 
	docker build -t gait-conditioned . --no-cache=true
release:
	docker tag gait-conditioned episodeyang/gait-conditioned
	docker push episodeyang/gait-conditioned
test:
	echo "add docker cmd including mount"
