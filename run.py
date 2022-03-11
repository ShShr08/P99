import os, shutil, time
path = input("Path to be searched in. ")
seconds = time.time() - (15 * 86400)

if os.path.exists(path):
  for root, directories, files in os.walk(path, topdown=True):
    for name in files:
      path = os.path.join(root, name)
      age = os.stat(path).st_age
      if seconds >= age:
        os.remove(path)
    for name in directories:
      path = os.path.join(root, name)
      age = os.stat(path).st_age
      if seconds >= age:
        shutil.rmtree(path)
else:
    print("Path not found")