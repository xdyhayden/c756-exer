# Makefile for standalone Music service (S2)

VER=v0.25

build-s2:
	docker image build -f Dockerfile --build-arg EXERARG=$(VER) -t s2-standalone:$(VER) .

run-s2:
	docker container run -it --rm -p 30001:30001 -v $(PWD):/data --name s2 s2-standalone:$(VER)

# Run with different port and volume mappings to demonstrate container mappings
run-s2-odd:
	docker container run -it --rm -p 20000:30001 -v $(PWD)/odd:/data --name s2-odd s2-standalone:$(VER)

# Build an entirely self-contained image of S2, including the music entries
build-s2-self:
	docker image build -f self-Dockerfile --build-arg EXERARG=$(VER) -t ghcr.io/tedkirkpatrick/s2-self-contained:$(VER) .
