#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/9/2 15:08
@Author :lancelot.sheng
@File   :douban_client.py
"""
import json

import requests  # 导入requests库用于HTTP请求
from bs4 import BeautifulSoup  # 导入BeautifulSoup库用于解析HTML内容
from datetime import datetime  # 导入datetime模块用于获取日期和时间
import os  # 导入os模块用于文件和目录操作
from logger import LOG  # 导入日志模块
from jinja2 import Environment, FileSystemLoader, select_autoescape


class DoubanMoviesClient:

    def __init__(self):
        self.url = 'https://m.douban.com/rexxar/api/v2/movie/recommend'  # Hacker News的URL
        self.headers = {'Referer': 'https://movie.douban.com/explore',
                        'Host': 'm.douban.com',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
        # 创建一个Environment，指定模板文件所在的目录
        self.env = Environment(
            loader=FileSystemLoader('templates'),
            autoescape=select_autoescape(['html', 'xml', 'txt'])
        )

    def fetch_top_latest_movies(self, count: int = 20) -> list:
        LOG.debug("准备获取豆瓣最新的热门新闻。")
        try:
            latest_movie_url = self.url + f"?refresh=0&start=0&count={count}&selected_categories=%7B%7D&uncollect=false&sort=U&tags="
            response = requests.get(latest_movie_url, headers=self.headers, timeout=10, verify=False)
            response.raise_for_status()  # 检查请求是否成功
            # LOG.info(f"响应内容： {response.text}")
            data = json.loads(response.text)
            movies = []
            datas = data["items"]
            for d in datas:
                # print(str(d))
                obj = {"title": d["title"], "year": d["year"], "uri": d["uri"],
                       "url": 'https://www.douban.com/doubanapp/dispatch?uri=' + (
                           d["uri"].replace('douban://douban.com', '')),
                       "comment": d["comment"]["comment"],
                       "rating": d["rating"]["value"]}
                movies.append(obj)
            return movies
        except Exception as e:
            LOG.error(f"获取豆瓣最新的热门新闻失败：{str(e)}")
            return []

    def format_douban_report(self, ms: list) -> str:
        if ms is None or len(ms) == 0:
            ms = []
        data = {'movies': ms}
        template = self.env.get_template('movie_format.txt')
        output = template.render(data)
        today = datetime.now().date().isoformat()  # 获取今天的日期
        repo = today
        repo_dir = os.path.join('douban', repo)  # 构建存储路径
        os.makedirs(repo_dir, exist_ok=True)  # 确保目录存在
        current = datetime.now().strftime("%Y-%m-%d")
        file_path = os.path.join(repo_dir, f'movies_{current}.md')  # 构建文件路径
        with open(file_path, 'w') as file:
            file.write(output)

        LOG.info(f"豆瓣最新电影排名文件生成： {file_path}")  # 记录日志
        return file_path

    def process_douban_report(self, count: int = 20) -> str:
        ms = self.fetch_top_latest_movies(count)
        file_path = self.format_douban_report(ms)
        return file_path


if __name__ == "__main__":
    douban = DoubanMoviesClient()
    path = douban.process_douban_report(20)
    print(f"生成文件成功")
    # for m in movies:
    #     print(
    #         f' title: {m["title"]}  year:{m["year"]}  rating:{m["rating"]}  uri:{m["uri"]}  url:{m["url"]}  comment:{m["comment"]}')
