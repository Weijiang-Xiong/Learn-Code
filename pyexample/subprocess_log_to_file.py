# import os
import subprocess 

with open("log.txt", "at") as f:
    subprocess.run("python pyexample/gzip_save_load.py", shell=True, stdout=f, stderr=f)

captured_output = subprocess.run("python pyexample/gzip_save_load.py", shell=True, capture_output=True)
print("the captured outputs are \n", captured_output.stdout.decode())

# clean up
# os.remove("log.txt")