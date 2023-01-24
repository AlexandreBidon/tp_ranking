import json
import utils

class SearchEngine():

    def __init__(
        self
        ,documents_path = 'raw_data/documents.json'
        ,index_path = 'raw_data/index.json'
        ):
        self.index_dict = json.load(open(index_path))
        self.documents_dict = json.load(open(documents_path))

    def search(
        self
        ,request : str
        ,request_type = 'AND' # AND OR
        ):
        # On tokenise la requete
        request_tokens = request.lower().split(' ')
        index_result = {}
        for token in request_tokens:
            if token in self.index_dict:
                index_result[token] = self.index_dict[token]
            else :
                if request_type == 'AND':
                    # Aucun site ne contient tous les tokens
                    return None
        # On classe les sites en fonction du nombre de token dans le titre
        ranked_dict = {}
        for token in index_result:
            for website_id in index_result[token]:
                if website_id in ranked_dict:
                    ranked_dict[website_id] += index_result[token]['count']
                else:
                    ranked_dict[website_id] = index_result[token]['count']

        # On construit le ranking en fonction du type de requete
        if request_type == 'OR':
            # Si requete OU, on retourne directement le ranking construit
            return(ranked_dict)
        elif request_type == 'AND':
            #
            pass
        print(index_result)
        