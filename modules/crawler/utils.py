import requests
from bs4 import BeautifulSoup
import time
import pandas

def parserTargetURL(url_type, **kwargs):
    base_url = "https://www.ptt.cc"
    target_page_name = "index"
    target_page_ext = ".html"
    
    # 看板參數(參數處理)
    if 'board' in kwargs:
        target_board = kwargs['board']
    else:
        target_board = "Stock"
    
    # 看板分頁(參數處理)
    if 'pageNum' in kwargs:
        target_page_num = kwargs['pageNum']
    else:
        target_page_num = ""
    
    # 第一頁面處理
    if 'articleURL' in kwargs:
        article_url =  kwargs['articleURL']
    else:
        article_url = "/bbs/Stock/M.1629865915.A.A54.html"
    
    if url_type == "board":
        target_url = "{}/bbs/{}/{}{}{}".format(
            base_url,
            target_board,
            target_page_name,
            target_page_num,
            target_page_ext,
        )
    else:
        target_url = base_url + article_url
        
    return target_url


def run(**kwargs):
    full_article = []


    target_url = parserTargetURL('board', **kwargs)
    res = requests.get(target_url)
    html = BeautifulSoup(res.text)


    article_title = html.find_all('div', class_='title')


    for title in article_title:
        try:
            temp_url = title.find('a').attrs['href']
            temp_title = title.find('a').contents[0]

            article_url = parserTargetURL('article', articleURL=temp_url)
            article_html = requests.get(article_url)
            article_html = BeautifulSoup(article_html.text)

            # 文章內容
            content = article_html.find('div', id='main-content').text

            # 時間字串
            article_time = article_html.find('div', id='main-content').find_all('div', class_='article-metaline')[2].find_all('span')[1].contents[0]

            # 用時間分割字串
            content = content.split(article_time)[1]

            # 用字串找出結束
            content_end_string = u'※ 發信站:'
            content = content.split(content_end_string)[0]

            # 找作者
            author = article_html.find('div', id='main-content').find_all('div', class_='article-metaline')[0].find_all('span')[1].contents[0].split(" ")[0]
            
        except:
            temp_title = "(本文已被刪除)"
            author = "無"
            content = "無"
            article_time = None

        temp_dict = {
            'url': temp_url,
            'title':  temp_title,
            'content': content,
            'author': author,
            'time': article_time
        }

        full_article.append(temp_dict)
        time.sleep(0.5)

    return full_article
