from socket import *
serverPort = 21000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('Client B is ready to receive')
with open("clientB_confirmed.txt", 'w') as writer:
    writer.write("")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()

    i = 0
    for items in modifiedMessage.split(" "):
        if items == "0xB0000001" or items == "0xB0000002":
            with open("balancesB.txt", 'r') as reader:
                trans = reader.read().split(" ")
                if items == "0xB0000001":
                    trans[2] = trans[1]
                elif items == "0xB0000002":
                    trans[5] = trans[4]
            with open("balancesB.txt", "w") as writer:
                for lines in trans:
                    writer.write(lines + " ")
            with open("clientB_unconfirmed.txt", 'r') as reader:
                contents = reader.read().split(" ")
                tx = contents.pop(0)
            with open("clientB_unconfirmed.txt", 'w') as writer:
                for lines in contents:
                    writer.write(lines + " ")
            with open("clientB_confirmed.txt", 'a') as ap:
                ap.write(tx + " ")
        elif items == "0xA0000001" or items == "0xA0000002":
            with open("balancesB.txt", 'r') as reader:
                trans = reader.read().split(" ")
                if items[i + 1] == "0xB0000001":
                    unconfirmed_amount = hex(int(trans[1], 16) + int(items[i + 2]))
                    confirmed_amount = hex(int(trans[2], 16) + int(items[i + 2]))
                    trans[1] = unconfirmed_amount
                    trans[2] = confirmed_amount
                elif items[i + 1] == "0xB0000002":
                    unconfirmed_amount = hex(int(trans[1], 16) + int(items[i + 2]))
                    confirmed_amount = hex(int(trans[2], 16) + int(items[i + 2]))
                    trans[1] = unconfirmed_amount
                    trans[2] = confirmed_amount
            with open("balancesB.txt", 'w') as writer:
                for lines in trans:
                    writer.write(lines + " ")
            with open("clientB_unconfirmed.txt", 'r') as reader:
                contents = reader.read().split(" ")
                tx = contents.pop(0)
            with open("clientB_confirmed.txt", 'a') as ap:
                ap.write(tx + " ")
        else:
            i += 1