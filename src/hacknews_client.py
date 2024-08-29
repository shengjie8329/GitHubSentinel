#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/8/28 15:15
@Author :lancelot.sheng
@File   :hacknews_client.py
"""
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from requests import RequestException
from jinja2 import Environment, FileSystemLoader, select_autoescape
from logger import LOG  # 导入日志模块


class HackNewsClient:

    def __init__(self):
        self.url = "https://news.ycombinator.com"
        self.proxies = {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890'  # https -> http
        }
        # 创建一个Environment，指定模板文件所在的目录
        self.env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml', 'txt'])
        )

    def fetch_hacknews_headlines(self, num: int = 0) -> list:
        if num <= 0 or num > 30:
            num = 30
        # 发送HTTP请求获取Hacker News的HTML内容
        response = requests.get(self.url, proxies=self.proxies, verify=False)
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

    @staticmethod
    def fetch_page_content(url: str) -> str:
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

    def process_hacknews_report(self, num: int = 0) -> str:
        headlines = self.fetch_hacknews_headlines(num)
        for idx, story in enumerate(headlines, 1):
            link = story['link']
            content = self.fetch_page_content(link)
            story['content'] = content
        data = {'headlines': headlines}
        template = self.env.get_template('pages_format.txt')
        output = template.render(data)
        today = datetime.now().date().isoformat()  # 获取今天的日期
        repo = today
        repo_dir = os.path.join('hack_news', repo)  # 构建存储路径
        os.makedirs(repo_dir, exist_ok=True)  # 确保目录存在
        current = datetime.now().strftime("%Y-%m-%dT%H_%M_%SZ")
        file_path = os.path.join(repo_dir, f'news_{current}.md')  # 构建文件路径
        with open(file_path, 'w') as file:
            file.write(output)

        LOG.info(f"hacknews进展文件生成： {file_path}")  # 记录日志
        return file_path
