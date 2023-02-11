import socket
import rpyc
import threading

class PubSubClient:
    MAXSTRING = 120

    def __init__(self, server_ip, server_port):
        self.conn = rpyc.connect(server_ip, server_port)
        self.server = self.conn.root

    def join(self, ip, port):
        print(self.server.join(ip, port))

    def leave(self, ip, port):
        print(self.server.leave(ip, port))

    def subscribe(self, ip, port, article):
        print(self.server.subscribe(ip, port, article))

    def unsubscribe(self, ip, port, article):
        print(self.server.unsubscribe(ip, port, article))

    def publish(self, article, ip, port):
        print(self.server.publish(article, ip, port))

    def ping(self):
        print(self.server.ping())

    def receive(self, port):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(("", port))
        while True:
            article, _ = udp_socket.recvfrom(self.MAXSTRING)
            print("Received article:", article.decode())

    def start(self, port):
        receive_thread = threading.Thread(target = self.receive, args = (port,))
        receive_thread.start()


if __name__ == "__main__":
    
    client = PubSubClient("localhost", 18861)
    while True:
        print("Enter the request you want to make (join/subscribe/unsubscribe/publish/leave/ping/exit):")
        request = input().strip()
        if request == "join":
            print("Enter IP address:")
            ip = input().strip()
            print("Enter port:")
            port = int(input().strip())
            client = PubSubClient("localhost", 18861)
            client.join(ip, port)
        elif request == "subscribe":
            print("Enter IP address:")
            ip = input().strip()
            print("Enter port:")
            port = int(input().strip())
            print("Enter article (format: type;originator;org;contents):")
            article = input().strip()
            client.subscribe(ip, port, article)
        elif request == "unsubscribe":
            print("Enter IP address:")
            ip = input().strip()
            print("Enter port:")
            port = int(input().strip())
            print("Enter article (format: type;originator;org;contents):")
            article = input().strip()
            client.unsubscribe(ip, port, article)
        elif request == "publish":
            print("Enter IP address:")
            ip = input().strip()
            print("Enter port:")
            port = int(input().strip())
            print("Enter article (format: type;originator;org;contents):")
            article = input().strip()
            client.publish(article, ip, port)
        elif request == "leave":
            print("Enter IP address:")
            ip = input().strip()
            print("Enter port:")
            port = int(input().strip())
            client.leave(ip, port)
        elif request == "ping":
            client.ping()
        elif request == "exit":
            break
        else:
            print("Invalid request. Please try again.")
