# Finnhub Company News Parser

This is a django project that parses news about Amazon, Meta, Tesla, Apple and Microsoft from finnhub.io

## Requirements: ##
- Docker
- Python 3.10 (If you want to run the project without Docker)

## Technologies used: ##
- Python
- Django Rest Framework
- Docker
- PostgreSQL

## Installation: ##
- If you are using Linux-based OS, open the terminal and paste this:

  ```
  git clone https://github.com/AldyKey/zmrn_parser_task.git
  ```
- If you are using Windows OS, download this repository and place it where you want to.
  
## Usage: ##
##### Move to the project folder: #####

  ```
  cd zmrn_parser_task
  ```
##### Build the docker containers: #####

  ```
  docker-compose build
  ```
##### Start the Docker containers: #####

  ```
  docker-compose up
  ```
##### Access the django server at: #####

  ```
  http://0.0.0.0:8000/
  ```
##### How to stop the Docker containers: #####

  ```
  docker-compose down
  ```
