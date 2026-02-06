build:
	docker build . -t first_project:dev

run: build
	docker run --rm first_project:dev "calc-it" "--num" "2" "--fac" "10"
