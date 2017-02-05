from py_ms_cognitive import PyMsCognitiveWebSearch

class BingSearch:

    def __init__(self, api_key = '9e995ecf81ca452594cf19193d1552ef', num_of_urls = 3):
        self.api_key = api_key
        self.num_of_urls = num_of_urls

    def get_urls(self, search_term):
        '''
        Return the urls from search results of Bing
        '''
        url_list = []
        lst = self.search(search_term)
        for elem in lst:
            url_list.append(elem)
        # lst = self.search('customer base of ' + search_term)
        # for elem in lst:
        #     url_list.append(elem)
        # lst = self.search('manufacturing units of ' + search_term)
        # for elem in lst:
            # url_list.append(elem)
        return url_list

    def search(self, search_term):
        '''
        Search a particular term on Bing
        '''
        try:
            search_service = PyMsCognitiveWebSearch(self.api_key, search_term)
        except Exception as e:
            print e
            return None
        results =  search_service.search(limit= self.num_of_urls, format='json')
        lst = []
        for elem in results:
            lst.append(elem.display_url)
        return lst