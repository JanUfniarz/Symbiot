import scrapy
from urllib.parse import urljoin

class GitHubTopicsSpider(scrapy.Spider):
    name = 'github_topics'
    start_urls = ['https://github.com/topics/pretrained-models']  # Replace this with the actual URL

    def parse(self, response):
        base_url = response.url  # Get the base URL of the page

        # Extract all text and corresponding links from the HTML
        texts_and_links = []

        for element in response.css('body *'):
            text = ' '.join(element.css('::text').extract())
            relative_link = element.css('::attr(href)').extract_first()

            if text and relative_link:
                absolute_link = urljoin(base_url, relative_link)  # Convert to absolute URL
                texts_and_links.append({'text': text, 'link': absolute_link})

        # You can print or process the extracted data as needed
        for item in texts_and_links:
            print(f"Text: {item['text']}")
            print(f"Link: {item['link']}")
            print('-' * 50)

        # Optionally, you can save the data to a file
        with open('output.txt', 'w', encoding='utf-8') as f:
            for item in texts_and_links:
                f.write(f"Text: {item['text']}\n")
                f.write(f"Link: {item['link']}\n")
                f.write('-' * 50 + '\n')
