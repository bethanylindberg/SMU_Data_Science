from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "C:\\Users\\bethf\\Desktop\\chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape_data():
    browser = init_browser()

    # Visit NASA
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "lxml")

    # Scrape data
    article = soup.find_all(class_="content_title")[0].text.strip()
    news_p = soup.find_all(class_="article_teaser_body")[0].text.strip()
    relativearticleurl = soup.find_all("a")[35]["href"]
    articleurl = 'https://mars.nasa.gov' + relativearticleurl
    relative_image_path = soup.find_all('img')[2]['src']
    nasa_img = 'https://mars.nasa.gov' + relative_image_path
    
    # Visit NASA images
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "lxml")

    # Scrape data
    relative_image_path = soup.find_all('img')[3]['src']
    featured_image_url = 'https://jpl.nasa.gov' + relative_image_path
    
    #Visit Mars Weather
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "lxml")
    
    # Scrape data
    mars_weather = soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[0].text.strip()
    
    #Visit Mars Facts
    url = "https://space-facts.com/mars/"

    #Scrape Table
    table = pd.read_html(url)[0]
    mars_facts = table.to_html(header=False,index=False)
    mars_facts = mars_facts.replace('\n','')
    mars_facts
    
    #Loop for Hemispheres
    hemispheres_list = []

    for num in range(0,4):
        hemispheres = {}
        
        #Visit Mars Astropedia
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        html = browser.html
        soup = bs(html, "lxml")
        
        #Click on hemisphere for full size image
        browser.find_by_css("h3")[num].click()

        html = browser.html
        soup = bs(html, "lxml")

        #Scrape data
        relative_path = soup.find('img',class_="wide-image")['src']
        img = 'https://astrogeology.usgs.gov' + relative_path
        title = soup.find('h2',class_="title").text.strip()

        #Append Data
        hemispheres["title"] = title
        hemispheres["img"] = img
        hemispheres_list.append(hemispheres)

        #Back to Mars Astropedia
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
    
    # Store data in a dictionary
    data = {
        "article": article,
        "articleurl": articleurl,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather":mars_weather,
        "marsfacts":mars_facts,
        "hemispheres_list":hemispheres_list
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return data  