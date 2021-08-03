import pyshark
import json 


cap=pyshark.FileCapture("./toobeetootee.pcap")

points=[]

for c  in cap:
	try:
		if str(c["MINETEST.CLIENT"].command)=="0x00000039":
			if str(c["MINETEST.CLIENT"].interact_action) in ["0","1","2"]:
#				print(f"add block at x =",c["MINETEST.CLIENT"].interact_pointed_above_x," y = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show," z = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)
				points.append({"name":"brick","x":int(c["MINETEST.CLIENT"].interact_pointed_above_x),"y":int(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show),"z":int(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)})			
			elif str(c["MINETEST.CLIENT"].interact_action) in ["3"]:
#				print(f"remove block at x =",c["MINETEST.CLIENT"].interact_pointed_above_x," y = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show," z = ",c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)
				points.append({"name":"air","x":int(c["MINETEST.CLIENT"].interact_pointed_above_x),"y":int(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-2].show),"z":int(c["MINETEST.CLIENT"]._get_all_fields_with_alternates()[-1].show)})			

	except:
		pass



with open("points.json","w") as outfile:
	json.dump(points,outfile)


import miney
import json

#connect to world
mt=miney.Minetest()

#load node coordinates to change
with open("points.json","r") as infile:
	pts=json.load(infile)

mt.node.set(pts)

