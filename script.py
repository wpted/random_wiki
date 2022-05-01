import requests
from bs4 import BeautifulSoup


def random_wiki_url():
    wiki_url = "https://en.wikipedia.org/w/api.php"
    payload = {
        "action": "query",
        "format": "json",
        "generator": "random",
        "prop": "info",
        "inprop": "url"
    }
    result = requests.get(url=wiki_url, params=payload)
    result.raise_for_status()
    random_page = result.json()["query"]["pages"]

    random_page_id = list(random_page.keys())[0]
    random_url = random_page[random_page_id]["fullurl"]

    return random_url


def get_content(url):
    result = requests.get(url=url)
    result.raise_for_status()
    content = result.text

    nc = BeautifulSoup(content, 'html.parser').text
    return nc


def main():

    url = random_wiki_url()
    print(f"{url=}")
    content = get_content(url)
    print(content)


if __name__ == "__main__":
    main()
