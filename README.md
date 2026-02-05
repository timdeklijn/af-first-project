# First Project

## Usage

``` bash
Usage: first [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  ingest  Ingest data into cronus-data

```

We use a commandline argument parser to be able to switch between differenct entrypoints inside the `first_project` package.

In the Dockerfile the `first` script is defined as entrypoint so the different tasks can call run the Dockerfile with different arguments. For example, to call the `ingest` command in a docker run do:

``` shell
docker run -t first_project
```
