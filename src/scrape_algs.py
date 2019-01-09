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
    try:
        if line.string[0] in "RULDFBM":
            alg_line = line.string.replace("’", "\'" )
            turns = alg_line.split()
            turns_prime_changd = []
            for turn in turns:
                if turn.endswith("\'"):
                    turns_prime_changd.append(turn[:-1])
                else:
                    turns_prime_changd.append(turn +  "\'")
                    
            turns_prime_changd.reverse()
            reverse_alg = "".join(turns_prime_changd)        
            reverse_url = urllib.parse.quote(reverse_alg)
            
            url = "http://cube.crider.co.uk/visualcube.php?fmt=png&size=200&alg={}&sch=gowbryht".format(reverse_url)
            dst = "../data/oll{}.png".format(idx)
            try:
                download_image(url, dst)
                print("Generated: OLL{}".format(idx))
                idx += 1
                urls.append(url+"\n")
            except:
                print("Download Error. ", url)
    except:
        print("Nonetype Object...Passed.")

with open("../data/urls.txt", "w") as f:
    f.writelines(urls)
