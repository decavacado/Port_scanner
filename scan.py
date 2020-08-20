import socket

def scanner(ip):
    ports = [("SSH", 22),("HTTP", 80),("SMTP", 25),("HTTPS", 443),("FTP", 21),("MONGO", 27017),("SQL", 1433)]
    for selection in ports:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Checking port " + selection[0])
            val = soc.connect_ex((ip, selection[1]))
            if val == 0:
                print("{name} {port}:open".format(name=selection[0],port=selection[1]))
            else:
                print("{name} {port}:closed".format(name=selection[0],port=selection[1]))
            soc.close()
        except socket.error:
            print("Host not found")
        

address = input("What is the IP?")
print("Finding open ports ...")
scanner(address)

    