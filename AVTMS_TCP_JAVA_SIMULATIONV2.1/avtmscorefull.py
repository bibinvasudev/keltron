import time
import threading
import math
import sys
import os
from socket import *
import datetime
import random
import alert


class avtmscorefull(threading.Thread):
	
	def __init__(self,path,s,time_intervel):

		self.s = s
		self.time_intervel = int(time_intervel)
		self.pathin =path
		threading.Thread.__init__(self)

# ----------finding distance between two points.............

	def finddistance(self,x1,y1,x2,y2):
		
		distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
		return distance

# ----------finding the new points--------------------------

	def findnewpoint(self,wx,wy,x2,y2,speed):
		
		
		y2 = y2
		newpoint = []	
		
		if wx==x2:	
			
			v = 0
			v1 = 1
			angle = 90
			if y2 >wy:
				time.sleep(self.time_intervel)
				newangle = 0						
				newpoint.insert(0,wx+speed*v)
				newpoint.insert(1,wy+speed*v1)
				newpoint.insert(2,newangle)
				return newpoint
			else:
				time.sleep(self.time_intervel)
				newpoint.insert(0,wx+speed*v)
				newangle = 180				
				newpoint.insert(1,wy-speed *v1)	
				newpoint.insert(2,newangle)
				return newpoint
			
		elif wy==y2:
			
			v1 =0
			v =1
			angle = 0
			if x2>wx:
			
				newangle = 270
				newpoint.insert(0,wx+speed*v)
				newpoint.insert(1,wy+speed*v1)
				newpoint.insert(2,newangle)
				return newpoint				
				
			else:	
			
				newangle = 90
				newpoint.insert(0,wx-speed*v)
				newpoint.insert(1,wy+speed*v1)
				newpoint.insert(2,newangle)
				return newpoint

		else:
								
			slope = (y2-wy)/(x2-wx)
			if slope <0:
				slope = -1*slope
			anglerad = math.atan(slope)	
			angle = anglerad*57.2957795
			v = math.cos(anglerad)
			v1 = math.sin(anglerad)
			
		if x2>wx and y2>wy:
										
			time.sleep(self.time_intervel)
			newpoint.insert(0,wx+speed*v)
			newpoint.insert(1,wy+speed*v1)
			newangle = 270+angle
			newpoint.insert(2,newangle)
			return newpoint
				
		elif wx> x2 and wy >y2:
						
			time.sleep(self.time_intervel)
			newpoint.insert(0,wx-speed *v)
			newpoint.insert(1,wy-speed *v1)
			newangle = 90+angle
			newpoint.insert(2,newangle)
			return newpoint

		elif wx>x2 and wy<y2:
		
			time.sleep(self.time_intervel)
			newpoint.insert(0,wx-speed*v)
			newpoint.insert(1,wy+speed*v1)
			newangle = 90-angle
			newpoint.insert(2,newangle)
			return newpoint

		else:
			time.sleep(self.time_intervel)
			newpoint.insert(0,wx+speed*v)
			newpoint.insert(1,wy-speed *v1)	
			newangle = 270-angle
			newpoint.insert(2,newangle)
			return newpoint

	def run(self):	
		
		try:
			x = []
			y = []
			del(x[0:50])
			del(y[0:50])
	
			fp_src = open(self.pathin,"r");
			remain =0
			print "fp_src",fp_src
# reading data line by line
			for line in fp_src:
					
				if line[0] == 'v':
					lstr=line.lstrip()
	        			rstr=lstr.rstrip() 
	        			tmpstr=rstr.strip()
					line_lst=tmpstr.split('\t')
					vid = str(line_lst[1])
		                  	
				elif line[0] == 's':
			
					lstr=line.lstrip()
	        			rstr=lstr.rstrip() 
	        			tmpstr=rstr.strip()
					line_lst=tmpstr.split('\t')
	        			speed =float(line_lst[1])
					
				elif line[0] ==' ':
				
					break			

				else:
		
					lstr=line.lstrip()
	        			rstr=lstr.rstrip() 
	        			tmpstr=rstr.strip()
					line_lst=tmpstr.split('\t')
					x.append(line_lst[0])
					y.append(line_lst[1])

			spmin = speed*.2
			i = 0
			spmax = speed+spmin
			speed =spmin + random.random()*(spmax-spmin)
			temp = 0				
			k = len(x)
			wx =float(x[0])
			wy =float(y[0])
	
			while i < k-1 :

				x2=float(x[i+1])
				y2=float(y[i+1])
				x1=float(x[i])
				y1=float(y[i])
				distance = self.finddistance(x1,y1,x2,y2)
				temp = temp+distance+remain
						
				if temp<=speed and i+1 ==k-1:
					i = 0
					distance = 0
					temp = 0
					wx =float(x[0])
					wy =float(y[0])

				elif temp<= speed and i+1 != k -1:

					remain = 0
             				i = i+1

				else:
					p = 1
					j =speed
					while j<= temp:
					
						x1 = wx
						y1 = wy
						newpoint= self.findnewpoint(x1,y1,x2,y2,speed)
						wx = newpoint[0]
						wy = newpoint[1]
						distire =newpoint[2]
						x1 = wx
						y1 = wy
						typ = '1'
						status = '12'

#taking time in a proper format as server required
 
						self.now = datetime.datetime.now()
						self.tim1=self.now.strftime("%H%M%S")
						self.tim2 = self.now.strftime("%d%m")
						self.tim2 = self.tim2+"08"
						

#converting lat long 				
						lat = wy
						lat1 = float(int(lat)*100+((lat%1)*60))
	
						longi = wx
						longi1 = float(int(longi)*100+((longi%1)*60))
						
						ab = "VTS,"+str(vid)+",NM,GP,00,"+str(self.tim1)+",A,"+str(lat1)+",N,"+str(longi1)+",E,0.000000,0.00,"+str(self.tim2)+",35,4F9C"
						print ab
						
						self.s.send(ab)

						p = p+1
						j = speed * p
						
				
					j = j-speed
					remain =temp-j
					temp = 0
					distance = 0 
					speed =spmin + random.random()*(spmax-spmin)
			
					if i +1== k -1:
						i = 0
						distance = 0
						temp = 0
						remain = 0
						wx =float(x[0])
						wy =float(y[0])
					else:
  				
             					i = i+1
				

		except Exception, X :
			self.s.close()
			print "ERROR IN CONNECTION !!!!! !  !   !     !       SERVER REFUSED CONNECTION !!!!!!!!!!!!!!!!!!"

					
		


	 
	
