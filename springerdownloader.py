import glob
import urllib.request
import re
from bs4 import BeautifulSoup
import os

special_characters = re.compile(r"[^0-9a-zA-Z_ÄÜÖäüö]")


def download_book(url, dir):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read().decode("utf-8"), features="html.parser")
    download_button = soup.find("a", attrs={"data-track-action": "Book download - pdf"})
    title = soup.find("div", attrs={"class": "page-title", "data-test": True}).find("h1").get_text()

    file_title = re.sub(special_characters, "_", title)
    file_path = os.path.join(dir, file_title+".pdf")
    if not os.path.exists(file_path):
        print("Downloading '" + title + "' from " + url)
        urllib.request.urlretrieve("https://link.springer.com" + download_button.get("href"),
                                   file_path)
    else:
        print(f"Book '{title}' already exists in '{dir}'.")


def main(ddir):
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
