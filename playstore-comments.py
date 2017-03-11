import requests
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud

def getGooglePlayReviews(page):
    headers = {
        
        "CONSENT":"YES+IT.it+20160117-18-0",
        
    }

    data = {
        "reviewType": 0,
        "pageNum" :page,
        "id":"com.facebook.katana",
        "reviewSortOrder":4,
        "xhr": 1,
        "token": "WZoOkfYty7v0H9yjvbZZ1pPDe5Q%3A1486642693855",
        "hl":"it"
    }
    r = requests.post("https://play.google.com/store/getreviews?authuser=0", headers=headers, data=data)
    revs = re.findall("(review-title)(.*?)(review-link)",r.text)
    x = []
    [x.append(y) for (a,y,b) in revs]
    return x

def getNPages(n):
    s = []
    [[s.append(x) for x in getGooglePlayReviews(i)] for i in range(1,n)]
    s = [x[25:-24] for x in s]
    return s

s = getNPages(5)
stop = set(stopwords.words('italian'))
final_list = [" ".join([i for i in x.lower().split() if i not in stop]) for x in s]
def showWordCloud(wordcloud):
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

wordcloud = WordCloud().generate(" ".join(final_list))
showWordCloud(wordcloud)