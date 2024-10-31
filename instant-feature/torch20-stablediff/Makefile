default: build release
build:
	docker build --progress plain -t pytorch20-stablediffusion .
run:
	docker run pytorch20-stablediffusion
release:
	docker tag pytorch20-stablediffusion episodeyang/pytorch20-stablediffusion:"`date "+%F"`"
	docker tag pytorch20-stablediffusion episodeyang/pytorch20-stablediffusion:latest
	docker push episodeyang/pytorch20-stablediffusion:"`date "+%F"`"
	docker push episodeyang/pytorch20-stablediffusion:latest
