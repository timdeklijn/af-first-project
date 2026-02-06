build:
	docker build . -t first_project:dev

run: build
	docker run --rm first_project:dev "ingest"
