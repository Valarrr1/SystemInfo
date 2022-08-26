import psutil
import platform # importing class

#computer network name

print(f"Computer network name: {platform.node()}")#buradaki f ne işe yarıyor anlayamadım.

#machine type
print(f"Machine type:  {platform.machine()}")

#proccesor type
print(f"Proccesors type: {platform.processor()}")

#platform type
print(f"Platform type: {platform.platform()}")

#operating system
print(f"OS : {platform.system()}")

#operating system relase
print(f"OS release: {platform.release()}")

#OS version

print(f"OS version : {platform.version()}")

print(f"Number of pyhsical cores: {psutil.cpu_count(logical=False)}")
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")

print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
