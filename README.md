# Silent Eight Recruitment Task

#### Chua Wei En

## Introduction

The task is to write a short program that count the number of islands.

## Folder Structure

Below is the folder structure for this project.

    .                
    ├── data                    # Data files
        ├── test_data           # Data files for unit test
    ├── src                     # Source files 
        ├── __init__.py 
        ├── run.py              # Main script counting islands
        ├── validate.py         # validate inputs
    ├── test
        ├── __init__.py                
        ├── test.py             # Test script with different testcases
    ├── .dockerignore           # ignore contents in data folder
    ├── .gitignore              # git ignore data and system files
    ├── Dockerfile              # Dockerfile to build Docker image
    ├── README.md               # Documentation
    ├── run.sh                  # Shell script that takes in input filepath, else it will throw an error
    └── setup.py                # setup project to import packages

## Steps to Run

There are two ways to run the scripts: either in local machine or in a Docker container. Please follow either one of the options below.

### Option 1: Run scripts locally

In order to run the scripts in the local machine please do the following:

1. Create a virtual environment using either `conda` or `python`. But for this example, `conda` is used and the environment name is `s8`. Ensure that you are in the project root folder.

```
(base) conda create -n s8 python=3.8
```

2. Activate the environment

```
(base) conda activate s8
```

3. To ensure that the modules can be imported in the scripts, install the project packages by running the below command:

```
(s8) python setup.py install
```

4. Once it is done, run the following commands to make the shell script executable and to run the programme. Ideally, the input data should be in `data` folder. Otherwise, please state in `<input-filepath>` below.

```
(s8) sudo chmod +x ./run.sh
(s8) ./run.sh <input-filepath>
```

### Option 2: Run scripts in a Docker container

In order to run the scripts in a Docker container please do the following:

1. Build a docker image with the `Dockerfile` in the root project folder. Ensure that you are in the project root folder.

    Ideally, the input data should be in `data` folder. Otherwise, please state in `<input filepath>` below. The build argument `filepath` is a ENV variable that will be the input to `run.sh`.

```
(base) docker build -t <image-name> -f Dockerfile . --platform linux/amd64 --build-arg filepath=<input-filepath>
```

2. To run the docker image, please use the following command.

    `-v` option will mount a volume from the local host to the Docker container, so the input data can be accessed in the Docker container.

```
(base) docker run -v <host-data-filepath>:<input-filepath> <image-name>
```

If there is no `<input-filepath>` or the file is not found, there will be error because the script was not succesfully executed. Once the scripts are successfully executed, you should see the output number of islands and the message `"Island Counting script execution was successful."`

## Unit Tests

You can find the test cases in `test/testcases.py`. The following testcases are considered:

- `validate` function is working
- `count_islands` function is working
- Edge cases:
  - grid contains a single island made up of a single 1.
  - grid contains only 0's.
  - grid is very large, with a large number of 1's and 0's
  - grid is very sparse, with a small number of 1's and a large number of 0's.
  - grid contains an island where some cells inside the island are 0's
  - grid contains an island where the cells are not all connected but there is a bridge that connects cells that are not next to each other
  
Test data for large grids can be found in `data/test_data`.

### Steps to run Unit Tests

To run the unit tests locally, ensure that you are in the project root folder and run the following command:

```
python -m unittest test.testcases
```
