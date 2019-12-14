from scrapy import Spider
from scrapy import Request
from analytics.items import AnalyticsItem
import re 
import math


class analyticsSpider(Spider):
    name = 'analytics_spider'
    allowed_domains = ['clutch.co']
    start_urls = ['https://clutch.co/it-services/analytics']

    def parse(self, response):
        # Find the total number of pages in the result so that we can decide how many urls to scrape next
        
        
        # n_pages = response.xpath('//li[@class="pager-current"]/text()').extract_first()
        # n_pages = re.findall('\d+',n_pages)[1]
        # n_pages = int(n_pages[0])

        # print(n_pages)
        print('=' * 50)
        
        # Find all result pages
        # result_urls = ['https://clutch.co/it-services/analytics?page={}'.format(x) for x in range(1, n_pages+1)]
        result_urls = ['https://clutch.co/it-services/analytics?page={}'.format(x) for x in range(1, 67)]
        #looping
        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page)       

    

    def parse_result_page(self, response):

        # This function parses the search result page.
        # Looking for url of the detail page.

        detail_urls = response.xpath('//div[@class="company-logo"]/a/@href').extract()
        print(len(detail_urls))
        print('=' * 50)
      
        # Yield the requests to the details pages, 
        # using parse_detail_page function to parse the response.

        for url in detail_urls:
                 
            yield Request(url= url, callback=self.parse_detail_page)

                                    ######This is the path to access for the company name from the 1st page
                                    #company_name = response.xpath('.//div//a[@target="_blank"]/text()').extract()


    def parse_detail_page(self, response):
    
        # Extract each field from the review tag
        company_name    = response.xpath('.//h1[@class="page-title"]/text()').extract()

        elements        = response.xpath('.//div[@class="col-xs-2-custom bordered-mobile-block"]/div/div/div/text()').extract()

        rating          = response.xpath('.//div[@class="provider-profile-rating-widget"]/span/text()').extract()

        location        = response.xpath('.//div[@class="field-location-name"]/span/text()').extract()

        #define parameters (unpacked "elements")
        min_project_size= elements[0]
        hourly_rate     = elements[1]
        employee        = elements[2]    
        founded_year    = elements[3]
        
        try:
            rating      = response.xpath('.//div[@class="provider-profile-rating-widget"]/span/text()').extract()
        except IndexError:
            rating      = ""


        item = AnalyticsItem()
        item['comapny_name']        = company_name
        item['min_project_size']    = min_project_size
        item['hourly_rate']         = hourly_rate
        item['employee']            = employee
        item['founded_year']        = founded_year
        item['location']            = location
        item['rating']              = rating
       
        yield item






