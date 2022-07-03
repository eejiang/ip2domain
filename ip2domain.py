import requests
from lxml import etree
import sys
header={
# 'Cache-Control': 'max-age=0"',
# 'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="99"',
# 'Sec-Ch-Ua-Mobile': '?0"',
# 'Sec-Ch-Ua-Platform': '"Linux"',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'Sec-Fetch-Site': 'none',
# 'Sec-Fetch-Mode': 'navigate',
# 'Sec-Fetch-User': '?1',
# 'Sec-Fetch-Dest': 'document',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'en-US,en;q=0.9',
# 'Connection': 'close'
'Host': 'ipchaxun.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'close',
'Cookie': 'Hm_lvt_e1818bae459f4aa54811832fda9b2dea=1656472541,1653511233; PHPSESSID=ltdgdud8eofl531pcaa3dr08g4; Hm_lpvt_e1818bae459f4aa54811832fda9b2dea=1653511233',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',

}
lines = []
fi1 = sys.argv[-1]
f = open(fi1)
for line in f.readlines():
    lines.append(line)
for domain in lines:
    domain = domain.replace("\n",'')
    resul=requests.get("https://ipchaxun.com/"+domain,verify=False,headers=header)
    html = resul.text
    htm=etree.HTML(html,etree.HTMLParser())
    # result=htm.xpath('//ul[@id="list"]/li/a[@target="_blank"]/text()') #获取a节点下的内容
    # result1=htm.xpath('//div[@class="result result2"]/h3/text()')
    result=htm.xpath("//div[@id='J_domain']/p/a[@target='_blank']/text()") #获取a节点下的内容
    # result1=htm.xpath('//div[@class="result result2"]/h3/text()')
    print(result)

