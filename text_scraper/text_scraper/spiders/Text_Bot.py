# -*- coding: utf-8 -*-
import scrapy


class TextBotSpider(scrapy.Spider):
    name = 'Text_Bot'

    #replace Link below with Desired Artist's azlyrics Home Page
    start_urls = ['https://www.azlyrics.com/b/bastille.html']

    def parse(self, response):

    	#Extracts links from the artist home page of AZlyrics
        links = response.css('a::attr(href)').extract()

        for item in zip(links):
        	scraped_info = {
        	'href' : item[0],
        	}
		yield scraped_info
