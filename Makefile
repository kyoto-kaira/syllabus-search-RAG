NAME := syllabus-rag

build:
	docker build -t $(NAME) .

build-no-cache:
	docker build --no-cache -t $(NAME) .

run:
	docker run -it --rm -v $(PWD):/root/workspace --name $(NAME) $(NAME) bash

exec:
	docker exec -it $(NAME) bash

stop:
	docker stop $(NAME)

clean:
	docker rmi $(NAME)

.PHONY: build run exec stop clean
