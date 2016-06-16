import re
# good page to work with
# http://www.loc.gov/pictures/search/?q=untitled&sp=17&co=fsa&st=grid
# untitled images, some have text
# http://www.loc.gov/pictures/search/?q=untitled&fa=displayed%3Aanywhere&sp=1&co=fsa&st=grid
# with "larger image available everywhere" option

# seems there is a universal search interface
# http://www.loc.gov/pictures/search/?q=buffalo&fa=displayed%3Aanywhere&sp=1&co=fsa&st=grid
# this will show only digitized images available elsewhere
# still need to check image size

#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import urllib
import os.path
import sqlite3
import io

def getpage(urladdress):

    try:
        sock = urllib.urlopen(urladdress)
        htmlSource = sock.read()
        sock.close()
    except:
        print("error obtaining URL, returning empty source")
        htmlSource=""

    return htmlSource

def process_single_page(add,conn):
    c = conn.cursor()
    doc = getpage(add)  
    index=int(add[51:61]) # integer to identify image

    soup = BeautifulSoup(''.join(doc),"lxml")

    atags= soup.findAll('a') # "returns list of all tags <a> ... </a>
    numb=0.0
    for atag in atags: # loop over all tags
        mys=atag.string
        if mys != None: # exclude tags with no string 
            m = re.search('TIFF \((.+?)mb\)', mys) 
            if m != None:
                numb=float(m.group(1))
                download_location="http:"+atag["href"] # http address for TIFF image
                break # stop searching tags once we found the one with TIFF image

    if(numb>5.0): # only look for files greater than specified size

        filetitle=soup.title.string.strip() # extracts title tag content from html, which is title of photo
        image_caption=filetitle.replace(" ","_").strip(")") # replaces spaces with underscores, strips bracket (why?)
        loc_code=download_location[-12:-5] # extract ID code

# update database

        update=(index,0,download_location,image_caption,add)
        print(update)
        c.execute("INSERT INTO tasks VALUES (?,?,?,?,?)",update)
        conn.commit()

# begin main


# --------------------------
# main
# --------------------------

data_file='example.db'
if(os.path.isfile(data_file) ):
    print("found existing data file")
    conn = sqlite3.connect(data_file)
    c = conn.cursor()
else:
    print("creating new database file")
    conn = sqlite3.connect(data_file)
    c = conn.cursor()
    c.execute("CREATE TABLE tasks (taskindex int, download_status int, download_link text, image_caption text, image_web text)")
    conn.commit()


nstart=1  
#nend=696 # actual end
nend=2 # short for testing


for itr in range(nstart,nend+1):
    searchpage="http://www.loc.gov/pictures/search/?q=untitled&fa=displayed%3Aanywhere&sp="+str(itr)+"&co=fsa&st=grid"
    print("processing: ",searchpage)

    doc11=getpage(searchpage)
    soup = BeautifulSoup(''.join(doc11),"lxml")

    tdtags= soup.findAll('td') # "returns list of all tags <td> ... </td>

    for tdtag in tdtags:
        atags=tdtag.findAll('a')
        for atag in atags:
            individual_image_page="http:"+atag["href"] 
            print(individual_image_page)
            process_single_page(individual_image_page,conn) 

