Design Document: PubSub System
Overview
The PubSub System is a system that consists of two components: the server and the client. The server component implements the Remote Procedure Call (RPC) library rpyc to maintain a list of clients and articles, expose methods for clients to join, leave, subscribe, unsubscribe, publish, and ping, and publish articles to clients who have subscribed to a specific type or organization. The client component implements a PubSubClient class that connects to the server using the rpyc library, allows the user to make requests, receives articles using a UDP socket, and starts a receive thread to listen for incoming articles.

Server Component
Implemented using the Remote Procedure Call (RPC) library rpyc
Maintains a list of clients and articles
Exposes methods to join, leave, subscribe, unsubscribe, publish, and ping
Publishes articles to clients that have subscribed to a specific type or organization
Uses ThreadedServer from rpyc to handle multiple client connections
Client Component
Implements a PubSubClient class
Connects to the server using the rpyc library
Allows the user to make requests such as join, subscribe, unsubscribe, publish, and leave
Receives articles using a UDP socket
Starts a receive thread to listen for incoming articles
Instructions
Server
Install the rpyc library using pip3 install rpyc
To start the server, run python3 server.py
Client
Install the rpyc library using pip3 install rpyc
To start the client, run python3 client.py
Follow the on-screen prompts to make requests to the server
Testing Description
The following test cases have been attempted:

Joining the server with different IP addresses and ports
A single client joins the server with a valid IP address and port. Expected Results: The client should receive a message indicating that they joined the server successfully.
A single client attempts to join the server with an invalid IP address and port. Expected Results: The client should receive a message indicating that they were unable to join the server.
Subscribing to articles of different types and organizations
A client subscribes to articles of type "ENTERTAINMENT". Expected Results: The client should receive a message indicating that they subscribed to articles of type "ENTERTAINMENT" successfully.
A client subscribes to articles from organization "CNN". Expected Results: The client should receive a message indicating that they subscribed to articles from organization "CNN" successfully.
Unsubscribing from articles
A client unsubscribes from articles of type "ENTERTAINMENT". Expected Results: The client should receive a message indicating that they unsubscribed from articles of type "ENTERTAINMENT" successfully.
A client unsubscribes from articles from organization "CNN". Expected Results: The client should receive a message indicating that they unsubscribed from articles from organization "CNN" successfully.
Publishing articles with different types and organizations
A client publishes an article of type "ENTERTAINMENT". Expected Results: All clients subscribed to articles of type "ENTERTAINMENT" should receive the published article.
A client publishes an article from organization "CNN". Expected Results: All clients subscribed to articles from organization "CNN" should receive the published article.
Leaving the server
A client leaves the
