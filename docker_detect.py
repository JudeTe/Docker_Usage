import os
from lineNotify import lineNotify

if os.path.exists("docker_usage.txt"):
    with open("docker_usage.txt", "r", encoding="utf-8") as f:
        output = f.read().split(" ")[2]
        IntOutput = output.split(".")[0]
        if IntOutput < 40 :
            
        #print(output)
            lineNotify("CPU usage " + output + " used!")





