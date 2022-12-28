from bs4 import BeautifulSoup
import requests
import csv
import news_scraper
import time
from newspaper import Article
import save_news
delay = 10


def scrape_dstar(page_link, topic):
    source = requests.get(page_link).text
    soup = BeautifulSoup(source, 'lxml')

    if soup:
        print('ds page paisi')  # print(soup)

        # REMINDER
        # GOTTA FIND SOME OTHER FILE FORMAT TO SAVE TO, CSV WOULD CREATE PROBLEMS

    # csv_file = open("scraped.csv", "w",  encoding="utf-8")
    # csvWriter = csv.writer(csv_file)

    #All = [["name","time"]]
    link_list = []
    #link_list_iterator = 0

    for link in soup.find_all('a'):  # collecting the links
        if link.parent.name == 'h3':
            # print(link["href"])################################# bug here
            link_list.append('https://www.thedailystar.net' + link["href"])

    topics = {
        0: 1,
        1: 3,
        2: 2
    }
    # for i in range(5):
    #     print(link_list[i])

    for i in range(2):
        news_scraper.scrape(link_list[i], topics[topic])

        time.sleep(delay)


def scrape_dsun(page_link, topic):
    source = requests.get(page_link).text
    soup = BeautifulSoup(source, 'lxml')

    if soup:
        print('bdn page paisi')  # print(soup)

        # REMINDER
        # GOTTA FIND SOME OTHER FILE FORMAT TO SAVE TO, CSV WOULD CREATE PROBLEMS

    # csv_file = open("scraped.csv", "w",  encoding="utf-8")
    # csvWriter = csv.writer(csv_file)

    #All = [["name","time"]]
    link_list = []
    #link_list_iterator = 0

    # print(soup.body.div[3].div.div.div[2].main.div.div[2].div.div[3].div.div.div.div[3].div.div[2].h3.a)
    for link in soup.find_all('a', {"class": "news"}):  # collecting the links
        # if link['class'] == 'news':
        print(link["href"])  # bug here
        link_list.append('https://www.daily-sun.com/' + link["href"])

    #print(f'the list {link_list}')
    topics = {
        0: 1,
        1: 3,
        2: 2
    }
    for i in range(2):
        print(link_list[i])

    for i in range(2):
        news_scraper.scrape(link_list[i], topics[topic])

    time.sleep(delay)


def scrape_bbc(page_link, topic):
    source = requests.get(page_link).text
    soup = BeautifulSoup(source, 'lxml')

    if soup:
        print('ds page paisi')  # print(soup)
    link_list = []
    #link_list_iterator = 0

    if page_link == 'https://www.bbc.com/news/world':
        for a in soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}):
            print("Found URL:", a['href'])
            link_list.append('https://www.bbc.com' + a["href"])

    elif page_link == 'https://www.bbc.com/sport':
        for a in soup.find_all('a', {"class": "ssrcss-1j8184x-PromoLink e1f5wbog0"}):
            print("Found URL:", a['href'])
            link_list.append('https://www.bbc.com' + a["href"])

    elif page_link == 'https://www.bbc.com/culture':
        for a in soup.find_all('a', {"class": "rectangle-story-item__title"}):
            print("Found URL:", a['href'])
            link_list.append('https://www.bbc.com' + a["href"])

    topics = {
        0: 1,
        1: 3,
        2: 2
    }


    for i in range(2):
        news_scraper.scrape(link_list[i], topics[topic])
        time.sleep(delay)

def scrape(link,site, topic):
    if site == 'star':
        scrape_dstar(link, topic)
    elif site == 'sun':
        scrape_dsun(link, topic)
    else:
        scrape_bbc(link, topic)



# page_link = 'https://www.bbc.com/news'  #actual link
# scrape_bbc(page_link, 2)

