import wikipediaapi as wiki
import requests
from bs4 import BeautifulSoup


def main():
    # wiki_wiki = wiki.Wikipedia('en', extract_format=wiki.ExtractFormat.WIKI)
    # page_py = wiki_wiki.page('Python_(programming_language)')
    # print("Page - Exists: %s" % page_py.exists())
    # print(page_py.text)

    wiki_url = "https://peps.python.org/pep-0020/"
    result = requests.get(url=wiki_url)
    result.raise_for_status()

    soup = BeautifulSoup(result.text, 'html.parser').text
    print(soup)


if __name__ == "__main__":
    main()
