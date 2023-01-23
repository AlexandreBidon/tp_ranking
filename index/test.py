from urllib import request
from bs4 import BeautifulSoup

url_list = [
	"https://fr.wikipedia.org/wiki/Stargate",
	"https://www.grandir-nature.com/",
	"https://www.strategic-culture.org/"]

index = {}
count_documents = len(url_list)
count_errors = 0
count_tokens = 0

for i in range(count_documents):
    try:
        url = url_list[i]
        html = request.urlopen(url, timeout= 5).read().decode('utf8')
        html[:60]
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title')

        title_token = title.string.split(sep=' ')
        count_tokens += len(title_token)
        print(title_token) # Prints the tag string content
        for token in title_token:
            if token in index:
                index[token].append(i)
            else :
                index[token] = [i]
    except Exception as e:
        count_errors += 1 

print(count_documents)
print("tokens : ", count_tokens)
print("errors : ", count_errors)
print(index)

