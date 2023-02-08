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
  
#### Move to the project folder: ####

  ```
  cd zmrn_parser_task
  ```
#### Inside the finnhub_parser folder create .env file ####

#### Copy the inside of .env_example file and paste it inside .env ####

#### Build the docker containers: ####

  ```
  docker-compose build
  ```
#### Start the Docker containers: ####

  ```
  docker-compose up -d --build 
  ```
#### Access the django server at: ####

  ```
  http://0.0.0.0:8000/
  ```
#### How to stop the Docker containers: ####

  ```
  docker-compose down -v
  ```
&mdash; Redis is used as the message broker for Celery to handle asynchronous tasks. 

&mdash; The project uses PostgreSQL as the database management system and runs in a separate Docker container. 

&mdash; The parsing of each ticker will start at 0 minute of each hour. 

## Usage: ##

#### Now, that you started Docker containers, you can send request to http://0.0.0.0:8000/ ####
#### You can get all the available news for each ticker at an endpoint: #### 
  ```
  http://0.0.0.0:8000/news/stock/all
  ```
#### Also, you can get all the news for specific ticker, for example Amazon: ####
  ```
  http://0.0.0.0:8000/news/stock/AMZN
  ```
#### If you want to get news about Amazon between specific dates, you should add two parameters to the url: "date_from" and "date_to" ####
  ```
  http://0.0.0.0:8000/news/stock/AMZN?date_from=2023-01-09&date_to=2023-02-01
  ```

#### The list of available tickers is inside the .env_example file ####
