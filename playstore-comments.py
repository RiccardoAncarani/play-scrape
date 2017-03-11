import requests
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud
from optparse import OptionParser
from matplotlib.cbook import dedent

def getGooglePlayReviews(id,page):
    headers = {        
        "CONSENT":"YES+IT.it+20160117-18-0",
        }

    data = {
        "reviewType": 0,
        "pageNum" :page,
        "id":id,
        "reviewSortOrder":4,
        "xhr": 1,        
        "hl":"it"
    }
    r = requests.post("https://play.google.com/store/getreviews?authuser=0", headers=headers, data=data)
    revs = re.findall("(review-title)(.*?)(review-link)",r.text)
    x = []
    [x.append(y) for (a,y,b) in revs]
    return x

def getNPages(id,n):
    s = []
    [[s.append(x) for x in getGooglePlayReviews(id,i)] for i in range(1,n)]
    s = [x[25:-24] for x in s]
    return s




def showWordCloud(wordcloud):
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def processAndPlot(s):
    stop = set(stopwords.words('italian'))
    final_list = [" ".join([i for i in x.lower().split() if i not in stop]) for x in s]
    showCloudFromList(final_list)

def showCloudFromList(final_list):
    wordcloud = WordCloud().generate(" ".join(final_list))
    showWordCloud(wordcloud)


def banner():
    banner = """
    __________.__                   _________ __                        
\______   \  | _____  ___.__.  /   _____//  |_  ___________   ____  
 |     ___/  | \__  \<   |  |  \_____  \\   __\/  _ \_  __ \_/ __ \ 
 |    |   |  |__/ __ \\___  |  /        \|  | (  <_> )  | \/\  ___/ 
 |____|   |____(____  / ____| /_______  /|__|  \____/|__|    \___  >
                    \/\/              \/                         \/ """
    print banner

def main():
    banner()
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-p", "--pages",
                      action="store", # optional because action defaults to "store"
                      dest="pages",
                      default=5,
                      help="The number of pages you want to scrape",)
    parser.add_option("-i", "--id",
                      action="store", # optional because action defaults to "store"
                      dest="app_id",
                      default="com.facebook.katana",
                      help="The id of the app you want to scrape comments",)
    (options, args) = parser.parse_args()
    s = getNPages(options.app_id,int(options.pages))
    print s

if __name__ == '__main__':
    main()
    