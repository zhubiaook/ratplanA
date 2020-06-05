if ! docker network inspect br-myblog &> /dev/null; then
	docker network create -d bridge br-myblog
fi
docker run --net br-myblog -d --name myblog slynxes/myblog:latest 
docker run --net br-myblog -d -v 80:80 --name nginx slynxes/nginx:latest
