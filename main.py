import time
import link_scraper
import news_scraper

delay = 21600  # in seconds

sports_page = ['https://www.thedailystar.net/sports',
                'https://www.daily-sun.com/online/sports', 'https://www.bbc.com/sport']
entertainment_page = ['https://www.thedailystar.net/entertainment',
                        'https://www.daily-sun.com/online/entertainment', 'https://www.bbc.com/culture']
bd_and_world_top_page = ['https://www.thedailystar.net/news/bangladesh',
                'https://www.daily-sun.com/online/national', 'https://www.bbc.com/news/world']
pages = [bd_and_world_top_page, entertainment_page, sports_page]

while True:
    for i in range(3):
        for j in range(3):
            if j == 0:
                link_scraper.scrape(pages[i][j], site='star', topic=i)
            elif j == 1:
                link_scraper.scrape(pages[i][j], site='sun', topic=i)
            else:
                link_scraper.scrape(pages[i][j], site='bbc', topic=i)

    time.sleep(delay)
