# 18) Write a Python program to extract year, month and date from an url


import re

def extract_date_from_url(url):
    date = re.findall(r"\d{4}/\d{2}/\d{2}",url)
    print(date)

extract_date_from_url("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
)
