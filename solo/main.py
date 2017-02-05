import bing_search
import scrapper
import nlp
import test_ml

class Logic:

    def __init__(self):
        pass

    def process(self, company_name, isIEC, path):

        search_engine = bing_search.BingSearch()
        a = search_engine.get_urls(company_name)
        url_list = a
        text_list = []
        my_scrapper = scrapper.Scrapper()
        """url = url_list.pop()
        text,urls = my_scrapper.scrap(url, 5)
        if urls is not None:
            a = set(urls)
        for elem in a:
            if elem is not None:
                url_list.add(elem)
        if text is not None:
            for elem in text:
                if elem is not None:
                    text_list.append(elem)
        """
        #print 'Length of url list', len(url_list)
        for url in url_list:
            text = my_scrapper.scrap(url, 0)
            for elem in text:
                text_list.append(elem)

        #Get features from NLP module
        string = ''
        for elem in text_list:
            if isinstance(elem, list):
                for value in elem:
                    text_list.append(value)
                continue
            if elem is None:
                continue
            string += elem
        features = nlp.main(string, path)

        #Check for IEC number here
        if(isIEC):
        	features.append(1)
        else:
        	features.append(0)

        self.write_to_csv(features,  './solo/tmp.csv')

        #TODO Call the xgboost model here
        #score = test_ml.get_prediction( './solo/tmp.csv', path)
        score = test_ml.get_prediction( features, path)
        return score,features,url_list[:3]
        

    def write_to_csv(self, features, filename):
        try:
            f = open(filename, 'w')
            first_flag = True
            for key in features:
                if first_flag:
                    first_flag = False
                else:
                    f.write(',')
                f.write(str(key))
            f.write('\n')
            f.close()
        except IOError as e:
            print 'Error in writing features to file'

    def write_to_file(self, text_list):
        f = open('text.txt', 'w')
        try:
            text_list.remove('\n')
        except Exception as e:
            pass
        for elem in text_list:
            try:
                if isinstance(elem, list):
                    for value in elem:
                        text_list.append(value)
                    try:
                        text_list.remove('\n')
                    except Exception as e:
                        pass
                    continue
                if elem.isspace():
                    continue
                try:
                    f.write(str(elem) + '\n')
                except Exception as e:
                    pass
            except Exception as e:
                print e
        f.close()


if __name__ == '__main__':
    obj = Logic()
    obj.process('persistent systems')
