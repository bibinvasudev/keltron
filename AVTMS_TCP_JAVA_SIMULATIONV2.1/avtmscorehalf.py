import time
import threading

import math
import sys

import os
import socket
import datetime
import random


class avtmscorehalf(threading.Thread):

	
	
	def __init__(self,path,s,time_intervel):
		self.time_intervel =int(time_intervel)
		self.s = s
		self.pathin =path
		self.vid = []
		self.speed = []
		self.x = []
		self.y = []
		self.lis=[]
		self.fp_src  =0
		self.line_lst = 0
		self.temp = 0
		self.remain = 0
		self.spmin  =0
		self.spmax = 0
		self.ab = ''
		threading.Thread.__init__(self)

	def finddistance(self,x1,y1,x2,y2):
		
		self.x1 = self.x1
		self.x2 = self.x2
		self.y1 = self.y1
		self.y2 = self.y2
		self.val1=self.x2-self.x1	
		self.ds= pow(self.val1,2)
		self.val2=self.y2-self.y1
		self.ds1= pow(self.val2,2)
		self.val=self.ds+self.ds1
		self.d=math.sqrt(self.val)	
		return self.d


	def findnewpoint(self,wx,wy,x2,y2,speed):
		
		self.newpoint = []	
		
		if self.wx==self.x2:	
			
			self.v = 0
			self.v1 = 1
			self.angle = 90
			if self.y2 >self.wy:
				time.sleep(self.time_intervel)
				self.wx = self.wx+self.speed*self.v
				self.wy = self.wy+self.speed*self.v1
				self.newangle = 0						
				self.newpoint.insert(0,self.wx)
				self.newpoint.insert(1,self.wy)
				self.newpoint.insert(2,self.newangle)
				return self.newpoint
			else:
				time.sleep(self.time_intervel)
				self.wx = self.wx+self.speed*self.v
				self.wy= self.wy-self.speed *self.v1
				self.newpoint.insert(0,self.wx)
				self.newangle = 180				
				self.newpoint.insert(1,self.wy)	
				self.newpoint.insert(2,self.newangle)
				return self.newpoint
			
		elif self.wy==self.y2:
			
			self.v1 =0
			self.v =1
			self.angle = 0
			if self.x2>self.wx:
				self.wx = self.wx+self.speed*self.v
				self.wy = self.wy+self.speed*self.v1
				self.newangle = 270
				self.newpoint.insert(0,self.wx)
				self.newpoint.insert(1,self.wy)
				self.newpoint.insert(2,self.newangle)
				return self.newpoint				
				
			else:	
				self.wx = self.wx-self.speed*self.v
				self.wy = self.wy+self.speed*self.v1
				self.newangle = 90
				self.newpoint.insert(0,self.wx)
				self.newpoint.insert(1,self.wy)
				self.newpoint.insert(2,self.newangle)
				return self.newpoint

		else:
			
			self.slope = (self.y2-self.wy)/(self.x2-self.wx)
			
			if self.slope <0:
				self.slope = -1*self.slope
			
			self.anglerad = math.atan(self.slope)	
			self.angle = self.anglerad*57.2957795
			self.v = math.cos(self.anglerad)
			self.v1 = math.sin(self.anglerad)
		
		if self.x2>self.wx and self.y2>self.wy:
										
			time.sleep(self.time_intervel)
			self.wx = self.wx+self.speed*self.v
			self.wy = self.wy+self.speed*self.v1						
			self.newpoint.insert(0,self.wx)
			self.newpoint.insert(1,self.wy)
			self.newangle = 270+self.angle
			self.newpoint.insert(2,self.newangle)
			return self.newpoint
				
		elif self.wx> self.x2 and self.wy >self.y2:
						
			time.sleep(self.time_intervel)
			self.wx = self.wx-self.speed *self.v
			self.wy= self.wy-self.speed *self.v1						
			self.newpoint.insert(0,self.wx)
			self.newpoint.insert(1,self.wy)
			self.newangle = 90+self.angle
			self.newpoint.insert(2,self.newangle)
			return self.newpoint

		elif self.wx>self.x2 and self.wy<self.y2:

			time.sleep(self.time_intervel)
			self.wx =self.wx-self.speed*self.v
			self.wy =self.wy+self.speed*self.v1	
			self.newpoint.insert(0,self.wx)
			self.newpoint.insert(1,self.wy)
			self.newangle = 90-self.angle
			self.newpoint.insert(2,self.newangle)
			return self.newpoint
		else:
			time.sleep(self.time_intervel)
			self.wx = self.wx+self.speed*self.v
			self.wy= self.wy-self.speed *self.v1
			self.newpoint.insert(0,self.wx)
			self.newpoint.insert(1,self.wy)	
			self.newangle = 270-self.angle
			self.newpoint.insert(2,self.newangle)
			return self.newpoint
				

		del self.newpoint[0]
		del self.newpoint[1]
		del self.newpoint[2]
			
		
		
	def run(self):	
		
		del(self.x[0:150])
		del(self.y[0:150])
		del(self.vid[0:1])
		del(self.speed[0:1])
		self.fp_src = open(self.pathin,"r");
		
#reading data line by line
		for line in self.fp_src:
					
			
			if line[0] == 'v':
				self.lstr=line.lstrip()
	        		self.rstr=self.lstr.rstrip() 
	        		self.tmpstr=self.rstr.strip()
				self.line_lst=self.tmpstr.split('\t')
				self.vid.append(self.line_lst[1])				
	                  	
			elif line[0] == 's':
			
				self.lstr=line.lstrip()
	        		self.rstr=self.lstr.rstrip() 
	        		self.tmpstr=self.rstr.strip()
				self.line_lst=self.tmpstr.split('\t')
	        		self.speed.append(self.line_lst[1])

			elif line[0] ==' ':
				print "vfbsdbfkjsbfkjsbfkjsdbkjflbsdkjlbfkjsdbfkjsbfkjbsd"
				break			
			else:
		
				self.lstr=line.lstrip()
	        		self.rstr=self.lstr.rstrip() 
	        		self.tmpstr=self.rstr.strip()
				self.line_lst=self.tmpstr.split('\t')
	                		
				self.x.append(self.line_lst[0])
				self.y.append(self.line_lst[1])
		
		self.vid =self.vid[0]
		
		self.speed = float(self.speed[0])
		self.spmin = self.speed*.2
		self.spmax = self.speed+self.spmin
		self.speed =self.spmin + random.random()*(self.spmax-self.spmin)
		self.x =self.x
		self.y =self.y
		self.k = len(self.x)
		self.wx =float(self.x[0])
		self.wy =float(self.y[0])
				
	
		for i in range(self.k-1 ):
			
			self.x2=float(self.x[i+1])
			self.y2=float(self.y[i+1])
			self.x1=float(self.x[i])
			self.y1=float(self.y[i])
			self.d = self.finddistance(self.x1,self.y1,self.x2,self.y2)
			self.temp = self.temp+self.d+self.remain
			if self.temp<=self.speed:
				
				self.remain = 0
				if i == self.k -2:
					print "Warning !!!! stopped   !!!!!!!!!!!!!!!!!!" 
			
			else:
				self.p = 1
				self.j = float(self.speed)
				while self.j<= self.temp:
				
					self.locpoint = self.findnewpoint(self.wx,self.wy,self.x2,self.y2,self.speed)
					self.wx = self.locpoint[0]
					self.wy = self.locpoint[1]
					self.dire =self.locpoint[2]

#taking time to proper format as server needed

					self.now = datetime.datetime.now()
					self.tim=self.now.strftime("%Y-%m-%d %H:%M:%S")
					self.tim1=self.now.strftime("%H%M%S")
					self.tim2 = self.now.strftime("%d%m")
					self.tim2 = self.tim2+"08"

					self.typ = '1'
					self.status = '12'
#converting lat long
					lat =self.wy
					lat1 = float(int(lat)*100+((lat%1)*60))

					longi = self.wx
					longi1 = float(int(longi)*100+((longi%1)*60))
		
					ab = "VTS,"+str(self.vid)+",NM,GP,00,"+str(self.tim1)+",A,"+str(lat1)+",N,"+str(longi1)+",E,0.000000,0.00,"+str(self.tim2)+",35,4F9C"
					print ab
					self.s.send(ab)
					self.p = self.p+1
					self.j = self.speed*self.p
					
				
				self.j = self.j-self.speed
					
				self.remain =self.temp-self.j
				self.temp = 0
				self.d = 0 

				self.speed =self.spmin + random.random()*(self.spmax-self.spmin)

