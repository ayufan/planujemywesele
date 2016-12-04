import scrapy

class PlanujemyWesele(scrapy.Spider):
    name = 'planujemywesele'
    start_urls = ['https://www.planujemywesele.pl/katalog/1/kategoria/zespol-weselny/miasto/tomaszow-lubelski,740/cena/3500,7000/liczba-osob/3,7/gatunki-muzyczne/disco']

    def parse(self, response):
        for tile in response.css('section.firm-tile'):
            href = tile.css('div.logo-ar > a ::attr(href)').extract_first()
            if href:
                yield scrapy.Request(response.urljoin(href), callback=self.parse_details)

        next_page = response.css('div.pagination > a[rel=next] ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_details(self, response):
        name = response.css('div.presentation > h2 ::text').extract_first()
        motto = response.css('div.presentation > h5 ::text').extract_first()
        desc = response.css('div.firm-description > div > p').extract_first()
        tel = response.css('a.phone ::attr(data-original-href)').extract_first()
        www = response.css('a.track_website_click ::attr(href)').extract_first()
        social = response.css('a.social-site ::attr(href)').extract_first()
        city = response.css('div.presentation > div.recommendations-align > div.margin-lg-top').css('a::text').extract_first()
        regions = response.css('div.regions > div.ellipsis-content > a.link::text').extract()

        yield { 'page': response.url, 'title': name, 'motto': motto, 'tel': tel, 'www': www, 'social': social, 'city': city, 'regions': regions }
