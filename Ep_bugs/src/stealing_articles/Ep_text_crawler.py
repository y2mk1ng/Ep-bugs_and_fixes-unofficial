import requests
from bs4 import BeautifulSoup
sessionRequests = requests.session()
url = "https://episode.cc/read/seeking.for.myself/my.190226.002200/0"
result = sessionRequests.get(url)
soup = BeautifulSoup(result.text,"html.parser")
content = soup.find("meta", property = "og:description")['content']
content_string = str(content)
with open('bian.txt', 'w', encoding = 'UTF-8') as f:
    f.write(content_string)
    f.close()