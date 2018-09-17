from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import requests

api = articleAPI('ac81039491bf4d86bbaf3184cf794b6d')

def parse_articles(articles):
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['url'] = i['web_url']
        news.append(dic)
    return(news)

def get_text_from_url(url):
    try:
      p = requests.get(url).content
      #print(p)
      soup = BeautifulSoup(p,'html.parser')
      paragraphs = soup.findAll("p")

      #text = []
      text = ''
      for p in paragraphs:
         #text += p.text
         #text = text.encode('ascii', 'ignore')
         text += p.get_text() + ' '
         #print(text)
      text = text.replace('\n',' ')
      text = text.replace('\t',' ')
      return text
    except:
      print("No Connection")

all_articles = []
c = 0
for i in range(0,6): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
    articles = api.search(q = 'trade',fq = {'source':['Reuters','AP', 'The New York Times']}, page = str(i))
    articles = parse_articles(articles)
    #all_articles = all_articles + articles
    allText = []
    for i in range(0,len(articles)):
        article1 = get_text_from_url(articles[i]['url'])
        
        with open('Business_'+str(c)+'.txt', 'w') as output:
          output.write(article1)
        c += 1
        allText.append(article1)

#print(allText)
#result_all = []
'''
for i in range(2013,2017):
    #print 'Processing' + str(i) + '...'
    result_year =  get_articles(str(i),'trump+russia')
    result_all = result_all + result_year
'''
#print(result_all)
