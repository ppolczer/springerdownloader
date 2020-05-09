# Springer Downloader
Springer currently offers free access to a range of essential textbooks from all disciplines:
https://www.springernature.com/de/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960

This simple Python script downloads all available books based on the lists provided by the
website above. The lists have been provided in an excel format, URLs have been copied from 
these files into text files for easier handling.

### Usage
The script takes a command line argument to specify the directory to which the books should 
be downloaded to.
```
python springerdownloader.py --ddir path/to/download/dir
```