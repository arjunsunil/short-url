# Implement URL shortner Using Django Rest framework

## Introduction

The goal of the project is to implement an HTTP API to support a URL shortner application. 


## To run the application

git clone https://github.com/arjunsunil/short-url-api.git


make sure that docker and python are installed on your system and correctly configured to run this application.

run `sudo docker-compose up --build` to rebuild and run the application

## API List
1. create/update/delete/list interviewer or candidate `http://127.0.0.1:8000/shorturl`


## To run the testcases

 Run - python manage.py test shorten_url/

## API Documentation

### swagger

`http://127.0.0.1:8000/swagger/`


### curl

#### Get the short url list
curl --location --request GET 'http://0.0.0.0:8000/shorturl/'


#### Get the spefic original url from pk
curl --location --request GET 'http://0.0.0.0:8000/shorturl/{pk}'

#### Get the spefic original url from short url
curl --location --request POST 'http://127.0.0.1:8000/get-original-url/' 
--form 'short_url="{short_url}"'



#### Create a short url
curl --location --request POST 'http://0.0.0.0:8000/shorturl/' 
--form 'url="{url}"'
