import MySQLdb
import urllib
import urllib2
from bs4 import BeautifulSoup

#open search result for viewing
#import webbrowser

keyword = 'machine'


db = MySQLdb.connect("localhost","root","awi421","mydb")

cursor = db.cursor()

search = urllib.urlencode({'item':keyword})

url = 'http://139.59.1.147/search-courses/'
full_url = url + '?' + search
response = urllib2.urlopen(full_url)


with open("search-page.html","w") as f:
    data = response.read()
    f.write(data)

soup = BeautifulSoup(data, "html.parser")
results = soup.find_all("h4")

for result in results:
    print result.text
    link = None
    alink = result.parent.find('a', href=True)
    if alink:
       link = alink["href"]

    sql = """INSERT INTO linkinfo (linkname, linkurl ,search)
             VALUES ('%s','%s','%s')""" %( result.text, link, keyword)
    print '\n'
    cursor.execute(sql)

db.commit()

db.close()
