default: build release
build:
	echo "requires the docker buildkit"
	DOCKER_BUILDKIT=1 docker build --progress=plain -t isaacgym .
clean-build:
	docker build -t isaacgym . --no-cache=true
release:
	docker tag isaacgym episodeyang/isaacgym:"`date "+%F"`"
	docker tag isaacgym episodeyang/isaacgym:latest
	docker push episodeyang/isaacgym:"`date "+%F"`"
	docker push episodeyang/isaacgym:latest
test:
	echo "add docker cmd including mount"
