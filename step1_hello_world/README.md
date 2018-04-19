# Step 1: Hello World

In this step we prepare a basic set up to publish and consume messages

### Declare the queue

 * Open a connection to the broker. By default: `host=localhost, port=5672, username=guest, password=guest`
 * From the connection open a channel
 * From the channel declare a queue `hello_world`
    * Every following operation (consume, publish...) will be done using the channel

### PAUSE: Understand connection, channels and declarations

### Publish and consume to the queue

 * Publish a `Hello world!` message to the queue
 * Consume the message from the queue
    * Try to use `basic_get`. We will use consumer later.
    
 _NOTE: Use the monitoring GUI to see it working live!_
    
### PAUSE: A bit more about publishing and consuming

[<- Previous](/README.md) :: [Next ->](/step2_basics/README.md)