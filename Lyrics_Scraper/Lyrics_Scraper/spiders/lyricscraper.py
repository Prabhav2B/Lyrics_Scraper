# -*- coding: utf-8 -*-
import csv
import scrapy
import re


links = []

with open('Extracted_Links.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		links.append(row['href'])

Start = 'https://www.azlyrics.com' + links[0]
links = links[1:]

File = open('Extracted_Lyrics.txt','w+')

class LyricscraperSpider(scrapy.Spider):
    
    name = 'lyricscraper'
    start_urls = [Start]

    def parse(self, response):
        
        Title_Raw = response.selector.xpath('//div[2]/b/text()').extract()

    	Lyrics_Raw = response.selector.xpath('//div[5]/text()').extract()

        lyrics = ""
        title = ""

        for ch in Title_Raw:
        	title = title + ch.encode('utf8')

        for lyric in Lyrics_Raw:
        	lyrics = lyrics + lyric.encode('utf8')
        
        File.write(title)
        File.write("\n")
        File.write(lyrics)
        File.write("\n\n")


        template = 'https://www.azlyrics.com'


        for link in links:
        	next_page = template+link
        	yield response.follow(next_page, self.parse)		