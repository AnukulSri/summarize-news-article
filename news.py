import nltk
from newspaper import Article


# nltk.download('punkt') is a Python command that is used to download the "punkt" dataset or resource from the Natural Language Toolkit (NLTK) library. 
# NLTK is a popular library in Python for working with human language data, including tasks like tokenization, parsing, and text classification.
# The "punkt" dataset in NLTK contains pre-trained models and data necessary for tokenization, which is the process of breaking down a text into individual words or tokens. 
# These pre-trained models can be used to tokenize text in various languages, making it easier to work with natural language data in your Python projects.

nltk.download('punkt')
url='https://indianexpress.com/article/technology/tech-news-technology/apple-event-2-things-wowed-us-8938618/'
article = Article(url)
article.download()
article.parse()
article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publish Date: {article.publish_date}')
print(f'Summary: {article.summary}')
