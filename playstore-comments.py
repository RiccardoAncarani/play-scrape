import requests
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud
from optparse import OptionParser
from matplotlib.cbook import dedent
import json

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
    stars = re.findall("Valutato con (.*?) stelle su cinque" ,r.text)
    x = []
    tmp = []
    [x.append(y) for (a,y,b) in revs]
    for i,rev in enumerate(x):
        tmp.append({"rating":int(stars[i]),"review":rev[25:-24].replace("span","")})
    print "[*] Retrieved " + str(len(tmp)) + " reviews"
    return tmp

def getNPages(id,n):
    s = []
    [[s.append(x) for x in getGooglePlayReviews(id,i)] for i in range(n)]
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
__________.__                   _________                                  
\______   \  | _____  ___.__.  /   _____/ ________________  ______   ____  
 |     ___/  | \__  \<   |  |  \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \ 
 |    |   |  |__/ __ \\___  |  /        \  \___|  | \// __ \|  |_> >  ___/ 
 |____|   |____(____  / ____| /_______  /\___  >__|  (____  /   __/ \___  >
                    \/\/              \/     \/           \/|__|        \/ 
                    Author Ancarani Riccardo"""
    print banner

def main():
    banner()
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-p", "--pages",
                      action="store", 
                      dest="pages",
                      default=5,
                      help="The number of pages you want to scrape",)
    parser.add_option("-i", "--id",
                      action="store", 
                      dest="app_id",
                      default="com.facebook.katana",
                      help="The id of the app you want to scrape comments",)
    parser.add_option("-o", "--output",
                      action="store", 
                      dest="output",
                      default="output.json",
                      help="The output file where you want to dump results",)
    (options, args) = parser.parse_args()
    print "[*] Downloading the first " + str(options.pages) + " pages from: " + options.app_id
    s = getNPages(options.app_id,int(options.pages))
    with open(options.output,"w+") as output_file:
        json.dump({"results": s},output_file)
    

if __name__ == '__main__':
    main()
    