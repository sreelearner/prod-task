import csv
from urllib.request import urlopen
from html.parser import HTMLParser

class BookParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_price = False
        self.in_rating = False
        self.books = []
        self.current = {}
        self.rating_map = {
            'One': '1',
            'Two': '2',
            'Three': '3',
            'Four': '4',
            'Five': '5'
        }

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h3' and 'title' in attrs.get('class', ''):
            self.in_title = True
        elif tag == 'a' and 'title' in attrs:
            self.current['Title'] = attrs['title']
        elif tag == 'p' and 'price_color' in attrs.get('class', ''):
            self.in_price = True
        elif tag == 'p' and 'star-rating' in attrs.get('class', ''):
            class_list = attrs.get('class', '').split()
            for cls in class_list:
                if cls in self.rating_map:
                    self.current['Rating'] = self.rating_map[cls]

    def handle_data(self, data):
        if self.in_price:
            self.current['Price'] = data.strip()

    def handle_endtag(self, tag):
        if tag == 'p' and self.in_price:
            self.in_price = False
        elif tag == 'article':
            if self.current:
                self.books.append(self.current)
                self.current = {}

def fetch_page(url):
    with urlopen(url) as response:
        return response.read().decode('utf-8')

def main():
    url = "http://books.toscrape.com/catalogue/page-1.html"
    html = fetch_page(url)

    parser = BookParser()
    parser.feed(html)

    with open('books.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Rating"])
        writer.writeheader()
        writer.writerows(parser.books)

    print("Scraping completed. Data saved to books.csv")

if __name__ == "__main__":
    main()

