import unittest
from ranking.search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

    def test_search(self):
        # GIVEN
        search_engine = SearchEngine()
        request = "Bienvenue site"

        # WHEN
        result = search_engine.search(request, request_all_tokens= False)

        #THEN
        self.assertEqual(
            result
            ,{'21': 2, '51': 1, '78': 1, '2': 1, '20': 1, '23': 1, '41': 1, '101': 1, '183': 1, '274': 1, '428': 1, '497': 1}
        )

    def test_search_2(self):
        # GIVEN
        search_engine = SearchEngine()
        request = "Bienvenue site"

        # WHEN
        result = search_engine.search(request, request_all_tokens= True)

        #THEN
        self.assertEqual(
            result
            ,{'21': 2}
        )

if __name__ == '__main__':
    unittest.main()