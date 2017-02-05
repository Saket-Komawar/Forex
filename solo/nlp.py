import pickle

import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
nltk.data.path.append('./solo/nltk_data')


def main(text, path):
    entityList = createEntityList(text)
    
    #get trie object of countries and cities
    countryList = getObjectFromFile( './solo/countries.pkl')
    cityList = getObjectFromFile(  './solo/cities.pkl')
        
    countryCount = findKeywordCount(entityList, countryList)
    cityCount = findKeywordCount(entityList, cityList)
    importCount = text.count('import')
    exportCount = text.count('export')
    keywordCount = text.count('foreign exchange')
    keywordCount += text.count('currency exchange')

    '''
    features = dict()
    features['countryCount'] = countryCount
    features['cityCount'] = cityCount
    features['importCount'] = importCount
    features['exportCount'] = exportCount
    features['keywordCount'] = keywordCount
    '''
    features = list()
    features.append(str(countryCount))
    features.append(str(cityCount))
    features.append(str(importCount))
    features.append(str(exportCount))
    features.append(str(keywordCount))

    return features

# create entityList from string using nltk module
def createEntityList(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    entityList = []
    current_chunk = []
    for i in chunked:
         if type(i) == Tree:
                 current_chunk.append(" ".join([token for token, pos in i.leaves()]))
         elif current_chunk:
                 named_entity = " ".join(current_chunk)
                 if named_entity not in entityList:
                         entityList.append(named_entity)
                         current_chunk = []
         else:
                 continue
    return entityList    


#reload object from file containing  list
def getObjectFromFile(fileName):
    File = open(fileName, 'rb')
    Object = pickle.load(File)
    File.close()
    return Object

def findKeywordCount(entityList, keywordList):
    _end = '_end_'
    keywordCount = 0
    for word in entityList:
        current_dict = keywordList
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:    
                break
        else:
            if _end in current_dict:
                print word
                keywordCount += 1
    return keywordCount


if __name__ == '__main__':
    main()









