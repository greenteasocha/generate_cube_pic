import urllib.request, urllib.parse
from bs4 import BeautifulSoup
from get_scrambled_pic import download_image

html = urllib.request.urlopen("http://tribox.com/3x3x3/solution/oll/")
#page_text = html.text.encode('utf-8').decode('ascii', 'ignore')
soup = BeautifulSoup(html)
print(soup.original_encoding)
a = soup.find_all("li")

print("START:\n")
urls = []
idx = 1
for line in a:
    print(line.string)
