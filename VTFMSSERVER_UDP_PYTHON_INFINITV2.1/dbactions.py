#!/usr/bin/python	
#----------------------------
import psycopg2 
import config

#------class for database connection and activities
#-------------------------------------------

class DbActivity:
	host=config.Host
	user=config.User
	pwd=config.Pwd
	db=config.Db

	#----------connect database via constructor---------
	def __init__(self):
		try:
			self.connection=psycopg2.connect("host="+DbActivity.host+" dbname="+DbActivity.db+" user="+DbActivity.user+" password="+DbActivity.pwd)
			#self.connection=psycopg.connect("host=192.168.1.109 dbname=mydb user=gopakumar password=panavila")
		except:
			print "database connection error"

	#------------execute the querry--------------------
	def executeQuerry(self,sqlQuerry):
		try:
			self.cursor=self.connection.cursor()
			self.cursor.execute(sqlQuerry)
			self.connection.commit()
			return True
		except:       
			print "querry error"

	#-----------------passing the querry for searching--------
	def search(self,querry):
		callid=[]
		if self.executeQuerry(querry):
			for self.row in self.cursor.fetchall():
				for self.col in self.row:
					callid.append(self.col)
		return callid

	#----------------close your database connectio object-----
	def close(self):
		self.connection.close()

	
								
		
	

