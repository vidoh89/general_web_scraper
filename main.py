"""
Building process for a webscrapper

step 1. Install the requests library

    -->(python -m pip install requests)<--

step 2. Import the request library

        -->(import requests)<--

step3. create a variable named base_url to save the get request for website access-->>
       This get request accesses the website needed.
       ( --> base_url = requests.get('https://oxylabs.io/')  <-- )

Test code. This will print out the dom object for the website's layout

    --> print(base_url.text)<--
    note:if done correctly ,dom object prints in terminal.

step 4.   Install BeautifulSoup

          -->(pip install beautifulsoup4)--<

step 5  Import beautifulsoup-(library used to parse HTML provided via requests library)

        -->(from bs4 import BeautifulSoup)<--

step 6. Find HTML element and use bs4 to parse it

        -->(soup = bs4(response.text,'html.parser'))<--

step 7. Find all HTML elements with a similar class name

        -->(
            blog_titles = soup.find_all('a',class_='ex_class_name')

            #loop through elements and print the results
            for title in blog_titles:
                print(title.text)


        )<--
step 8. Using the soup.select() mehtod to find elements by css classname
        -->(
        blog_titles = soup.select("a.css_classname")
        )<--
"""

import requests

from bs4 import BeautifulSoup


# base_url = requests.get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')
base_url2 = requests.get('https://oxylabs.io/blog')
bs4 = BeautifulSoup

soup = bs4(base_url2.text, 'html.parser')

linkTags = soup.link.parent.prettify()
titleTags = soup.find_all('p')

for paragraphs in titleTags:
    print(f"Here is your objects, {paragraphs}")
# blog_titles = soup.find_all('div', class_='edsl5ca1')
# blog_titles = soup.select('a.edsl5ca4')
# for title in blog_titles:
#     print(title.text)
# print(blog_titles)
# print(soup.title)
