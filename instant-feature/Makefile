default: build release
build:
	docker build --progress plain -t instant-feature .
run:
	docker run instant-feature
release:
	docker tag instant-feature episodeyang/instant-feature:"`date "+%F"`"
	docker tag instant-feature episodeyang/instant-feature:latest
	docker push episodeyang/instant-feature:"`date "+%F"`"
	docker push episodeyang/instant-feature:latest
