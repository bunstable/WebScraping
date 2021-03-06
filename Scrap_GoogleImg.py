'''Tool for downloading pictures from Google image search'''

import json
from scraptools import getUrlContent, downloadRessource

def getImgSearchUrl(searchTerm, startPage=0):
    '''Creates a url for a google image search, the url points to a json response'''
    searchTerm = searchTerm.replace(' ','%20') #simple conversion
    return 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q={0}&start={1}'\
           .format(searchTerm, int(startPage)*4)

def getPics(subject, destPath='', nbPages=1, startPage=0):
    '''Downloads images on subject, to folder destPath'''
    for pageNb in xrange(startPage, startPage+nbPages):
        print 'Page', pageNb
        url = getImgSearchUrl(subject, pageNb)
        response = getUrlContent(url)
        if response:
            jsonInfo = json.loads(response)
            
            if jsonInfo and jsonInfo['responseData']:
                results = jsonInfo['responseData']['results']
                
                for res in results:
                    #print res['titleNoFormatting']
                    #print res['contentNoFormatting']
                    #print res['width'], res['height']
                    print res['url']
                    downloadRessource(res['url'], destPath)

if __name__ == '__main__':
    getPics('cat')
    getPics('dog')
    #getPics('cat', 'googleImgScrap/', 3)
