## Installation Instructions

### MySQL

To install and run MySQL on a Docker container, follow the instructions that were previously given.

### PyMySQL

``` bash
pip install PyMySQL
```

## Boilerplate

We have provided a boilerplate piece of code just to get you started. The only reason this boiler plate is being shared is to show you what an acceptable UI looks like. You can decide to not use the boilerplate if you feel that you have already implemented a similar flow for your application.

### To Run

To run the boilerplate code, you will need to login with your MySQL username and password (the boilerplate code has the username, password, and port hardcoded to work with the Docker installation instructions).

``` bash
python3 boilerPlate.py
```

This will prompt for you to enter your username and password.

### UI Interface

The commands run as specified in the Requirements document. The tutorial on how to run it is shown in the video attached.

### Error Handling

``` python
try:
    do_stuff()
except Exception as e:
    print (e)
```

## Creating Dump File For MySQL

The database dump file can be created using

``` bash
mysqldump -u username -p databasename > filename.sql
```