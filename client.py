import socket
import json
import sys
import os


clientSocket = socket.socket()
host = "192.168.240.8"
port = 8888

try:
	clientSocket.connect((host,port))

except socket.error as e:
	print (str(e))

response = clientSocket.recv(1024).decode()
opt1 = input("Name:")
clientSocket.send(str.encode(opt1))
name1 = clientSocket.recv(2048).decode()
no = input("Number Phone:")
clientSocket.send(str.encode(no))
num = clientSocket.recv(2048).decode()
d = json.loads(response)
while True:


  print ("Skincare Supplier")
  print ("-----------------")
  for keys in d.keys():
    name,cost = d[keys]
    print ('Item Code ->',keys,'Product->:',name,'\n','The cost is :',cost)


 # opt = input("Enter Your name:")
  #clientSocket.send(str.encode(opt))
  #name1 = clientSocket.recv(2048).decode()
  #no = input("Enter Your Number:")
  #clientSocket.send(str.encode(no))
  #num = clientSocket.recv(2048).decode()
  #print ("\nWelcome Mr %s"+str(name1))
  #print ("\nNumber Phone: %s"+str(num))
  option = input('\nYour Option:')
  clientSocket.send(str.encode(option.strip()))
  check = clientSocket.recv(2048).decode()

  if check == 'YES':
    quantity = input('Number quantity:')
    clientSocket.send(str.encode(quantity))
    product = clientSocket.recv(2048).decode()
    print ("Product select:",product)
    result = clientSocket.recv(2048).decode()
    print ("Order Total:",result,)
    print ("*-----------------*\n")
    #ans = input("Do you want to delete item?")
    #clientSocket.send(str.encode(ans))

  elif check == 'FINISH':
    ans = input("Do you want to delete item?")
    clientSocket.send(str.encode(ans))
    fb = clientSocket.recv(2048).decode()
    print (fb)
   
    ans1 = input("Enter the Product item name?")
    clientSocket.send(str.encode(ans1))
    fb1 = clientSocket.recv(2048).decode()
    print(fb1)
    ans2 = input("Do you want cancel all this product?")
    clientSocket.send(str.encode(ans2))
    fb2 = clientSocket.recv(2048).decode()
    print(fb2)

    if fb2 == "YES":
      clientSocket.send(b"My Latest product")
      fb3 =clientSocket.recv(2048).decode()
      print (fb3)
      clientSocket.send(b'Please')
      fb4 =clientSocket.recv(2048).decode()
      print(fb4)
     #receive receipt file
    print('Session Ended')
    exit(0)

  elif check == 'NO':
    print("No Matched Item Code")


clientSocket.close()
