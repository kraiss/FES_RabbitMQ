# Step 5: Clustering

### Create the RabbitMQ cluster

```
docker-compose exec rabbit1 bash
~# rabbitmqctl -n rabbit@rabbit1 stop_app
~# rabbitmqctl -n rabbit@rabbit1 join_cluster rabbit@rabbit2
~# rabbitmqctl -n rabbit@rabbit1 start_app
```

#### Monitor the cluster

 * Try to shutdown/restart your rabbit nodes and see how the monitoring react
    * Stop the first node ```docker-compose stop rabbit1```
    * Start the first node ```docker-compose start rabbit1```

#### PAUSE: Dead ends and pitfalls with HA mode

[<- Previous](/step4_advanced/README.md) 