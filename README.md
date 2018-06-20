# RabbitMQ Training Guide

This repository contains training material for RabbitMQ most part inspired by [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html)

If you were not part of this training, I advise you to use [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html) instead.

## Step 0: Set up RabbitMQ over Docker

1. Install Docker !!
2. Start RabbitMQ. 
  * Use the [docker-compose configuration](/docker-compose.yml) with the command : ```docker-compose up -d```  
  * Note: After the training, you can stop/clean everything with: ```docker-compose down```  
3. Test that everything works fine:
    * Open `http://localhost:15672/` in a browser, you should see the authentication page
    * Authenticate with `guest` / `guest` (It's RabbitMQ Management plugin default user/password)
    * In `Nodes`, you can see cluster state. If all is green, you are ready to go!  

## PAUSE: What are we running with docker?
    
## PAUSE: Tour of the Management UI

## Python FTW !!

For every following steps, code samples will be provided in Python.

If you want to run these samples, make sure Python installed and install [Pika](https://pypi.org/project/pika/) with [pip](https://packaging.python.org/tutorials/installing-packages/)

On Windows, you can use [Ubuntu Subsystem](https://www.omgubuntu.co.uk/2016/08/enable-bash-windows-10-anniversary-update)

```bash
# Install pip and pika on Ubuntu or Ubuntu Subsystem
sudo apt update
sudo apt install python3-pip
python -m pip install pika
```

Note: The code sample have been tested with Python 3.5 and pika 0.12

[Next ->](/step1_hello_world/README.md)