from newspaper import Article
import save_news, time
import nltk
import urllib.request
from save_image import save_img
# create an article object
def scrape(l, topic='bleh'):
    nltk.download('punkt')
    time.sleep(5)
    print(f'link------>{l}\ntype:{type(l)}')
    # link = 'https://www.thedailystar.net/' + link 
    # print(f'link------>{link}\ntype:{type(link)}')
    
    article = Article(l)
    article.download()
    article.parse()
    article.nlp()

    title = article.title
    link = article.url
    authors = article.authors
    date = article.publish_date
    text = article.text
    summary = article.summary
    image_link= article.top_image
    
    #urllib.request.urlretrieve(str(image_link), "local-filename.jpg")
    img_name = save_img(image_link)
    
    
    print("==================================================================================")
    print("==================================================================================")
    print("==================================================================================\nLINK AND ACTUAL NEWS:")
    print(link)
    print(text)
    print('***********************************************************************************\nSUMMARY:')
    print(image_link)
    print(summary)
    
    news = {
        'link' : link,
        'title': title,
        'author':authors,
        'date' : str(date),
        'news_text': text,
        'summary' : summary,
        'img' : img_name
    }
    
    save_news.save(news, topic)
    #print(news)
scrape('https://www.daily-sun.com/post/651316/Man-Utd-too-good-for-Tottenham-Liverpool-revival-rolls-on')
