import json
import requests
from openai import OpenAI  # 导入OpenAI库用于访问GPT模型
from logger import LOG  # 导入日志模块

class LLM:
    def __init__(self, config):
        """
        初始化 LLM 类，根据配置选择使用的模型（OpenAI 或 Ollama）。

        :param config: 配置对象，包含所有的模型配置参数。
        """
        self.config = config
        self.model = config.llm_model_type.lower()  # 获取模型类型并转换为小写
        if self.model == "openai":
            self.client = OpenAI(base_url="https://ai-yyds.com/v1")  # 创建OpenAI客户端实例
        elif self.model == "ollama":
            self.api_url = config.ollama_api_url  # 设置Ollama API的URL
        else:
            LOG.error(f"不支持的模型类型: {self.model}")
            raise ValueError(f"不支持的模型类型: {self.model}")  # 如果模型类型不支持，抛出错误

    def generate_report(self, system_prompt, user_content):
        """
        生成报告，根据配置选择不同的模型来处理请求。

        :param system_prompt: 系统提示信息，包含上下文和规则。
        :param user_content: 用户提供的内容，通常是Markdown格式的文本。
        :return: 生成的报告内容。
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        # 根据选择的模型调用相应的生成报告方法
        if self.model == "openai":
            return self._generate_report_openai(messages)
        elif self.model == "ollama":
            return self._generate_report_ollama(messages)
        else:
            raise ValueError(f"不支持的模型类型: {self.model}")

    def _generate_report_openai(self, messages):
        """
        使用 OpenAI GPT 模型生成报告。

        :param messages: 包含系统提示和用户内容的消息列表。
        :return: 生成的报告内容。
        """
        LOG.info(f"使用 OpenAI {self.config.openai_model_name} 模型生成报告。")
        try:
            response = self.client.chat.completions.create(
                model=self.config.openai_model_name,  # 使用配置中的OpenAI模型名称
                messages=messages
            )
            LOG.debug("GPT 响应: {}", response)
            return response.choices[0].message.content  # 返回生成的报告内容
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise

    def _generate_report_ollama(self, messages):
        """
        使用 Ollama LLaMA 模型生成报告。

        :param messages: 包含系统提示和用户内容的消息列表。
        :return: 生成的报告内容。
        """
        LOG.info(f"使用 Ollama {self.config.ollama_model_name} 模型生成报告。")
        try:
            payload = {
                "model": self.config.ollama_model_name,  # 使用配置中的Ollama模型名称
                "messages": messages,
                "max_tokens": 4000,
                "temperature": 0.7,
                "stream": False
            }

            response = requests.post(self.api_url, json=payload)  # 发送POST请求到Ollama API
            response_data = response.json()

            # 调试输出查看完整的响应结构
            LOG.debug("Ollama 响应: {}", response_data)

            # 直接从响应数据中获取 content
            message_content = response_data.get("message", {}).get("content", None)
            if message_content:
                return message_content  # 返回生成的报告内容
            else:
                LOG.error("无法从响应中提取报告内容。")
                raise ValueError("Ollama API 返回的响应结构无效")
        except Exception as e:
            LOG.error(f"生成报告时发生错误：{e}")
            raise

if __name__ == '__main__':
    from config import Config  # 导入配置管理类
    config = Config()
    llm = LLM(config)

    markdown_content="""
---
### 标题: 刺猬
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35633904
### 年份: 2024
### 评分: 7.4
### 简介: 导演居然同时找了珠穆朗玛峰和马里亚纳海沟演戏

---
### 标题: 异形：夺命舰
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35792500
### 年份: 2024
### 评分: 7.5
### 简介: 买的是imax票，看的是指缝版

---
### 标题: 姥姥的外孙
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36328210
### 年份: 2024
### 评分: 9.0
### 简介: 你不拍，我不拍，“华人文化”老外拍

---
### 标题: 狗阵
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35242872
### 年份: 2024
### 评分: 7.0
### 简介: #77ᵗʰCannes 05/16Market Screening 管虎最好的一部电影8.5+

---
### 标题: 逆鳞
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36847744
### 年份: 2024
### 评分: 5.8
### 简介: 看完只想说“社会我腾哥，人狠话不多”😎

---
### 标题: 名侦探柯南：百万美元的五棱星
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36363001
### 年份: 2024
### 评分: 6.9
### 简介: 我兰真是天使。

---
### 标题: 抓娃娃
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36653918
### 年份: 2024
### 评分: 7.4
### 简介: 别谈意义 别想太多 搞笑就值得五星

---
### 标题: 因果报应
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36934908
### 年份: 2024
### 评分: 8.5
### 简介: 别让陈思诚看到这部片！

---
### 标题: 重生
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36484198
### 年份: 2024
### 评分: 6.1
### 简介: 属于阮经天的黄金时代来了

---
### 标题: 普罗米修斯
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/3771562
### 年份: 2012
### 评分: 7.6
### 简介: ⋯⋯開始快睡著了。然後快吐了⋯⋯

---
### 标题: 年少日记
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/34940879
### 年份: 2023
### 评分: 8.4
### 简介: 东亚家庭的坠楼死亡的剖析。

---
### 标题: 头脑特工队2
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36090457
### 年份: 2024
### 评分: 8.4
### 简介: 有人看电影 有人照镜子

---
### 标题: 异形
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/1300868
### 年份: 1979
### 评分: 8.3
### 简介: 女人和猫才是生命力最顽强的生物。

---
### 标题: 红楼梦之金玉良缘
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/26924522
### 年份: 2024
### 评分: 3.5
### 简介: 这项目从立项筹备到上映，也算历经多年坎坷了，我觉得胡玫之所以把它搬上大银幕，还是想用年轻人更接受更喜欢的男女纯爱来诠释时代悲剧，以现代人的视角看会更唏嘘，感动两个字，不足以形容。“木石前盟和金玉良缘”，一个是前世姻缘，一个复杂人性与残酷现实，这个预言果然实现，以大红喜事，以死亡，以双向奔赴的信守诺言。内心无比空空荡荡，又无比充盈，一切自有因缘，但行好事，自有安排。

---
### 标题: 红毯先生
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35494829
### 年份: 2023
### 评分: 6.5
### 简介: 我心目中4星，但他绝不是6.9分电影。大局观5星。

---
### 标题: 异形：契约
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/11803087
### 年份: 2017
### 评分: 7.4
### 简介: 两只法鲨傍地走 安能辨我是攻受

---
### 标题: 肖申克的救赎
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/1292052
### 年份: 1994
### 评分: 9.7
### 简介: 策划了19年的私奔……

---
### 标题: 白蛇：浮生
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36463483
### 年份: 2024
### 评分: 7.1
### 简介: 一个大家都熟得不能再熟的故事，讲成这样也不容易

---
### 标题: 异形2
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/1293792
### 年份: 1986
### 评分: 8.1
### 简介: 都过了两个生肖周期，中国电影还没摸到卡神的脚后跟。

---
### 标题: 热辣滚烫
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36081094
### 年份: 2024
### 评分: 7.6
### 简介: 看完想大喊：姐！
"""

    # 示例：生成 GitHub 报告
    system_prompt = """
你是一个关注热门电影的影评家，擅于热门电影的整理和评论。

任务：
你会收到一个包含电影列表的markdown格式的文件，其中每一条目间以分割线(---)分隔；
每一个条目中包含改电影的“名称”，“链接”，“年份”，“评分”，“简介”这几种属性
现在需要你根据收到的最新的电影列表进行分析，根据评分从高到低来排出5条推荐的电影，需要包含电影名称，上映时间，并根据标题和简介扩充总结出一个简短的评论，以markdown格式输出。

输出格式：
# 【推荐电影列表】
### Top N: {名称}
### 上映时间: {年份}
### 简评:  {归纳的评论}

参考示例如下:
# 【推荐电影列表】
### Top 1: 重生
### 上映时间: 2024
### 简评:  阮经天最新的代表作，讲述一个群体复仇的故事
---
### Top 2: 姥姥的外孙
### 上映时间: 2024
### 简评:  老外拍“华人文化”，引爆华人圈
---
### Top 3: 异形：夺命舰
### 上映时间: 2024
### 简评:  异形最新作，回归密闭空间中的原始恐惧
---
    """

    github_report = llm.generate_report(system_prompt, markdown_content)
    LOG.debug(github_report)
