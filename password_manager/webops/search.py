import webbrowser
import googlesearch

class Website():
    def __init__(self,app_name) -> None:
        self.app_name = app_name

    def open(self): 
        search_query = f"{self.app_name} website"
        search_results = googlesearch.search(search_query, num_results=1)

        try:
            if search_results:
                url = next(search_results)
                webbrowser.open(url)
            else:
                pass
        except Exception as error:
            print(error)

