import scrapy

class bookSpyder(scrapy.Spider):
    name = "book"
    start_urls = ["https://books.toscrape.com"]


    def parse(self, response):
        for books in response.css("li.col-xs-6.col-sm-4.col-md-3.col-lg-3 article.product_pod"):
            yield{
                "name": books.css("h3 a::attr(title)").get(),
                "price": books.css("div.product_price p.price_color::text").get().replace("£", ""),
                "link": books.css("h3 a::attr(href)").get()
            }

        next_page = response.css("div ul.pager li.next a").attrib["href"]

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)