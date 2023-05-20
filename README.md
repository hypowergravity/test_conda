---
title: Making a test conda package
author: Sriram Srinivasa Raghavan
date: May 2023
---

# Test Conda package

This is a repository for creating a test conda package. The package, named 'my_package', simply prints the installed version of cctbx as a command-line argument.

# Creating a conda environment

```bash
conda create -n test_conda
conda activate test_conda
```

In order to remove the environment, do the following:

```bash
conda env remove --name test_conda
```

# Building the conda package.

Go to the folder containing the source code and meta.yaml and setup.py folder which is placed as shown:

Example

    .
    ├── my_package
    │   ├── build.bat
    │   ├── build.sh
    │   ├── meta.yaml
    │   ├── my_package
    │   │   ├── __init__.py
    │   │   └── main.py
    │   └── setup.py
    └── readme.md

Now, build the conda recipe in the test_conda channel within the parent directory "my_package" containing meta.yaml and setup.py files.

```bash
conda build .
```

After the build is complete,
It will show the path of the my_package in the build directory of conda. 
For example, "/Users/sriram/opt/anaconda3/conda-bld/osx-64/my_package-0.1-py38_0.tar.bz2".

The next step is that it can either be uploaded to anaconda user base or installed locally.

To locally install the package:

```bash
conda install --use-local my_package
```

In order to upload, anaconda has to be configured using the command, and then, anaconda client has to be installed.

```bash
conda install anaconda-client conda-build
```

It has to be rebuilt.

```bash
conda config --set anaconda_upload no
conda build .
conda build . --output
```

Now, use anaconda to login using user credentials and upload the package.

```bash
anaconda login
anaconda upload /Users/sriram/opt/anaconda3/conda-bld/osx-64/my_package-0.1-py38_0.tar.bz2
```

Finally,this package can be installed using conda command.

It can be installed in a new environment if there is conflict of same versions, if using the same system.

```bash
 conda install -c hypowergravity my_package
```
