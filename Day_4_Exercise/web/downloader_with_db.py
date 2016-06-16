import sqlite3
import urllib
import os

data_file='example.db'
conn = sqlite3.connect(data_file)
c = conn.cursor()

#    c.execute("CREATE TABLE tasks (taskindex int, download_status int, download_link text, image_caption text, image_web text)")



#t = (1,0,'http://www.google.com')
#c.execute("INSERT INTO tasks VALUES (?,?,?)",t)
#conn.commit()

c.execute("SELECT * from tasks")
y=c.fetchall()

max_to_download=10000
download_count=0

for row in y:
#    print(row)
#    if(row[1]==0):
    if(row[1]==0 and row[3]!="[Untitled]"):
        print(row[2])
	filename=str(row[0])
        urllib.urlretrieve(row[2], filename+".tif")
        print("downloaded",str(row[0]))
	os.system("convert "+filename+".tif "+filename+".jpg ; rm "+filename+".tif")
        t=(row[0],)

        c.execute("UPDATE tasks SET download_status=1 where taskindex=?",t)
        conn.commit()
        download_count=download_count+1
	if download_count > max_to_download-1:
		break

print("outside of loop")

#t=(1,)
#y=c.execute("UPDATE tasks SET download_status=1 where taskindex=?",t)
#conn.commit()

#y=c.execute("SELECT * from tasks")
#for row in y:
#    print(row)




conn.commit()
conn.close()
