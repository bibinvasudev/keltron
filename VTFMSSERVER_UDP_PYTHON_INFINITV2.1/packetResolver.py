import dbactions

def insert_into_table(packet,dbObj):
	dataSplit=packet.split(',')
        if(len(dataSplit)!=8):
        
        	
		sqlUp= "Update \"avtms_vehiclelocation\" set latitude="+dataSplit[1]+",latitudedir='"+dataSplit[2]+"',longitude="+dataSplit[3]+",longitudedir='"+dataSplit[4]+"',utctime='"+dataSplit[5]+"',speed='"+dataSplit[6] +"',direction= "+dataSplit[7]+",key_status= '"+dataSplit[8]+"',inputpin_status='"+dataSplit[9]+"',display_status='"+dataSplit[10]+"',front_panel_display='"+dataSplit[11]+"',odometer='"+dataSplit[12]+"',input_output_pin_status='"+dataSplit[13]+"' where simno = "+dataSplit[0]
		print sqlUp
		#dbObj.executeQuerry(sqlIns)
		dbObj.executeQuerry(sqlUp)

        	#if not dbObj.search("select *from \"avtms_vehiclelocatio\" where simno"+dataSplit[0]):
		#	if dbObj.executeQuerry(sqlIns):
		#		print " 'Vehicle' -Inserted"
		#else:
	        #	if dbObj.executeQuerry(sqlUp):
		#		print "'Vehicle' -Updated"
	else:
		print "Wrong packet format"
