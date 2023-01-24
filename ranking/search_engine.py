import json


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
        ,request_all_tokens = True
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
                    ranked_dict[website_id] += index_result[token][website_id]['count']
                else:
                    ranked_dict[website_id] = index_result[token][website_id]['count']
        if request_all_tokens :
            # On ne retient que les sites qui sont contiennent tous les tokens
            website_all_tokens = []
            for token in index_result:
                website_all_tokens.append([website_id for website_id in index_result[token]])
            website_all_tokens = set.intersection(*map(set,website_all_tokens))
            ranked_dict = {key: ranked_dict[key] for key in website_all_tokens}
        return(ranked_dict)
        