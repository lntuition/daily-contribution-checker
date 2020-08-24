IMAGE="contribution-markdown-report"

build:
	docker build -t ${IMAGE} .
clean:
	docker rmi -f ${IMAGE}
debug: build
	docker run -it --entrypoint '' ${IMAGE} bash
