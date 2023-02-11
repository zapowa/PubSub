import socket
import rpyc
from rpyc.utils.server import ThreadedServer

class PubSubServer(rpyc.Service):
    MAXCLIENT = 100
    MAXSTRING = 120
    clients = []
    articles = [] 
    
    def on_connect(self, conn):
        self.clients.append((conn, conn._channel.stream.sock.getpeername(), "", "", ""))

    def on_disconnect(self, conn):
        self.clients = [client for client in self.clients if client[0]._channel.stream.sock != conn._channel.stream.sock]

    def exposed_join(self, ip, port, conn=None):
        self.clients.append((conn, ip, port, "", ""))
        print("Client joined with IP:", ip, "and port:", port)
        return "Client joined successfully."

    def exposed_leave(self, ip, port):
        self.clients = [client for client in self.clients if client[:2] != (ip, port)]
        print("Client left with IP:", ip, "and port:", port)
        return "Client left successfully."

    def exposed_unsubscribe(self, ip, port, article):
        fields = article.split(";")
        if len(fields) != 4:
            return "Error: badly formatted article."
        type, originator, org, contents = fields
        self.clients = [client for client in self.clients if client[:3] != (type, originator, org)]
        print("Client unsubscribed with IP:", ip, "and port:", port, "for article type:", type)
        return "Unsubscription successful."

    def exposed_subscribe(self, ip, port, article, conn=None):
        fields = article.split(";")
        if len(fields) != 4:
            return "Error: badly formatted article."
        type, originator, org, contents = fields
        if not type:
            return "Error: type field is missing."

        if article not in self.articles:
            return "Error: article does not exist."

        self.clients.append((conn, ip, port, type, org))
        print("Client subscribed with IP:", ip, "and port:", port, "for article type:", type)
        return "Subscription successful."

    def exposed_publish(self, article, ip, port):
        fields = article.split(";")
        if len(fields) != 4:
            return "Error: badly formatted article."
        type, originator, org, contents = fields
        if not contents:
            return "Error: contents field is missing."

        self.articles.append(article)

        for conn, connid, c_type, c_org, _ in self.clients:
            if (not type or c_type == type) and (not org or c_org == org):
                conn.root.receive(article)
        print("Article published with IP:", ip, "and port:", port, "and type:", type)
        return "Article published successfully."

    def exposed_ping(self):
        print("Ping received.")
        return "Server is up."


if __name__ == "__main__":
    server = ThreadedServer(PubSubServer, port = 18861)
    server.start()
