default: build release
build:
	docker build --progress plain -t instant-feature-t20 .
run:
	docker run instant-feature-t20
release:
	docker tag instant-feature-t20 episodeyang/instant-feature-t20:"`date "+%F"`"
	docker tag instant-feature-t20 episodeyang/instant-feature-t20:latest
	docker push episodeyang/instant-feature-t20:"`date "+%F"`"
	docker push episodeyang/instant-feature-t20:latest
