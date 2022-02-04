# Mission to Mars Challenge

## Overview of Project
The challenge involved web scraping, i.e. a method of gaining data from different sources quickly instead of visiting 
each website yourself and then manually extracting the data. I used Chrome Developer Tools to identify the HTML components 
attached to the required data. I also used BeautifulSoup and Splinter to automate a web browser and gather the required 
data. The web scraping process is automated, using a programming script. I then stored the data in MongoDB, a NoSQL 
database. That means that it can handle data that isn’t as structured. To display it, I created a web application using 
Flask. My code can be found in “Mission_to_Mars_Challenge.ipynb,” “scraping.py,” “app.py,” and “index.html.” </p>

## Project Steps
The first step is understanding how a webpage is built. Every webpage is put together using a combination of HTML, CSS
 and other libraries. Once the structure of a webpage is more familiar, the next step is to write a Python script that
 uses BeautifulSoup and Splinter. BeautifulSoup will extract data needed for analysis and then I stored it in MongoDB. 
 Finally, I  used a web application using Flask. This web application has a button that executes my scraping code and 
 then updates the pages to display the newest data.  </p>
## Summary
I completed a web scraping challenge, pulling required data from active web pages using Chrome Developer Tools and 
BeautifulSoup, storing the required data in MongoDB, and displaying the scraped data in a web application using Flask.
