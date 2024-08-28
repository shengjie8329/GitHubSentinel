#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/8/26 14:22
@Author :lancelot.sheng
@File   :test_hackernews.py
"""
import requests
from bs4 import BeautifulSoup
from requests import RequestException
from jinja2 import Environment, FileSystemLoader, select_autoescape

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'  # https -> http
}

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml', 'text'])
)


def fetch_hacknews_headlines_test(num: int = 0) -> list:
    if num <= 0 or num > 30:
        num = 30
    # 发送HTTP请求获取Hacker News的HTML内容
    url = 'https://news.ycombinator.com'
    response = requests.get(url, proxies=proxies, verify=False)
    headlines = []
    # 检查请求是否成功
    if response.status_code == 200:
        content = response.text

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(content, 'html.parser')

        # 查找包含热点新闻的链接和标题的元素
        # items = soup.find_all('a', class_='storylink')
        # 查找包含热点新闻的标题和外部链接的元素
        items = soup.find_all('span', class_='titleline')

        # 提取标题和对应的外部链接

        for item in items:
            link_tag = item.find('a')
            if link_tag and link_tag['href'].startswith('http'):
                title = link_tag.get_text()
                link = link_tag['href']
                headlines.append({"title": title, "link": link})

        if len(headlines) > num:
            headlines = headlines[:num]
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return headlines


def fetch_page_content_test(url: str) -> str:
    # 发送HTTP请求获取网页内容
    try:
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            content = response.text

            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(content, 'html.parser')

            # 提取文章正文内容
            # 常见的文章内容标签可能包括 <article>, <div>, <section>, <p> 等
            # 根据具体的网页结构选择合适的标签来提取内容

            # 示例1: 提取 <article> 标签内的所有文本内容
            text = ''
            article = soup.find('article')
            if article:
                text = article.get_text()
            # 示例2: 如果没有 <article> 标签，提取 <div> 标签中 class 为 'post-content' 的内容
            post_content = soup.find('div', class_='post-content')
            if post_content:
                text = text + '\n\n' + post_content.get_text()
            # 示例3: 如果上述标签都没有，提取页面中的所有段落内容
            paragraphs = soup.find_all('p')
            temp = "\n\n".join([p.get_text() for p in paragraphs])
            text = text + '\n\n' + temp

            # 打印提取的文本内容
            # print(text)
            return text
        else:
            print(f"Failed to retrieve the webpage {url}. Status code: {response.status_code}")
            return ''
    except RequestException as e:
        # 捕获并处理所有请求相关的异常
        print(f"An error occurred while trying to fetch the URL {url} : {e}")
        return ''
    except Exception as e:
        # 捕获并处理其他非请求相关的异常
        print(f"An unexpected error occurred {url} : {e}")
        return ''


def process_hacknews_report_test(num: int = 0) -> str:
    headlines = fetch_hacknews_headlines_test(num)
    for idx, story in enumerate(headlines, 1):
        link = story['link']
        content = fetch_page_content_test(link)
        story['content'] = content
        # print(f"{idx}. {story['title']}\n   Link: {story['link']}\n {story['content']} \n")
    data = {'headlines': headlines}
    template = env.get_template('pages_format.txt')
    output = template.render(data)
    return output


str = process_hacknews_report_test(10)
print(str)
