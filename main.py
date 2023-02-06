from ranking.search_engine import SearchEngine
import click




@click.command()
@click.option('--request', help='The request to search.')
@click.option('--request_all_tokens',  default= False, help='Require all the tokens of the request in the result.')
@click.option('--result_file',  default= 'results.json', help='The path of the result file to export.')
def search_export(request, request_all_tokens, result_file):
    search_engine = SearchEngine()
    result = search_engine.search(request, request_all_tokens= request_all_tokens)
    search_engine.export_result(ranked_dict = result, result_file= result_file)



if __name__ == '__main__':
    search_export()