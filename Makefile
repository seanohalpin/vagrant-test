.PHONY: run

run:
	docker run -it --rm soha/server01

build: Dockerfile
	docker build -t soha/server01 -f ./Dockerfile .
