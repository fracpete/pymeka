# pymeka

## Docker

### Build local image

* Build the image from Docker file (from within `docker/0.0.1`)

  ```bash
  docker build -t pymeka_cpu .
  ```
  
* Run the container

  ```bash
  docker run -v /local/dir:/container/dir -it pymeka_cpu
  ```
  `/local/dir:/container/dir` maps a local disk directory into a directory inside the container

## Pre-built images

* Build

  ```bash
  docker build -t pymeka:0.0.1 .
  ```
  
* Tag

  ```bash
  docker tag \
    pymeka:0.0.1 \
    fracpete/pymeka:0.0.1
  ```
  
* Push

  ```bash
  docker push fracpete/pymeka:0.0.1
  ```

### Special directories

* `/workspace/wekafiles` - the directory that `WEKA_HOME` is pointing to (packages, props files, etc) 


## Usage

### Basic

For using the image interactively, you can run the following command: 

```bash
docker run -u $(id -u):$(id -g) \
    -it fracpete/pymeka:0.0.1
```

**NB:** 

* Use `-v localdir:containerdir` to map directories from your host into the container.
* Use `--rm` to automatically remove the container when you are exiting it.

### With local packages

Instead of having to reinstall your packages each time you start up the container, 
you can map your local Weka packages into the container as follows: 

```bash
docker run -u $(id -u):$(id -g) \
    -v $HOME/wekafiles/:/workspace/wekafiles \
    -it fracpete/pymeka:0.0.1
```

**NB:** With this approach you can separate various package installations on your host system
in different directories.
