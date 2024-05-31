# from ExObject.ExStock import is_trading_day, get_last_trading_day, get_next_trading_day, get_price
# from ExObject.DateTime import DateTime
from ExObject.ExParsel import ExSelector
import requests

# print(is_trading_day(DateTime.Now()))
# print(get_last_trading_day(DateTime.Now()))
# print(get_next_trading_day(DateTime.Now()))

# data=get_price("300059.SZ","2021-11-15")

# data2=get_price("300059.SZ","2018-11-13","cn")
# print(data)
# print(data2)


res = requests.get("https://www.newsbtc.com/").text
data = ExSelector(res)
for item in data.xpath("//article[contains(@class,'block-article')]"):
    source_url = item.xpath(".//a/@href").FIrstCleanString()
    title = item.xpath(".//a//text()").FIrstCleanString()
    cover_pic = item.xpath(".//img/@src").extract().AllCleanString()
    print(cover_pic)
