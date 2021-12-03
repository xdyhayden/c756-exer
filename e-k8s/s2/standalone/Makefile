# Makefile for standalone Music service (S2)

VER=v0.25
HOST_DIR=$(HWD)/s2/standalone

build-s2:
	docker image build -f Dockerfile --build-arg EXERARG=$(VER) -t s2-standalone:$(VER) .

run-s2:
	docker container run -it --rm -p 30001:30001 -v $(HOST_DIR):/data --name s2 s2-standalone:$(VER)

# Run with different port and volume mappings to demonstrate container mappings
# HOWEVER, if the client is running from another container connecting to this over the bridge
# network, it will use port 30001.  The host port mapping (20000) only is visible to clients
# running in the host OS, while containers use the container mapping (30001).
run-s2-odd:
	docker container run -it --rm -p 20000:30001 -v $(HOST_DIR)/odd:/data --name s2-odd s2-standalone:$(VER)

# Build an entirely self-contained image of S2, including the music entries
build-s2-self:
	docker image build -f self-Dockerfile --build-arg EXERARG=$(VER) -t ghcr.io/tedkirkpatrick/s2-self-contained:$(VER) .
