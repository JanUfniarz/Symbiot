import scrapy
from scrapy.crawler import CrawlerProcess

class GitHubSpider(scrapy.Spider):
    name = 'github_spider'
    start_urls = ['https://github.com/topics/pretrained-models']

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
    }

    def parse(self, response):
        # Znajdź linki do repozytoriów na stronie tematu
        repo_links = response.css('h3.f3 a::attr(href)').extract()

        for repo_link in repo_links:
            full_repo_link = response.urljoin(repo_link)
            yield scrapy.Request(full_repo_link, callback=self.parse_repo)

        # Znajdź link do następnej strony i przejdź do niej
        next_page = response.css('div.pagination a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_repo(self, response):
        # Zbierz informacje o repozytorium
        repo_name = response.css('h1 strong a::text').extract_first()
        repo_url = response.url
        repo_description = response.css('div.f4 span::text').extract_first()

        # Dodaj informacje do elementu wynikowego
        repo_data = {
            'Name': repo_name,
            'URL': repo_url,
            'Description': repo_description,
        }

        # Dodaj informacje ze strony repozytorium
        # Poniżej znajdują się przykładowe selektory CSS, dostosuj je do swoich potrzeb
        repo_data['Readme'] = response.css('div#readme article::text').extract_first()
        repo_data['Contributors'] = response.css('span.num::text').extract_first()

        yield repo_data

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(GitHubSpider)
    process.start()
