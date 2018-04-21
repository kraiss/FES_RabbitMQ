# RabbitMQ Training Guide

This repository contains training material for RabbitMQ most part inspired by [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html)

If you were not part of this training, I advise you to use [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html) instead.

## Step 0: Set up RabbitMQ

1. Install Erlang (RabbitMQ runs on Erlang): http://www.erlang.org/downloads
    * Note: Check that `ERLANG_HOME` is correctly define (example on Windows: `C:\Program Files (x86)\erl6.4`)
2. Install the server: https://www.rabbitmq.com/download.html
3. Install Management Plugin: https://www.rabbitmq.com/management.html
    * Note: On Windows you may have to go in RabbitMQ installation directory to run the installation command
4. Test that everything works fine:
    * Open `http://localhost:15672/` in a browser, you should see the authentication page
    * Authenticate with `guest` / `guest` (It's RabbitMQ Management plugin default user/password)
    * In `Nodes`, you can see cluster state. If all is green, you are ready to go!    
    
**When everyone will be ready, we will take a tour of the Management UI**

## Python FTW !!

For every following steps, code samples will be provided in Python.

If you want to run these samples, make sure Python installed and install [Pika](https://pypi.org/project/pika/) with [pip](https://packaging.python.org/tutorials/installing-packages/)

On Windows, you can use [Ubuntu Subsytem](https://www.omgubuntu.co.uk/2016/08/enable-bash-windows-10-anniversary-update)

```bash
# Install pip and pika on Ubuntu or Ubuntu Subsystem
sudo apt update
sudo apt install python-pip
pip install pika
```

Note: The code sample have been tested with Python 2.7 and pika 0.11.2

[Next ->](/step1_hello_world/README.md)