from bs4 import BeautifulSoup
import requests
import re


class Scrapper:
    def __init__(self):
        pass

    def visible(self, element):
        try:
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title', 'div', 'input']:
                return False
            elif re.match('<!--.*-->', str(element)):
                return False
        except Exception as e:
            return False
        return True

    def scrap(self, url, scrap_limit):
        """
        Scrap the url given and return page text
        and maximum three links to other pages from that page
        """
        try:
            print  '"' + str(url) + '"'
            if url[:4] != 'http':
                url = 'http://' + url
            proxies = {
                'http':None,
                'htts':None
            }
            r = requests.get(url, proxies = proxies)
        except Exception as e:
            print e
            return None, None
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        texts = soup.findAll(text=True)
        visible_text = filter(self.visible, texts)

        i = 0
        links_list = []
        for link in soup.find_all('a'):
            if (i >= scrap_limit):
                break
            links_list.append(link.get('href'))
            i += 1
        return visible_text, links_list
