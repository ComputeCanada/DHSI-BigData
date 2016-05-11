
The goal of this exercise is to go through a whole workflow of an example big data DH: scraping the web for data, downloading the data, putting the data in appropriate storage, analysing it, and presenting the results in human accessible format.  In this example, the data will be a set of old photographs, and the analysis will consist of trying to identify images which contain objects with text in them, such as advertising billboards and street signs.

You can work through the exercise at your own pace.  The instructors are available to help you and will answer your questions.  If any of the steps are beyond your current capabilities, please let the instructors know and we will provide tools which can help you proceed further.
 
# Dataset

The dataset we will look at will the Farm Security Administration/Office of War Information (FSA-OWI) photographs archived on the Library of Congress website (http://www.loc.gov/pictures/collection/fsa/). The photographs were taken in the 1930s and 1940s, during the Great Depression and World War II.  This massive collection contains over 170,000 images, documenting all aspects of life in the United States in those years.  One of the most iconic photographs taken during the Depression , ["Migrant Mother"](http://www.loc.gov/pictures/collection/fsa/item/fsa1998021539/PP/) is a part of this collection.

One of the key benefits of using this dataset is that all the photographs are in the Public Domain, since they were made by employees of the US government.

However, the documentation of the collection is incomplete .  69,000 of the photographs are untitled, and for some of these no information at all is available.  Even for photographs containing accopanying information, the title and caption might not fully indicate the interesting aspects of a photograph. For example:


The goal for this exercise is to analyse the untitled photographs in the collection and identify those which contain text.  The text can then be used to deduce more information about the photograph. For example:



# Scraping the web

The Library of Congress website provides a search interface to its collection.  However, this search interface has not been updated for over a decade and, while very useful, does not provide all the functionality that the researcher might need.  For example, while the search can be limited to return only images which are digitized, it cannot be set to return only images which have been digitized in high resolution.  The images available only in low resolution  which are returned are usually not useful for analysis, and we want to modify our search process so that they are discarded.  
Also, the search results are only availble in a webpage, and cannot be easily downloaded to a convenient dataset for further processing, so we need to write a program which can collect them to a convenient format for future use.

An example program for scraping the web which you can build on is [provided](/file). You should write a program that scans over successive pages of a search for a term, ("untitled" in this case)

`http://www.loc.gov/pictures/search/?q=untitled&fa=displayed%3Aanywhere&sp=1&co=fsa&st=grid`

`http://www.loc.gov/pictures/search/?q=untitled&fa=displayed%3Aanywhere&sp=2&co=fsa&st=grid`

`...`

`http://www.loc.gov/pictures/search/?q=untitled&fa=displayed%3Aanywhere&sp=696&co=fsa&st=grid`

and extracts the addresses of each of the 100 images in each page, for example:

`http://www.loc.gov/pictures/collection/fsa/item/fsa1997000003/PP/`

For each of these pages, you should analyze whether a high resolution TIFF version of the image is available. If it is, you want to save the image link and title.

The natural way to store this information would be a database.  A python example with the details of setting up and using a simple database is provided [here](/exampledatabase).

The HTML code of any web page can be extracted using urllib module of Python.  An example of using it is provided [here](/exampleurllib).  You can search the HTML text extracted using the string.find method, or regular expressions. 

# Downloading and storing the data

The scraping of the web should be separated from the downloading stage since the downloads may take a long time, and the downloading program may have to be run intermittently over an extended time period.

Take the existing database and add a field for indicating download status.  Then write a program which will download the files.  Apply a tranformation to .tiff files to reduce their size.  You may also want to rescale the resolution.  Can use imagemagick program for that.

Once the program is done, set it running to download a set of files.  If that is too time consuming, a previously prepared set of images is also available.

# Detecting text in image 
Detecting text in photographic images (as opposed to scans of pages with text) is still a developing field, and the problem is rather challenging.  The difficulty often lies in detecting that text is present somewhere in the image in the first place.

For this exercise we will use a standard OCR tool called Tesseract. This software is conveniently available in all commonly used distributions of Linux.  Applying it to photographs is not its typical use, but it works remarkably well for demonstration purposes.  In any future workflow one would use better tools as they become available.

First, try to detect text in a single [image](http://loc.gov/pictures/resource/fsa.8a04355/) (first download the [high resolution .tif version of the image](http://cdn.loc.gov/master/pnp/fsa/8a04000/8a04300/8a04355a.tif) ), for example:

`tesseract 8a04355a.tif out.txt`

The text reconized in the image is very clear and the program does a relatively good job in recognising it and producing understandable output, stored in file out.txt. 

Then try a more challenging [image](http://www.loc.gov/pictures/collection/fsa/item/fsa1997003919/PP/). Here no text is detected.  Try rotating the image slightly with imagemagick and see if detection improves.

 `convert 8a03931u.tif  -rotate 10 output_rotated10.JPG`

 `tesseract output_rotated10.JPG out.txt` 

At the end, write a script which tries to reliably detects text in image. You might want to try a few rotations of the image in your attempts.  Your script should count the characters in the output: once some threshold is exceeded, you can have some confidence that the photograph contains some text.

# Analysing the data 
Write a Spark script which will apply the image analysis script to all the files in your data set.  Add a field to the database indicate whether text has been detected in the image or not.  Run the script on the set of images you gathered to detect those which contain text.

# Presenting the data 

Organize the output in some useful way so that humans can easily scan through it.  Make a webpage with images containing text embedded, for example.  You might want to rescale some of the images in your database first.  An example html file containing the essential code for this is [here](/link).









