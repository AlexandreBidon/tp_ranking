from index.index import Index

if __name__ == "__main__":

    print(
        Index(
            import_data_path="raw_data/crawled_urls.json"
            ,export_index_path="test"
            ,timeout=3
            ,print_progress= True))