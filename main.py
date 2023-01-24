from ranking.search_engine import SearchEngine


test = SearchEngine()

print(test.search('Bienvenue site', request_all_tokens= False))