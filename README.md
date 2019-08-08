# Grind App

Tool to walk through the directory and run various operations as defined below
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing
clone the project

```
git clone https://github.com/chakri408/TE
```

## Running the tests
Project has one executable file.  
*grind.py*  



### Help

grind.py help

```
$ python grind.py 
usage: grind.py [-h] [--d PATH] [--m MATCH] [--r RECURSIVE]

Usage:

optional arguments:
  -h, --help     show this help message and exit
  --d PATH       List files in directory. Eg: ./grind --d <path>
  --m MATCH      Search file in given directory at top level. Eg: ./grind --d
                 <path> --m foo
  --r RECURSIVE  Search file recursively in a given directory. Eg: ./grind --d
                 <directory> --r foo

Eg: ./grind
```

Following three supported actions implemented. However, it has large scope to add more.

**1. An operation to list all files in a given path.**

```
$ python grind.py --d "/tmp/example"
/tmp/example/foo
/tmp/example/bar
/a
/c
/b
```

**2. An operation to Search file in given directory .**

```
$ python grind.py --d "/tmp/example" --m foo
/tmp/example/foo
```

**3. An operation to Search file recursively in a given directory.**

```
$ python grind.py --d "/tmp/example" --r hello
/tmp/example/a/hello
```



