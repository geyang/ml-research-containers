IM_NAME=episodeyang/orbslam3
# IM_TAG=1.0-ubuntu18.04
# You will need to apply the exact same name to container_name in orb-container/docker-compose.yml
CONT_NAME=orbslam3 


default: run
build:
	docker build --progress plain -t orbslam3 .
enter:
	clear && docker exec -it ${CONT_NAME} bash
down:
	docker-compose down
run:
	docker run orbslam3
release:
	docker tag orbslam3 episodeyang/orbslam3:"`date "+%F"`"
	docker tag orbslam3 episodeyang/orbslam3:latest
	docker push episodeyang/orbslam3:"`date "+%F"`"
	docker push episodeyang/orbslam3:latest


