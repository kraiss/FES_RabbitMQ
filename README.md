# RabbitMQ Training Guide

This repository contains training material for RabbitMQ most part inspired from [RabbitMQ tutorials](https://www.rabbitmq.com/getstarted.html)

If you were not part of this training, I advise you to use it instead.

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

[Next ->](/step1_hello_world/README.md)