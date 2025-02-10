import scrapy
from scrapy_playwright.page import PageMethod


class UniqloSpider(scrapy.Spider):
    name = 'uniqlomb'

    def start_requests(self):
        yield scrapy.Request(
            url = "https://www.uniqlo.com/fr/fr/men/bottoms",
            meta=dict(
                playwright=True,
                playwright_include_page = True,
                playwright_page_methods =[
                    PageMethod('wait_for_selector', '.fr-ec-product-tile-resize-wrapper')]
                ),
        )

    def parse(self, response):

        for art in response.css(".fr-ec-product-tile-resize-wrapper"):
            
            name = art.css(".fr-ec-title::text").get()
            price_text = art.css(".fr-ec-price-text::text").get()
            link = art.css(".fr-ec-tile::attr(href)").get()
            rate_text = art.css(".fr-ec-rating-average-product-tile::text").get()
            image = art.css(".fr-ec-image::attr(style)").re_first(r'url\("([^"]+)"\)')
            # Convertir les champs price et rate en float
            price = float(price_text.replace('€', '').replace(',', '.').strip()) if price_text else None
            rate = float(rate_text.strip()) if rate_text else None

            yield {
                'name': name,
                'price': price,
                'link': link,
                'rate': rate,
                'image': image,
                'type': "bottom",
                'sexe': "men"
            }
