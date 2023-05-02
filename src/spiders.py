import scrapy
from datetime import datetime, timedelta

class DecryptSpider(scrapy.Spider):
    name = 'decrypt'
    allowed_domains = ['decrypt.co']
    start_urls = ['https://decrypt.co/']

    def parse(self, response):
        # Filtro data
        n_days = 7 # Modificare il numero di giorni a seconda delle esigenze
        date_limit = datetime.now() - timedelta(days=n_days)

        # Imposta selectors
        article_selector = 'div.post-listing div.post-listing__row article.post-listing__item'
        article_url_selector = 'a.post-listing__title::attr(href)'
        article_date_selector = 'div.post-listing__date::text'

        # Ottieni l'URL dell'articolo
        for article in response.css(article_selector):            
            article_date_str = article.css(article_date_selector).get().strip()
            article_date = datetime.strptime(article_date_str, '%B %d, %Y')
            if article_date >= date_limit: #TODO Da verificare questa condizione
                article_url = article.css(article_url_selector).get()
                # Recupera info dell'articolo
                yield scrapy.Request(article_url, 
                                     callback=self.parse_article,
                                     meta={'article_date':article_date})

    def parse_article(self, response):
        title_selector: str
        content_selector: str
        image_url_selector: str
        date_selector: str
        title = response.css('h1.article-header__title::text').get()
        description = response.css('div.article-header__lead::text').get()
        image_url = response.css('div.article-header__cover img::attr(src)').get()
        yield {
            'title': title,
            'description': description,
            'image_url': image_url,
            'date': response.meta.get('article_date')
        }

