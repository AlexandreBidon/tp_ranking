from urllib import request
from bs4 import BeautifulSoup

class Index():

    def __init__(self, data_path : str, timeout : int, print_progress = False) -> None:
        self.url_list = self.__import_data(data_path = data_path)
        self.count_documents = len(self.url_list)
        self.count_tokens = 0
        self.count_errors = 0
        self.index = {}
        self.__tokenize_title(timeout = timeout, print_progress = print)

    def __tokenize_title(self, timeout : int, print_progress = False):
        for i in range(self.count_documents):
            if print_progress:
                print(f"Document actuellement indexé : {i + 1}/{self.count_documents}")
            try:
                url = self.url_list[i]
                html = request.urlopen(url, timeout= timeout).read().decode('utf8')
                html[:60]
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.find('title')

                title_token = title.string.split(sep=' ')
                self.count_tokens += len(title_token)
                for token in title_token:
                    if token in self.index:
                        self.index[token].append(i)
                    else :
                        self.index[token] = [i]
            except Exception as e:
                self.count_errors += 1 

    def __import_data(self, data_path : str):
        # TODO : import JSON
        url_list = [
            "https://fr.wikipedia.org/wiki/Stargate",
            "https://www.grandir-nature.com/",
            "https://www.strategic-culture.org/"]
        return(url_list)

    def __str__(self):
        return f"--- STATISTIQUES ---\nNombre de documents : {self.count_documents}\nNombre d'erreurs lors de l'indexage : {self.count_errors}\nNombre de tokens : {self.count_tokens}"