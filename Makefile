build:
	docker build . -t first_project
	docker run --rm first_project "ingest"
