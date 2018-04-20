# Step 2: Basics

In this step we will see how consumers behave and compete

### Consumers

 * It's time! Let's rewrite your consumer as a true consumer
 * Run at least two different consumers
 * Then publish messages to the queue
    * What is happening ?

### PAUSE: What is happening ?

### Durability and message persistence

**Durability:**
 * Create a durable queue
 * Send a message to the queue
 * Restart the cluster (for Windows user, use the Services panel)
 * What happened ?
 
**Persistence**
 * Keep your durable queue
 * Send a **persistent** message to the queue using publish properties
 * Restart the cluster
 * What changed ?

### PAUSE: Exchanges

### Fanout Exchange

 * Declare a fanout exchange and two queues bind to the exchange
 * Publish **to the exchange** instead of the queue
    * What is happening ?

[<- Previous](/step1_hello_world/README.md) ::  :: [Next ->](/step3_routing/README.md)