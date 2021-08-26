#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

f = cgi.FieldStorage()
cmd = f.getvalue("x")
val = cmd.split()

#Creating deployment
if  val[0]=="1":
    dname = val[2]
    iname = val[1]
    out=sp.getoutput("sudo  kubectl create deployment {} --image={} --kubeconfig /root/admin.conf".format(dname,iname)) 
    print(out)

#Creating pod
elif  val[0]=="2":
    pname = val[2]
    iname = val[1]
    out=sp.getoutput("sudo  kubectl run {} --image={} --kubeconfig /root/admin.conf".format(pname,iname)) 
    print(out)

#Delete pod
elif  val[0]=="3":
    pname = val[1]
    out=sp.getoutput("sudo  kubectl delete pod {}  --kubeconfig /root/admin.conf".format(pname))
    print(out)

#delete deployment
elif  val[0]=="4":
    dname = val[1]
    out=sp.getoutput("sudo  kubectl delete deployment {} --kubeconfig /root/admin.conf".format(dname))
    print(out)

#expose deployment
elif  val[0]=="5":
    dname = val[1]
    port_no = val[2]
    etype  = val[3]
    out=sp.getoutput("sudo  kubectl expose deployment {} --type={} --port={} --kubeconfig /root/admin.conf".format(dname,etype,port_no)) 
    print(out)

#scale deployment
elif  val[0]=="6":
    dname = val[1]
    replica= val[2]
    out=sp.getoutput("sudo  kubectl scale deployment {} --replicas={} --kubeconfig /root/admin.conf".format(dname,replica)) 
    print(out)

#list pods
elif val[0]=="7":
    out=sp.getoutput("sudo  kubectl get pods --kubeconfig /root/admin.conf") 
    print(out)

#list deployments
elif val[0]=="8":
    out=sp.getoutput("sudo  kubectl get deployments --kubeconfig /root/admin.conf") 
    print(out) 
    
#list services
elif val[0]=="9":
    out=sp.getoutput("sudo  kubectl get svc --kubeconfig /root/admin.conf") 
    print(out)   

#error
else:
    val[0]=="404"
    print("Something went wrong.")
