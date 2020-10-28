import requests
from lxml import etree


uri = 'https://www.yq-888.com/xiaoshuo/1/101454/'
head = 'https://www.yq-888.com/'
chapter = requests.get(uri)
chapter_html =etree.HTML(chapter.text)
chapter_list = chapter_html.xpath('//div[@id="list"]/dl/dd/a/@href')

access_L = []
count = 0
for i in chapter_list:
    count +=1 
    if count > 12 :
        access_L.append(head+i)

for i in access_L:
    xs = requests.get(i)
    xs_html = etree.HTML(xs.text)
    xs_text = xs_html.xpath('//div[@id="content"]/p/text()')
    xs_head = xs_html.xpath('//div[@class="bookname"]/h1/text()')
    with open("E:/video/神级宠物进化系统.txt", "a") as f:
        f.write(xs_head[0])
        for i in xs_text:
            f.write(i)