#!/Users/thor/opt/anaconda3/bin/python

from bs4 import BeautifulSoup

from datetime import datetime  

with open('source.html', 'r') as f:
    content=f.read()
    soup = BeautifulSoup(content)
    divTag2 = soup.find_all("div", {"class": "price"})
    divTag = soup.find_all("a", {"class": "product-item-link"})
    for tag in divTag:
        #myTag=tag.find('b')
        #myTag2=tag.find_all('h5')
        print(tag.text)
        #print(type(myTag2))
        #print("*** "+myTag2.text)
        #print((tag.find('b')).replace("<b>","**"))

    for tag in divTag2:
        print(tag.text)
        #myTag=tag.find('b')
        #print(type(myTag))
        #myTag3=tag.find_all('a')
        #for aTag in myTag3:
        #    aTag=btag.find_all('a')
            #print("**** "+aTag.text)
            #for aSingleTag in aTag:
            #    print(type(aSingleTag))
            #    print("kurt")
        #myTag2=tag.find_all('h5')
        #print("** "+myTag.text)
        #for htag in myTag2:
        #    print("*** "+htag.text)

        #print(type(myTag2))
        #print("*** "+myTag2.text)
        #print((tag.find('b')).replace("<b>","**"))
    '''
    for tag in divTag:
        myTag=tag.find('b')
        #print(type(myTag))
        myTag3=tag.find_all('a')
        myTag2=tag.find_all('h5')
        print("** "+myTag.text)
        for htag in myTag2:
            print("*** "+htag.text)

        #for aTag in myTag3:
        #    aTag=btag.find_all('a')
        #    print("**** "+aTag.text)
            #for aSingleTag in aTag:
            #    print(type(aSingleTag))
            #    print("kurt")
        #print(type(myTag2))
        #print("*** "+myTag2.text)
        #print((tag.find('b')).replace("<b>","**"))
    '''
