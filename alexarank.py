#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys


class AlexaRank:

    def parser(url):
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def cleaner(text):
        clean = text.replace("#", "")
        clean = clean.replace("\n", "")
        clean = clean.replace(" ", "")
        return clean

    def removewww(domain):
        name = domain.replace("http://", "")
        name = name.replace("https://", "")
        name = name.replace("www.", "")
        return name

    def globalrank(url):
        soup = AlexaRank.parser(url)
        text = soup.find("p", class_="big data").get_text()
        rank = AlexaRank.cleaner(text)
        return rank

    def countryrank(url):
        soup = AlexaRank.parser(url)
        soup = soup.find("div", id="CountryRank")
        soup = soup.find("li", )
        text = soup.find("span", class_="pull-right").get_text()
        rank = AlexaRank.cleaner(text)
        return rank


if __name__ == '__main__':
    try:
        domain = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <domain_url>")
    if (domain == '-h') | (domain == '--help'):
        print(f'Alexa Rank Checker\nUsage: {sys.argv[0]} <domain_url>\nOptions:\n‑h, ‑‑help            show this help message and exit')
    else:
        domain = AlexaRank.removewww(domain)
        url = "https://www.alexa.com/siteinfo/" + domain
        try:
            print(AlexaRank.globalrank(url))
            print(AlexaRank.countryrank(url))
        except AttributeError:
            pass
