import glob
import urllib.request
from bs4 import BeautifulSoup


def download_book(url, dir):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read().decode("utf-8"), features="html.parser")
    download_button = soup.find("a", attrs={"data-track-action": "Book download - pdf"})
    title = soup.find("div", attrs={"class": "page-title", "data-test": True}).find("h1").get_text()
    print("Downloading '" + title + "' from " + url)
    urllib.request.urlretrieve("https://link.springer.com" + download_button.get("href"),
                               dir + "/" + title.replace(" ", "_") + ".pdf")


def main(ddir):
    import os
    if not os.path.exists(ddir):
        os.makedirs(ddir)
    for file in glob.glob("book_urls/*.txt"):
        with open(file) as url_list:
            for line in url_list.readlines():
                download_book(line, ddir)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Download free springer books")
    parser.add_argument('--ddir', metavar='path', required=True,
                        help='The directory where the books should be downloaded to')
    args = parser.parse_args()
    main(args.ddir)
