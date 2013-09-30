import socket,sys,packetResolver,dbactions
import config

#create the socket and bind it to a port

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((config.SERVERIP,int(config.SERVERPORT)))

#establish a database connection 

obj=dbactions.DbActivity()

#variable for packet count 

count=0
print "VTFMSSERVER Starting............"

#listening for a packet
try:
	while True:
                data,addr=s.recvfrom(1024)
                count=count+1
                print "count="+str(count)
		print data
		
		#module for spliting and inserting the packet into the table

        	packetResolver.insert_into_table(data,obj) 
		print "--------"       
finally:
	s.close()




			

			

