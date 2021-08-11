#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess 
import cgi
#cmd = "kubectl get pods --kubeconfig admin.conf"
#o = subprocess.getoutput(cmd)
#print(o)

f=cgi.FieldStorage()
cmd=f.getvalue("commands")
name=f.getvalue("name")
replicas=f.getvalue("replica")
port=f.getvalue("port")

if(("all" in cmd) or ("number" in cmd) or ("no." in cmd) or ("Number" in cmd)) and (("pods" in cmd) or ("pod" in cmd) or ("Pod" in cmd)):
    output=subprocess.getoutput("kubectl get pods --kubeconfig admin.conf")
    print("<body style ='padding: 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")
    

elif(("all" in cmd) or ("get" in cmd) ) and (("deployments" in cmd) or ("Deployments" in cmd) or ("deployment" in cmd)):
    output=subprocess.getoutput("kubectl get deployments --kubeconfig admin.conf")    
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

elif(("create" in cmd) or ("launch" in cmd) or ("form" in cmd) or ("run" in cmd) or ("run" in cmd)) and (("pod" in cmd) or ("pods" in cmd)):
    output=subprocess.getoutput("kubectl run {} --image=centos:latest --kubeconfig admin.conf".format(name))
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

elif(("create" in cmd) or ("launch" in cmd)) and (("deployments" in cmd) or ("deployment" in cmd)):
    output=subprocess.getoutput("kubectl create deployment {} --image=centos:latest --kubeconfig admin.conf".format(name))
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

elif ("expose" in cmd) and ("deployment" in cmd):
    output=subprocess.getoutput("kubectl expose deployment {} --port={} --type=NodePort --kubeconfig admin.conf".format(name,port))
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

elif (("create" in cmd) or ("scale" in cmd) or ("replica" in cmd)) and ("deployment" in cmd):
    output=subprocess.getoutput("kubectl scale deployment {} --replicas={} --kubeconfig admin.conf",format(name,replicas))
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

elif (("delete" in cmd ) or ("remove" in cmd )) and ("deployment" in cmd):
    output=subprocess.getoutput("kubectl delete  deployment {}",format(name))
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

elif (("delete" in cmd ) or ("remove" in cmd )) and ("pods" in cmd):
    output=subprocess.getoutput("kubectl delete  pods {} --kubeconfig admin.conf",format(name))
    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")

else:

    print("<body style ='padding; 40px;'>")
    print('<h1 style="color: #df405a ; " >OUTPUT</h1>')
    print("Invalid commands")
    print("<pre>{}</pre>".format("Please type the Kubernetes Commands only !!"))
    print("</body>")
