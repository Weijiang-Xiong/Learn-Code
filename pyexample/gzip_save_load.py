import os
import json
import gzip 
import numpy as np

data = {"a": np.random.rand(10, 10, 10).tolist(), 
        "b": np.random.rand(10, 10, 10).tolist(), 
        "c": np.random.rand(10, 10, 10).tolist()}

print("Saving and loading compressed data...")
# Save data to a gzip file
with gzip.open("data.json.gz", "wt") as f:
    json.dump(data, f)
    
with gzip.open("data.json.gz", "rt") as f:
    data_read = json.load(f)
    # print(data)

print("File size of compressed data in Bytes: ", os.path.getsize("data.json.gz"))

print("Saving and loading uncompressed data...")
with open("data.json", "wt") as f:
    json.dump(data, f)

with open("data.json", "rt") as f:
    data_read = json.load(f)
    # print(data_read)

print("File size of uncompressed data in Bytes: ", os.path.getsize("data.json"))

print("Saving and loading compressed data by serializing into a string and write to a gzip file...")
with gzip.open("data_method2.json.gz", "wt") as f:
    f.write(json.dumps(data))

try:
    data_read = json.load(gzip.open("data_method2.json.gz", "rt"))
except:
    print("json.load() on this file can raise an error (happened with the aimsun-saved gz files, maybe because of an old version of python or json library)") 

print("Instead, use json.loads(f.read())")
data_read = json.loads(gzip.open("data_method2.json.gz", "rt").read())

print("Cleaning up...")
os.remove("data.json")
os.remove("data.json.gz")
os.remove("data_method2.json.gz")