import scrapy


class ShopcluesSpider(scrapy.Spider):
    name = 'shopclues'
    allowed_domains = ['www.shopclues.com/mobiles-smartphones.html']
    start_urls = ['https://www.shopclues.com/mobiles-smartphones.html']
    custom_settings = {
       'FEED_URI' : 'tmp/shopclues.csv'
   }

    def parse(self, response):
        titles = response.css('img::attr(title)').extract()
        images = response.css('img::attr(data-img)').extract()
        prices = response.css('.p_price::text').extract()
        discounts = response.css('.prd_discount::text').extract()

        for item in zip(titles,prices,images,discounts):
            scrapped_info = {
                'title' : item[0],
                'price' : item[1],
                'image_urls' : [(item[2])],
                'discount' : item[3]
            }
            yield scrapped_info