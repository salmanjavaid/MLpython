crs = open("D:\\Parsed\\Class 10\\34040-34500.txt", "r")
for columns in ( raw.strip().split() for raw in crs ):  
   print columns[0]
