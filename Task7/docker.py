#! /usr/bin/python3
print("content-type:text/html")
print()
import subprocess as sp
import cgi
values=cgi.FieldStorage
osname=values.getvalue("name")
image=values.getvalue("imgname")
cmd=values.getvalue("cmd")
command=values.getvalue("command")

if (cmd=="run"):
	output=sp.getstatusoutput("sudo docker run -dit --name {} {}".format(osname,image))
elif (cmd=="show containers"):
	output=sp.getstatusoutput("sudo docker ps")
elif (cmd=="show images"):
	output=sp.getstatusoutput("sudo docker images")
elif (cmd=="execute"):
	output=sp.getstatusoutput("sudo docker exec {} {}".format(osname,command))
elif (cmd=="remove"):
	output=sp.getstatusoutput("sudo docker rm {} -f".format(osname))
elif(cmd=="start"):
	output=sp.getstatusoutput("sudo docker start {} ".format(osname))
elif(cmd=="attach"):
	output=sp.getstatusoutput("sudo docker attach {} ".format(osname))
elif (cmd=="stop"):
	output=sp.getstatusoutput("sudo docker stop {} ".format(osname))
elif (cmd=="run and delete"):
	output=sp.getstatusoutput("sudo docker run -dit rm".format(osname))

if (output[0]==0):
	print(output[1])
else:
	print("Error in execution!")
	print(output[1])
