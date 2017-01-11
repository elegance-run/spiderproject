# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
import scrapy.spiders
from scrapy.selector import HtmlXPathSelector           #导入HtmlXPathSelector进行解析
from scrapy.contrib.spiders import CrawlSpider,Rule     #自定义抓取链接的规则
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor      #............
from pythonbeautiful.items import PythonbeautifulItem                       #............

class ZhengSpider(BaseSpider):
   name = "Me"
   allowed_domains = ["http://www.laianbbs.com"]              #运行抓取的网页
   start_urls = ["http://www.laianbbs.com/forum-54-1.html"]             #第一个抓取的网页

   #定义两个规则，第一个是当前要解析的网页，回调函数是parse_item；
   #rules = [
   #    Rule(SgmlLinkExtractor(allow=(r'http://guba.eastmoney.com/default_1.html\?start=\d+.*'))),
   #    Rule(SgmlLinkExtractor(allow=(r'http://guba.eastmoney.com/subject/\d+')), callback='parse_item'),
   #]

   # for i in range (1,2,1):
   #     start_urls.append('http://www.laianbbs.com/forum-54-%d.html'%i)

   def parse(self, response):
       hxs = HtmlXPathSelector(response)

       #sites = hxs.select('/html[@class="comiis_wide"]/body[@id="nv_forum"]/div[@id="wp"]/div[@class="boardnavr"]/div[@class="comiis_width"]/div[@class="comiis_rk"]/div[@class="comiis_lp"]/div[@id="ct"]/div[@class="mn fcvp"]/div[@id="threadlist"]/div[@class="bm_c"]/form[@id="moderate"]/table[@id="threadlisttableid"]/tbodytr/th[@class="common"]/')
       items = []
       sites = hxs.select('//tbody')


       for site in sites:
           item = PythonbeautifulItem()
           item['readtitle'] = site.select('tr/th[@class="common"]/a[@class="s xst"]/text()').extract()
           item['uptime'] = site.select('tr/td[@class="by"][1]/em/span/text()').extract()          #/tr
           item['lastsubmmit'] = site.select('tr/td[@class="by"][2]/em/a/text()').extract()
           items.append(item)
       return items