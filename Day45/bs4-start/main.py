from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
article = soup.find_all('span' ,class_='titleline')
upvotes = soup.select(".subline > .score")

article_texts = [each_article.getText() for each_article in article]
article_links = [each_article.find("a").get("href") for each_article in article]
article_upvotes = [each_upvote.getText() for each_upvote in upvotes]
new_article_upvotes_number = [ int(each_digit_point.replace(" points","")) for each_digit_point in (article_upvotes)]


largest = max(new_article_upvotes_number)
largest_index = new_article_upvotes_number.index(largest)

print(f"The most Popular and most liked article today is:\n\nNews: {article_texts[largest_index]}\n\nnLink:  {article_links[largest_index]}")
