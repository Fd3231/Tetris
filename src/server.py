import random
import socket
from threading import Thread


HOST= "127.0.0.1"
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class RandomGenerator:
	def __init__(self):
		self.bag = []
		self.refill_bag()
	
	def refill_bag(self):
		self.bag = [0,1,2,3,4,5,6]
		random.shuffle(self.bag)
	
	def get_next_piece(self):
		if len(self.bag) == 0:
			self.refill_bag()
		return self.bag.pop(0)

r = RandomGenerator()
pieces1 = list()
pieces2 = list()

try:
    s.bind((HOST,PORT))
except socket.error as err:
    str(err)

s.listen(2)
print("Waiting for connection")

def threaded_client(conn,player):
    reply = ""
    print(player)
    conn.send(str(player).encode("utf-8"))
    while True:
        try:
            data = conn.recv(2048)
            if not data:
                print("Disconnected")
                break
            else:
                if data=="over":
                    playerReady[player] = True
                else:
                    reply = get_piece(conn,player)


            conn.sendall(str(reply).encode("utf-8"))
        except:
            break
    print("Connection closed")
    conn.close()


def get_piece(conn,clientId):
    print(clientId)
    playerReady[clientId] +=1
    while (playerReady[0] != playerReady[1]):
        pass
    piece = r.get_next_piece()
    pieces1.append(piece)
    pieces2.append(piece)
    if clientId == 0:
        return pieces1.pop(0)
    return pieces2.pop(0)


playerReady = [0,0]
player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    thread = Thread(target=threaded_client, args=(conn, player))
    thread.start()
    player+=1
