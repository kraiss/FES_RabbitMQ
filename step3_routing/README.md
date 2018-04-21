# Step 3: Routing

### Direct Exchange

 * Create a direct exchange 
 * Create queues (at least 3) bind to the exchange with different routing key
    * Don't forget, you bind with queue_bind(..)
 * Try to publish different messages and see how it behaves
    * Some achievements:
        * Reach each queues it with distinct messages
        * Reach several queues with the same message
        * Reach the same queue with two distinct messages
        * Lose messages

### DEMO: Topic Exchange

### DEMO: Header Exchange

### PAUSE: Let's sum up what we just test

[<- Previous](/step2_basics/README.md) :: [Next ->](/step4_signals/README.md)