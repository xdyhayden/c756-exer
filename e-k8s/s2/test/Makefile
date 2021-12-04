# Makefile for test of Music service (S2)

VER=v0.8

SERVER=`docker inspect s2 --format '{{.NetworkSettings.IPAddress}}'`

build-music_test:
	docker image build -f Dockerfile -t music_test:$(VER) .

run-music_test:
	docker container run -it --rm --name music_test music_test:$(VER) python3 music_test.py $(SERVER) 30001
