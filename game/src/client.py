from matc_client.match import Match
from matc_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from sys import stdin

def operate(op, userid, username, score):
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    user = User(userid, username, score)
    
    if op == "add":
        client.add_user(user, "")
    elif op == "remove":
        client.remove_user(user, "")

    #Close!
    transport.close()

def main():
    for line in stdin:
        op, user_id, username, score = line.split(" ")
        operate(op, int(user_id), username, int(score))


if __name__ == "__main__":
    main()
