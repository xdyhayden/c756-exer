# Makefile for standalone Music service (S2)

VER=v0.8

build-mcli:
	docker image build -f Dockerfile -t mcli:$(VER) .

run-mcli:
	docker container run -it --rm --name mcli mcli:$(VER) python3 mcli.py `docker inspect s2 --format '{{.NetworkSettings.IPAddress}}'` 30001
