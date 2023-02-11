Design Document:

The system consists of two components: the server and the client.



Server Component:

Implemented using the Remote Procedure Call (RPC) library rpyc
Maintains a list of clients and articles
Exposes methods to join, leave, subscribe, unsubscribe, publish and ping
Publishes articles to clients that have subscribed to a specific type or organization
Uses ThreadedServer from rpyc to handle multiple client connections



Client Component:

Implements a PubSubClient class
Connects to the server using the rpyc library
Allows the user to make requests such as join, subscribe, unsubscribe, publish and leave
Receives articles using a UDP socket
Starts a receive thread to listen for incoming articles



Instructions:

Server:

Install the rpyc library using "pip3 install rpyc"
To start the server, run "python3 server.py"

Client:

Install the rpyc library using "pip3 install rpyc"
To start the client, run "python3 client.py"
Follow the on-screen prompts to make requests to the server




Testing Description:

The following test cases have been attempted:



Joining the server with different IP addresses and ports:

Test Case #1: A single client joins the server with a valid IP address and port.
Expected Results: The client should receive a message indicating that they joined the server successfully.

Test Case #2: A single client attempts to join the server with an invalid IP address and port.
Expected Results: The client should receive a message indicating that they were unable to join the server.



Subscribing to articles of different types and organizations:

Test Case #1: A client subscribes to articles of type "ENTERTAINMENT".
Expected Results: The client should receive a message indicating that they subscribed to articles of type "ENTERTAINMENT" successfully.

Test Case #2: A client subscribes to articles from organization "CNN".
Expected Results: The client should receive a message indicating that they subscribed to articles from organization "CNN" successfully.



Unsubscribing from articles:

Test Case #1: A client unsubscribes from articles of type "ENTERTAINMENT".
Expected Results: The client should receive a message indicating that they unsubscribed from articles of type "ENTERTAINMENT" successfully.

Test Case #2: A client unsubscribes from articles from organization "CNN".
Expected Results: The client should receive a message indicating that they unsubscribed from articles from organization "CNN" successfully.



Publishing articles with different types and organizations:

Test Case #1: A client publishes an article of type "ENTERTAINMENT".
Expected Results: All clients subscribed to articles of type "ENTERTAINMENT" should receive the published article.

Test Case #2: A client publishes an article from organization "CNN".
Expected Results: All clients subscribed to articles from organization "CNN" should receive the published article.



Leaving the server:

Test Case #1: A client leaves the server.
Expected Results: The client should receive a message indicating that they left the server successfully.



Pinging the server:

Test Case #1: A client pings the server.
Expected Results: The client should receive a message indicating that the server is up and running.



Multiple request test case:

Test Case #1: Two clients join, both clients subscribe to "ENTERTAINMENT", one client publishes an entertainment article.

How to Run:
Client #1:

Start the client using python client.py
Enter "join" when prompted
Enter the IP address and port when prompted
Enter "subscribe" when prompted
Enter the article in the format "ENTERTAINMENT;client1;org1;article contents" when prompted
Client #2:
Start another instance of the client using python client.py
Enter "join" when prompted
Enter the IP address and port when prompted
Enter "subscribe" when prompted
Enter the article in the format "ENTERTAINMENT;client1;org1;article contents" when prompted
Client #1:
Enter "publish" when prompted
Enter the article in the format "ENTERTAINMENT;client1;org1;article contents" when prompted
Expected Results:

Both Client #1 and Client #2 should receive the published article.



Missing fields test case:

A client joins the server and tries to publish an article with missing fields.

How to Run:
Client #1:
Run python client.py
Enter "join" and provide the IP address and port
Enter "publish" and provide an article with missing fields
Expected Results:
The server should return an error message indicating the article is badly formatted




Source Code and Deliverables:

The source code and all necessary files have been tarred into a single file deliverables.tar.gz. To extract the files, run "tar -xzvf deliverables.tar.gz".
