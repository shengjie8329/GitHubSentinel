#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   :2024/9/3 13:58
@Author :lancelot.sheng
@File   :test_douban_client.py
"""
import sys
import os
import unittest
from unittest.mock import patch, MagicMock, ANY

# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates')))

from douban_client import DoubanMoviesClient  # 导入要测试的 DoubanMoviesClient 类


class TestDoubanClient(unittest.TestCase):

    def setUp(self):
        self.client = DoubanMoviesClient()

    @patch('douban_client.requests.get')
    def test_fetch_top_movies_success(self, mock_get):
        # 模拟HTTP响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
{
	"count": 10,
	"show_rating_filter": true,
	"recommend_categories": [{
		"is_control": true,
		"type": "类型",
		"data": [{
			"default": true,
			"text": "全部类型"
		}, {
			"default": false,
			"text": "喜剧"
		}, {
			"default": false,
			"text": "爱情"
		}, {
			"default": false,
			"text": "动作"
		}, {
			"default": false,
			"text": "科幻"
		}, {
			"default": false,
			"text": "动画"
		}, {
			"default": false,
			"text": "悬疑"
		}, {
			"default": false,
			"text": "犯罪"
		}, {
			"default": false,
			"text": "惊悚"
		}, {
			"default": false,
			"text": "冒险"
		}, {
			"default": false,
			"text": "音乐"
		}, {
			"default": false,
			"text": "历史"
		}, {
			"default": false,
			"text": "奇幻"
		}, {
			"default": false,
			"text": "恐怖"
		}, {
			"default": false,
			"text": "战争"
		}, {
			"default": false,
			"text": "传记"
		}, {
			"default": false,
			"text": "歌舞"
		}, {
			"default": false,
			"text": "武侠"
		}, {
			"default": false,
			"text": "情色"
		}, {
			"default": false,
			"text": "灾难"
		}, {
			"default": false,
			"text": "西部"
		}, {
			"default": false,
			"text": "纪录片"
		}, {
			"default": false,
			"text": "短片"
		}]
	}, {
		"is_control": true,
		"type": "地区",
		"data": [{
			"default": true,
			"text": "全部地区"
		}, {
			"default": false,
			"text": "华语"
		}, {
			"default": false,
			"text": "欧美"
		}, {
			"default": false,
			"text": "韩国"
		}, {
			"default": false,
			"text": "日本"
		}, {
			"default": false,
			"text": "中国大陆"
		}, {
			"default": false,
			"text": "美国"
		}, {
			"default": false,
			"text": "中国香港"
		}, {
			"default": false,
			"text": "中国台湾"
		}, {
			"default": false,
			"text": "英国"
		}, {
			"default": false,
			"text": "法国"
		}, {
			"default": false,
			"text": "德国"
		}, {
			"default": false,
			"text": "意大利"
		}, {
			"default": false,
			"text": "西班牙"
		}, {
			"default": false,
			"text": "印度"
		}, {
			"default": false,
			"text": "泰国"
		}, {
			"default": false,
			"text": "俄罗斯"
		}, {
			"default": false,
			"text": "加拿大"
		}, {
			"default": false,
			"text": "澳大利亚"
		}, {
			"default": false,
			"text": "爱尔兰"
		}, {
			"default": false,
			"text": "瑞典"
		}, {
			"default": false,
			"text": "巴西"
		}, {
			"default": false,
			"text": "丹麦"
		}]
	}],
	"items": [{
		"comment": {
			"comment": "导演居然同时找了珠穆朗玛峰和马里亚纳海沟演戏",
			"id": "4280761611",
			"user": {
				"kind": "user",
				"name": "momo",
				"url": "https://www.douban.com/people/145833429/",
				"uri": "douban://douban.com/user/145833429",
				"avatar": "https://img3.doubanio.com/icon/up145833429-13.jpg",
				"is_club": false,
				"type": "user",
				"id": "145833429",
				"uid": "145833429"
			}
		},
		"rating": {
			"count": 175113,
			"max": 10,
			"star_count": 3.5,
			"value": 7.4
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2912147213.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2912147213.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/ECGM6JFQI?type=rank&category=movie&rank_type=year",
			"rank": 9,
			"title": "2023最值得期待的影视"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 中国香港 / 剧情 喜剧 家庭 / 顾长卫 / 葛优 王俊凯",
		"id": "35633904",
		"title": "刺猬",
		"tags": [{
			"name": "2023最值得期待的影视",
			"uri": "douban://douban.com/subject_collection/ECGM6JFQI?category=movie&rank_type=year&type=rank"
		}, {
			"name": "中国大陆 亲情 小说改编",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E4%BA%B2%E6%83%85%2C%E5%B0%8F%E8%AF%B4%E6%94%B9%E7%BC%96&type=tags"
		}],
		"interest": null,
		"type": "movie",		
		"has_linewatch": false,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2854710585.jpg", "https://img2.doubanio.com/view/photo/m/public/p2854710581.jpg", "https://img9.doubanio.com/view/photo/m/public/p2908983915.jpg", "https://img1.doubanio.com/view/photo/m/public/p2912135900.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35633904",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "你不拍，我不拍，“华人文化”老外拍",
			"id": "4241853394",
			"user": {
				"kind": "user",
				"name": "大号煎饼",
				"url": "https://www.douban.com/people/64345409/",
				"uri": "douban://douban.com/user/64345409",
				"avatar": "https://img3.doubanio.com/icon/up64345409-3.jpg",
				"is_club": false,
				"type": "user",
				"id": "64345409",
				"uid": "64345409"
			}
		},
		"rating": {
			"count": 95353,
			"max": 10,
			"star_count": 4.5,
			"value": 9.0
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img1.doubanio.com/view/photo/m_ratio_poster/public/p2911511570.jpg",
			"normal": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2911511570.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?type=rank&category=movie&rank_type=weekly",
			"rank": 1,
			"title": "一周口碑电影榜"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 泰国 / 剧情 / 帕特·波尼蒂帕特 / 普提蓬·阿萨拉塔纳功 乌萨·萨梅坎姆",
		"id": "36328210",
		"title": "姥姥的外孙",
		"tags": [{
			"name": "一周口碑电影榜",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?category=movie&rank_type=weekly&type=rank"
		}, {
			"name": "泰国 亲情 温情",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E6%B3%B0%E5%9B%BD%2C%E4%BA%B2%E6%83%85%2C%E6%B8%A9%E6%83%85&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2905125686.jpg", "https://img1.doubanio.com/view/photo/m/public/p2908082188.jpg", "https://img1.doubanio.com/view/photo/m/public/p2907790668.jpg", "https://img9.doubanio.com/view/photo/m/public/p2907558015.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36328210",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "买的是imax票，看的是指缝版",
			"id": "4273338109",
			"user": {
				"kind": "user",
				"name": "GiveMe0Cola",
				"url": "https://www.douban.com/people/110185037/",
				"uri": "douban://douban.com/user/110185037",
				"avatar": "https://img1.doubanio.com/icon/up110185037-19.jpg",
				"is_club": false,
				"type": "user",
				"id": "110185037",
				"uid": "hedmgh"
			}
		},
		"rating": {
			"count": 242410,
			"max": 10,
			"star_count": 4.0,
			"value": 7.5
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2910926865.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2910926865.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?type=rank&category=movie&rank_type=weekly",
			"rank": 2,
			"title": "一周口碑电影榜"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 美国 英国 / 科幻 惊悚 恐怖 / 费德·阿尔瓦雷兹 / 卡莉·史派妮 戴维·荣松",
		"id": "35792500",
		"title": "异形：夺命舰",
		"tags": [{
			"name": "一周口碑电影榜",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?category=movie&rank_type=weekly&type=rank"
		}, {
			"name": "美国 科幻 惊悚",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E7%BE%8E%E5%9B%BD%2C%E7%A7%91%E5%B9%BB%2C%E6%83%8A%E6%82%9A&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2905901513.jpg", "https://img9.doubanio.com/view/photo/m/public/p2905901516.jpg", "https://img3.doubanio.com/view/photo/m/public/p2905901517.jpg", "https://img1.doubanio.com/view/photo/m/public/p2910800040.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35792500",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "#77ᵗʰCannes 05/16Market Screening 管虎最好的一部电影8.5+",
			"id": "4191884584",
			"user": {
				"kind": "user",
				"name": "🦋",
				"url": "https://www.douban.com/people/135623300/",
				"uri": "douban://douban.com/user/135623300",
				"avatar": "https://img3.doubanio.com/icon/up135623300-162.jpg",
				"is_club": false,
				"type": "user",
				"id": "135623300",
				"uid": "LanYeah-7"
			}
		},
		"rating": {
			"count": 60465,
			"max": 10,
			"star_count": 3.5,
			"value": 7.0
		},
		"vendor_count": 4,
		"playable_date": "2024-08-21 00:00:00",
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2908333792.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2908333792.jpg"
		},
		"honor_infos": [],
		"vendor_icons": ["https://img2.doubanio.com/f/frodo/8286b9b5240f35c7e59e1b1768cd2ccf0467cde5/pics/vendors/migu_video.png", "https://img9.doubanio.com/f/frodo/fbc90f355fc45d5d2056e0d88c697f9414b56b44/pics/vendors/tencent.png", "https://img1.doubanio.com/f/frodo/990703f165ee40fa7a023949252882058a2ba57d/pics/vendors/mgtv.png"],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 剧情 / 管虎 / 彭于晏 佟丽娅",
		"id": "35242872",
		"title": "狗阵",
		"tags": [{
			"name": "中国大陆 文艺 人生",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E6%96%87%E8%89%BA%2C%E4%BA%BA%E7%94%9F&type=tags"
		}, {
			"name": "戛纳电影节 一种关注大奖 获奖作品",
			"uri": "douban://douban.com/subject_collection/ECTQ6MQQY?category=movie&rank_type=award_movie&type=rank"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": true,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2908333935.jpg", "https://img3.doubanio.com/view/photo/m/public/p2908333933.jpg", "https://img3.doubanio.com/view/photo/m/public/p2906793923.jpg", "https://img9.doubanio.com/view/photo/m/public/p2909264574.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35242872",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "别让陈思诚看到这部片！",
			"id": "4273077475",
			"user": {
				"kind": "user",
				"name": "momo",
				"url": "https://www.douban.com/people/174456957/",
				"uri": "douban://douban.com/user/174456957",
				"avatar": "https://img3.doubanio.com/icon/up174456957-13.jpg",
				"is_club": false,
				"type": "user",
				"id": "174456957",
				"uid": "174456957"
			}
		},
		"rating": {
			"count": 36238,
			"max": 10,
			"star_count": 4.5,
			"value": 8.5
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2909638286.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2909638286.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?type=rank&category=movie&rank_type=weekly",
			"rank": 3,
			"title": "一周口碑电影榜"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 印度 / 剧情 动作 惊悚 犯罪 / 尼蒂兰·萨米纳坦 / 维杰·西图帕提 阿努拉格·卡施亚普",
		"id": "36934908",
		"title": "因果报应",
		"tags": [{
			"name": "一周口碑电影榜",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?category=movie&rank_type=weekly&type=rank"
		}, {
			"name": "印度 悬疑 犯罪",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E5%8D%B0%E5%BA%A6%2C%E6%82%AC%E7%96%91%2C%E7%8A%AF%E7%BD%AA&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2911775482.jpg", "https://img1.doubanio.com/view/photo/m/public/p2911775479.jpg", "https://img2.doubanio.com/view/photo/m/public/p2911775481.jpg", "https://img1.doubanio.com/view/photo/m/public/p2911775480.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36934908",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "看完只想说“社会我腾哥，人狠话不多”😎",
			"id": "4280824386",
			"user": {
				"kind": "user",
				"name": "xzw",
				"url": "https://www.douban.com/people/1364351/",
				"uri": "douban://douban.com/user/1364351",
				"avatar": "https://img2.doubanio.com/icon/u1364351-1.jpg",
				"is_club": false,
				"type": "user",
				"id": "1364351",
				"uid": "xzw"
			}
		},
		"rating": {
			"count": 18066,
			"max": 10,
			"star_count": 3.0,
			"value": 5.8
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img1.doubanio.com/view/photo/m_ratio_poster/public/p2911517619.jpg",
			"normal": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2911517619.jpg"
		},
		"honor_infos": [],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 剧情 犯罪 / 大庆 / 沈腾 张雨绮",
		"id": "36847744",
		"title": "逆鳞",
		"tags": [{
			"name": "中国大陆 犯罪 喜剧",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E7%8A%AF%E7%BD%AA%2C%E5%96%9C%E5%89%A7&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2911521214.jpg", "https://img9.doubanio.com/view/photo/m/public/p2911779824.jpg", "https://img3.doubanio.com/view/photo/m/public/p2911521213.jpg", "https://img3.doubanio.com/view/photo/m/public/p2911521217.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36847744",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "东亚家庭的坠楼死亡的剖析。",
			"id": "4158037283",
			"user": {
				"kind": "user",
				"name": "小东懒得动",
				"url": "https://www.douban.com/people/62367841/",
				"uri": "douban://douban.com/user/62367841",
				"avatar": "https://img9.doubanio.com/icon/up62367841-6.jpg",
				"is_club": false,
				"type": "user",
				"id": "62367841",
				"uid": "62367841"
			}
		},
		"rating": {
			"count": 119318,
			"max": 10,
			"star_count": 4.0,
			"value": 8.4
		},
		"vendor_count": 4,
		"playable_date": "2024-08-25 00:00:00",
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2906644236.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2906644236.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/ECTE6FIUY?type=rank&category=movie&rank_type=year",
			"rank": 3,
			"title": "豆瓣2024最值得期待华语电影"
		}],
		"vendor_icons": ["https://img2.doubanio.com/f/frodo/8286b9b5240f35c7e59e1b1768cd2ccf0467cde5/pics/vendors/migu_video.png", "https://img9.doubanio.com/f/frodo/fbc90f355fc45d5d2056e0d88c697f9414b56b44/pics/vendors/tencent.png", "https://img9.doubanio.com/f/frodo/88a62f5e0cf9981c910e60f4421c3e66aac2c9bc/pics/vendors/bilibili.png"],
		"year": "2023",
		"card_subtitle": "2023 / 中国香港 / 剧情 / 卓亦谦 / 卢镇业 郑中基",
		"id": "34940879",
		"title": "年少日记",
		"tags": [{
			"name": "豆瓣2024最值得期待华语电影",
			"uri": "douban://douban.com/subject_collection/ECTE6FIUY?category=movie&rank_type=year&type=rank"
		}, {
			"name": "中国香港 家庭 人生",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF%2C%E5%AE%B6%E5%BA%AD%2C%E4%BA%BA%E7%94%9F&type=tags"
		}, {
			"name": "香港电影金像奖 最佳电影 获奖作品",
			"uri": "douban://douban.com/subject_collection/ECJE6UCEY?category=movie&rank_type=award_movie&type=rank"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": true,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2907377433.jpg", "https://img1.doubanio.com/view/photo/m/public/p2901511658.jpg", "https://img3.doubanio.com/view/photo/m/public/p2898713342.jpg", "https://img3.doubanio.com/view/photo/m/public/p2907377537.jpg"],
		"card": "subject",
		"playable_date_info": "9天前上架",
		"following_rating": null,
		"uri": "douban://douban.com/movie/34940879",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "我兰真是天使。",
			"id": "4156775551",
			"user": {
				"kind": "user",
				"name": "nina★11",
				"url": "https://www.douban.com/people/2279875/",
				"uri": "douban://douban.com/user/2279875",
				"avatar": "https://img3.doubanio.com/icon/up2279875-27.jpg",
				"is_club": false,
				"type": "user",
				"id": "2279875",
				"uid": "lastnina"
			}
		},
		"rating": {
			"count": 54194,
			"max": 10,
			"star_count": 3.5,
			"value": 6.9
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2911723556.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2911723556.jpg"
		},
		"honor_infos": [],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 日本 / 动画 悬疑 犯罪 / 永冈智佳 / 高山南 山崎和佳奈",
		"id": "36363001",
		"title": "名侦探柯南：百万美元的五棱星",
		"tags": [{
			"name": "日本 动画 悬疑",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E6%97%A5%E6%9C%AC%2C%E5%8A%A8%E7%94%BB%2C%E6%82%AC%E7%96%91&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img1.doubanio.com/view/photo/m/public/p2901471850.jpg", "https://img3.doubanio.com/view/photo/m/public/p2901471842.jpg", "https://img3.doubanio.com/view/photo/m/public/p2901471843.jpg", "https://img3.doubanio.com/view/photo/m/public/p2901471847.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36363001",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "别谈意义 别想太多 搞笑就值得五星",
			"id": "4242053729",
			"user": {
				"kind": "user",
				"name": "wendy",
				"url": "https://www.douban.com/people/1026205/",
				"uri": "douban://douban.com/user/1026205",
				"avatar": "https://img2.doubanio.com/icon/up1026205-1.jpg",
				"is_club": false,
				"type": "user",
				"id": "1026205",
				"uid": "1026205"
			}
		},
		"rating": {
			"count": 443216,
			"max": 10,
			"star_count": 3.5,
			"value": 7.4
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2910105262.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2910105262.jpg"
		},
		"honor_infos": [],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 喜剧 / 闫非 彭大魔 / 沈腾 马丽",
		"id": "36653918",
		"title": "抓娃娃",
		"tags": [{
			"name": "中国大陆 喜剧 搞笑",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E5%96%9C%E5%89%A7%2C%E6%90%9E%E7%AC%91&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2910360527.jpg", "https://img2.doubanio.com/view/photo/m/public/p2910360531.jpg", "https://img3.doubanio.com/view/photo/m/public/p2910978732.jpg", "https://img3.doubanio.com/view/photo/m/public/p2910978733.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36653918",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "这部电影真的太好看了！！又燃又炸！！！",
			"id": "4253953504",
			"user": {
				"kind": "user",
				"name": "豆友谊如宝🇷🇺",
				"url": "https://www.douban.com/people/245503718/",
				"uri": "douban://douban.com/user/245503718",
				"avatar": "https://img2.doubanio.com/icon/up245503718-1.jpg",
				"is_club": false,
				"type": "user",
				"id": "245503718",
				"uid": "245503718"
			}
		},
		"rating": {
			"count": 91485,
			"max": 10,
			"star_count": 3.0,
			"value": 5.9
		},
		"vendor_count": 2,
		"playable_date": "2024-08-31 00:00:00",
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2910944812.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2910944812.jpg"
		},
		"honor_infos": [],
		"vendor_icons": ["https://img2.doubanio.com/f/frodo/8286b9b5240f35c7e59e1b1768cd2ccf0467cde5/pics/vendors/migu_video.png", "https://img1.doubanio.com/f/frodo/990703f165ee40fa7a023949252882058a2ba57d/pics/vendors/mgtv.png"],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 动作 奇幻 / 乌尔善 夏鹏 / 胡先煦 李宛妲",
		"id": "35228399",
		"title": "异人之下",
		"tags": [{
			"name": "中国大陆 奇幻 动作",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E5%A5%87%E5%B9%BB%2C%E5%8A%A8%E4%BD%9C&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": true,
		"photos": ["https://img1.doubanio.com/view/photo/m/public/p2910193950.jpg", "https://img1.doubanio.com/view/photo/m/public/p2909664699.jpg", "https://img1.doubanio.com/view/photo/m/public/p2911376450.jpg", "https://img3.doubanio.com/view/photo/m/public/p2910193947.jpg"],
		"card": "subject",
		"playable_date_info": "3天前上架",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35228399",
		"episodes_info": "",
		"item_type": "movie"
	}],
	"bottom_recommend_tags": ["荒诞", "家庭", "建筑", "温暖", "公路", "赛车", "童年", "特摄", "游戏改编", "神话"],
	"start": 0,
	"playable_filters": [{
		"uri": "douban://douban.com/playable_setting?rxr_callback=",
		"key": "free_playable",
		"title": "免费观看"
	}, {
		"uri": "",
		"key": "new_playable",
		"title": "最新上架"
	}, {
		"uri": "",
		"key": "soon_playable",
		"title": "即将上架"
	}],
	"filters": [{
		"text": "未标“看过”",
		"checked": false,
		"name": "uncollect",
		"desc": "仅看还没有被标记为“看过”的影片"
	}, {
		"text": "免费观看设置",
		"desc": "定制免费观看影视库",
		"uri": "douban://douban.com/playable_setting?rxr_callback=",
		"name": "vendor_setting"
	}],
	"quick_mark": null,
	"recommend_tags": ["荒诞", "家庭", "建筑", "温暖", "公路", "赛车", "童年", "特摄", "游戏改编", "神话"],
	"manual_tags": [],
	"sorts": [{
		"text": "综合排序",
		"checked": true,
		"name": "T"
	}, {
		"text": "近期热度",
		"checked": false,
		"name": "U"
	}, {
		"text": "首映时间",
		"checked": false,
		"name": "R"
	}, {
		"text": "高分优先",
		"checked": false,
		"name": "S"
	}],
	"total": 500
}
        '''

        mock_get.return_value = mock_response

        top_movies = self.client.fetch_top_latest_movies(10)
        self.assertEqual(len(top_movies), 10)
        self.assertEqual(top_movies[0]['title'], '刺猬')
        self.assertEqual(top_movies[0]['url'], 'https://www.douban.com/doubanapp/dispatch?uri=/movie/35633904')

    @patch('douban_client.requests.get')
    @patch('douban_client.os.makedirs')
    @patch('douban_client.open', new_callable=unittest.mock.mock_open)
    def test_export_top_movies(self, mock_open, mock_makedirs, mock_get):
        # 模拟HTTP响应
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
{
	"count": 10,
	"show_rating_filter": true,
	"recommend_categories": [{
		"is_control": true,
		"type": "类型",
		"data": [{
			"default": true,
			"text": "全部类型"
		}, {
			"default": false,
			"text": "喜剧"
		}, {
			"default": false,
			"text": "爱情"
		}, {
			"default": false,
			"text": "动作"
		}, {
			"default": false,
			"text": "科幻"
		}, {
			"default": false,
			"text": "动画"
		}, {
			"default": false,
			"text": "悬疑"
		}, {
			"default": false,
			"text": "犯罪"
		}, {
			"default": false,
			"text": "惊悚"
		}, {
			"default": false,
			"text": "冒险"
		}, {
			"default": false,
			"text": "音乐"
		}, {
			"default": false,
			"text": "历史"
		}, {
			"default": false,
			"text": "奇幻"
		}, {
			"default": false,
			"text": "恐怖"
		}, {
			"default": false,
			"text": "战争"
		}, {
			"default": false,
			"text": "传记"
		}, {
			"default": false,
			"text": "歌舞"
		}, {
			"default": false,
			"text": "武侠"
		}, {
			"default": false,
			"text": "情色"
		}, {
			"default": false,
			"text": "灾难"
		}, {
			"default": false,
			"text": "西部"
		}, {
			"default": false,
			"text": "纪录片"
		}, {
			"default": false,
			"text": "短片"
		}]
	}, {
		"is_control": true,
		"type": "地区",
		"data": [{
			"default": true,
			"text": "全部地区"
		}, {
			"default": false,
			"text": "华语"
		}, {
			"default": false,
			"text": "欧美"
		}, {
			"default": false,
			"text": "韩国"
		}, {
			"default": false,
			"text": "日本"
		}, {
			"default": false,
			"text": "中国大陆"
		}, {
			"default": false,
			"text": "美国"
		}, {
			"default": false,
			"text": "中国香港"
		}, {
			"default": false,
			"text": "中国台湾"
		}, {
			"default": false,
			"text": "英国"
		}, {
			"default": false,
			"text": "法国"
		}, {
			"default": false,
			"text": "德国"
		}, {
			"default": false,
			"text": "意大利"
		}, {
			"default": false,
			"text": "西班牙"
		}, {
			"default": false,
			"text": "印度"
		}, {
			"default": false,
			"text": "泰国"
		}, {
			"default": false,
			"text": "俄罗斯"
		}, {
			"default": false,
			"text": "加拿大"
		}, {
			"default": false,
			"text": "澳大利亚"
		}, {
			"default": false,
			"text": "爱尔兰"
		}, {
			"default": false,
			"text": "瑞典"
		}, {
			"default": false,
			"text": "巴西"
		}, {
			"default": false,
			"text": "丹麦"
		}]
	}],
	"items": [{
		"comment": {
			"comment": "导演居然同时找了珠穆朗玛峰和马里亚纳海沟演戏",
			"id": "4280761611",
			"user": {
				"kind": "user",
				"name": "momo",
				"url": "https://www.douban.com/people/145833429/",
				"uri": "douban://douban.com/user/145833429",
				"avatar": "https://img3.doubanio.com/icon/up145833429-13.jpg",
				"is_club": false,
				"type": "user",
				"id": "145833429",
				"uid": "145833429"
			}
		},
		"rating": {
			"count": 175113,
			"max": 10,
			"star_count": 3.5,
			"value": 7.4
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2912147213.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2912147213.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/ECGM6JFQI?type=rank&category=movie&rank_type=year",
			"rank": 9,
			"title": "2023最值得期待的影视"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 中国香港 / 剧情 喜剧 家庭 / 顾长卫 / 葛优 王俊凯",
		"id": "35633904",
		"title": "刺猬",
		"tags": [{
			"name": "2023最值得期待的影视",
			"uri": "douban://douban.com/subject_collection/ECGM6JFQI?category=movie&rank_type=year&type=rank"
		}, {
			"name": "中国大陆 亲情 小说改编",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E4%BA%B2%E6%83%85%2C%E5%B0%8F%E8%AF%B4%E6%94%B9%E7%BC%96&type=tags"
		}],
		"interest": null,
		"type": "movie",		
		"has_linewatch": false,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2854710585.jpg", "https://img2.doubanio.com/view/photo/m/public/p2854710581.jpg", "https://img9.doubanio.com/view/photo/m/public/p2908983915.jpg", "https://img1.doubanio.com/view/photo/m/public/p2912135900.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35633904",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "你不拍，我不拍，“华人文化”老外拍",
			"id": "4241853394",
			"user": {
				"kind": "user",
				"name": "大号煎饼",
				"url": "https://www.douban.com/people/64345409/",
				"uri": "douban://douban.com/user/64345409",
				"avatar": "https://img3.doubanio.com/icon/up64345409-3.jpg",
				"is_club": false,
				"type": "user",
				"id": "64345409",
				"uid": "64345409"
			}
		},
		"rating": {
			"count": 95353,
			"max": 10,
			"star_count": 4.5,
			"value": 9.0
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img1.doubanio.com/view/photo/m_ratio_poster/public/p2911511570.jpg",
			"normal": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2911511570.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?type=rank&category=movie&rank_type=weekly",
			"rank": 1,
			"title": "一周口碑电影榜"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 泰国 / 剧情 / 帕特·波尼蒂帕特 / 普提蓬·阿萨拉塔纳功 乌萨·萨梅坎姆",
		"id": "36328210",
		"title": "姥姥的外孙",
		"tags": [{
			"name": "一周口碑电影榜",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?category=movie&rank_type=weekly&type=rank"
		}, {
			"name": "泰国 亲情 温情",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E6%B3%B0%E5%9B%BD%2C%E4%BA%B2%E6%83%85%2C%E6%B8%A9%E6%83%85&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2905125686.jpg", "https://img1.doubanio.com/view/photo/m/public/p2908082188.jpg", "https://img1.doubanio.com/view/photo/m/public/p2907790668.jpg", "https://img9.doubanio.com/view/photo/m/public/p2907558015.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36328210",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "买的是imax票，看的是指缝版",
			"id": "4273338109",
			"user": {
				"kind": "user",
				"name": "GiveMe0Cola",
				"url": "https://www.douban.com/people/110185037/",
				"uri": "douban://douban.com/user/110185037",
				"avatar": "https://img1.doubanio.com/icon/up110185037-19.jpg",
				"is_club": false,
				"type": "user",
				"id": "110185037",
				"uid": "hedmgh"
			}
		},
		"rating": {
			"count": 242410,
			"max": 10,
			"star_count": 4.0,
			"value": 7.5
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2910926865.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2910926865.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?type=rank&category=movie&rank_type=weekly",
			"rank": 2,
			"title": "一周口碑电影榜"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 美国 英国 / 科幻 惊悚 恐怖 / 费德·阿尔瓦雷兹 / 卡莉·史派妮 戴维·荣松",
		"id": "35792500",
		"title": "异形：夺命舰",
		"tags": [{
			"name": "一周口碑电影榜",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?category=movie&rank_type=weekly&type=rank"
		}, {
			"name": "美国 科幻 惊悚",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E7%BE%8E%E5%9B%BD%2C%E7%A7%91%E5%B9%BB%2C%E6%83%8A%E6%82%9A&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2905901513.jpg", "https://img9.doubanio.com/view/photo/m/public/p2905901516.jpg", "https://img3.doubanio.com/view/photo/m/public/p2905901517.jpg", "https://img1.doubanio.com/view/photo/m/public/p2910800040.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35792500",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "#77ᵗʰCannes 05/16Market Screening 管虎最好的一部电影8.5+",
			"id": "4191884584",
			"user": {
				"kind": "user",
				"name": "🦋",
				"url": "https://www.douban.com/people/135623300/",
				"uri": "douban://douban.com/user/135623300",
				"avatar": "https://img3.doubanio.com/icon/up135623300-162.jpg",
				"is_club": false,
				"type": "user",
				"id": "135623300",
				"uid": "LanYeah-7"
			}
		},
		"rating": {
			"count": 60465,
			"max": 10,
			"star_count": 3.5,
			"value": 7.0
		},
		"vendor_count": 4,
		"playable_date": "2024-08-21 00:00:00",
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2908333792.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2908333792.jpg"
		},
		"honor_infos": [],
		"vendor_icons": ["https://img2.doubanio.com/f/frodo/8286b9b5240f35c7e59e1b1768cd2ccf0467cde5/pics/vendors/migu_video.png", "https://img9.doubanio.com/f/frodo/fbc90f355fc45d5d2056e0d88c697f9414b56b44/pics/vendors/tencent.png", "https://img1.doubanio.com/f/frodo/990703f165ee40fa7a023949252882058a2ba57d/pics/vendors/mgtv.png"],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 剧情 / 管虎 / 彭于晏 佟丽娅",
		"id": "35242872",
		"title": "狗阵",
		"tags": [{
			"name": "中国大陆 文艺 人生",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E6%96%87%E8%89%BA%2C%E4%BA%BA%E7%94%9F&type=tags"
		}, {
			"name": "戛纳电影节 一种关注大奖 获奖作品",
			"uri": "douban://douban.com/subject_collection/ECTQ6MQQY?category=movie&rank_type=award_movie&type=rank"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": true,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2908333935.jpg", "https://img3.doubanio.com/view/photo/m/public/p2908333933.jpg", "https://img3.doubanio.com/view/photo/m/public/p2906793923.jpg", "https://img9.doubanio.com/view/photo/m/public/p2909264574.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35242872",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "别让陈思诚看到这部片！",
			"id": "4273077475",
			"user": {
				"kind": "user",
				"name": "momo",
				"url": "https://www.douban.com/people/174456957/",
				"uri": "douban://douban.com/user/174456957",
				"avatar": "https://img3.doubanio.com/icon/up174456957-13.jpg",
				"is_club": false,
				"type": "user",
				"id": "174456957",
				"uid": "174456957"
			}
		},
		"rating": {
			"count": 36238,
			"max": 10,
			"star_count": 4.5,
			"value": 8.5
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2909638286.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2909638286.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?type=rank&category=movie&rank_type=weekly",
			"rank": 3,
			"title": "一周口碑电影榜"
		}],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 印度 / 剧情 动作 惊悚 犯罪 / 尼蒂兰·萨米纳坦 / 维杰·西图帕提 阿努拉格·卡施亚普",
		"id": "36934908",
		"title": "因果报应",
		"tags": [{
			"name": "一周口碑电影榜",
			"uri": "douban://douban.com/subject_collection/movie_weekly_best?category=movie&rank_type=weekly&type=rank"
		}, {
			"name": "印度 悬疑 犯罪",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E5%8D%B0%E5%BA%A6%2C%E6%82%AC%E7%96%91%2C%E7%8A%AF%E7%BD%AA&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2911775482.jpg", "https://img1.doubanio.com/view/photo/m/public/p2911775479.jpg", "https://img2.doubanio.com/view/photo/m/public/p2911775481.jpg", "https://img1.doubanio.com/view/photo/m/public/p2911775480.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36934908",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "看完只想说“社会我腾哥，人狠话不多”😎",
			"id": "4280824386",
			"user": {
				"kind": "user",
				"name": "xzw",
				"url": "https://www.douban.com/people/1364351/",
				"uri": "douban://douban.com/user/1364351",
				"avatar": "https://img2.doubanio.com/icon/u1364351-1.jpg",
				"is_club": false,
				"type": "user",
				"id": "1364351",
				"uid": "xzw"
			}
		},
		"rating": {
			"count": 18066,
			"max": 10,
			"star_count": 3.0,
			"value": 5.8
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img1.doubanio.com/view/photo/m_ratio_poster/public/p2911517619.jpg",
			"normal": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2911517619.jpg"
		},
		"honor_infos": [],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 剧情 犯罪 / 大庆 / 沈腾 张雨绮",
		"id": "36847744",
		"title": "逆鳞",
		"tags": [{
			"name": "中国大陆 犯罪 喜剧",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E7%8A%AF%E7%BD%AA%2C%E5%96%9C%E5%89%A7&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img9.doubanio.com/view/photo/m/public/p2911521214.jpg", "https://img9.doubanio.com/view/photo/m/public/p2911779824.jpg", "https://img3.doubanio.com/view/photo/m/public/p2911521213.jpg", "https://img3.doubanio.com/view/photo/m/public/p2911521217.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36847744",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "东亚家庭的坠楼死亡的剖析。",
			"id": "4158037283",
			"user": {
				"kind": "user",
				"name": "小东懒得动",
				"url": "https://www.douban.com/people/62367841/",
				"uri": "douban://douban.com/user/62367841",
				"avatar": "https://img9.doubanio.com/icon/up62367841-6.jpg",
				"is_club": false,
				"type": "user",
				"id": "62367841",
				"uid": "62367841"
			}
		},
		"rating": {
			"count": 119318,
			"max": 10,
			"star_count": 4.0,
			"value": 8.4
		},
		"vendor_count": 4,
		"playable_date": "2024-08-25 00:00:00",
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2906644236.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2906644236.jpg"
		},
		"honor_infos": [{
			"kind": "movie",
			"uri": "douban://douban.com/subject_collection/ECTE6FIUY?type=rank&category=movie&rank_type=year",
			"rank": 3,
			"title": "豆瓣2024最值得期待华语电影"
		}],
		"vendor_icons": ["https://img2.doubanio.com/f/frodo/8286b9b5240f35c7e59e1b1768cd2ccf0467cde5/pics/vendors/migu_video.png", "https://img9.doubanio.com/f/frodo/fbc90f355fc45d5d2056e0d88c697f9414b56b44/pics/vendors/tencent.png", "https://img9.doubanio.com/f/frodo/88a62f5e0cf9981c910e60f4421c3e66aac2c9bc/pics/vendors/bilibili.png"],
		"year": "2023",
		"card_subtitle": "2023 / 中国香港 / 剧情 / 卓亦谦 / 卢镇业 郑中基",
		"id": "34940879",
		"title": "年少日记",
		"tags": [{
			"name": "豆瓣2024最值得期待华语电影",
			"uri": "douban://douban.com/subject_collection/ECTE6FIUY?category=movie&rank_type=year&type=rank"
		}, {
			"name": "中国香港 家庭 人生",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF%2C%E5%AE%B6%E5%BA%AD%2C%E4%BA%BA%E7%94%9F&type=tags"
		}, {
			"name": "香港电影金像奖 最佳电影 获奖作品",
			"uri": "douban://douban.com/subject_collection/ECJE6UCEY?category=movie&rank_type=award_movie&type=rank"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": true,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2907377433.jpg", "https://img1.doubanio.com/view/photo/m/public/p2901511658.jpg", "https://img3.doubanio.com/view/photo/m/public/p2898713342.jpg", "https://img3.doubanio.com/view/photo/m/public/p2907377537.jpg"],
		"card": "subject",
		"playable_date_info": "9天前上架",
		"following_rating": null,
		"uri": "douban://douban.com/movie/34940879",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "我兰真是天使。",
			"id": "4156775551",
			"user": {
				"kind": "user",
				"name": "nina★11",
				"url": "https://www.douban.com/people/2279875/",
				"uri": "douban://douban.com/user/2279875",
				"avatar": "https://img3.doubanio.com/icon/up2279875-27.jpg",
				"is_club": false,
				"type": "user",
				"id": "2279875",
				"uid": "lastnina"
			}
		},
		"rating": {
			"count": 54194,
			"max": 10,
			"star_count": 3.5,
			"value": 6.9
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img9.doubanio.com/view/photo/m_ratio_poster/public/p2911723556.jpg",
			"normal": "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2911723556.jpg"
		},
		"honor_infos": [],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 日本 / 动画 悬疑 犯罪 / 永冈智佳 / 高山南 山崎和佳奈",
		"id": "36363001",
		"title": "名侦探柯南：百万美元的五棱星",
		"tags": [{
			"name": "日本 动画 悬疑",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E6%97%A5%E6%9C%AC%2C%E5%8A%A8%E7%94%BB%2C%E6%82%AC%E7%96%91&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img1.doubanio.com/view/photo/m/public/p2901471850.jpg", "https://img3.doubanio.com/view/photo/m/public/p2901471842.jpg", "https://img3.doubanio.com/view/photo/m/public/p2901471843.jpg", "https://img3.doubanio.com/view/photo/m/public/p2901471847.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36363001",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "别谈意义 别想太多 搞笑就值得五星",
			"id": "4242053729",
			"user": {
				"kind": "user",
				"name": "wendy",
				"url": "https://www.douban.com/people/1026205/",
				"uri": "douban://douban.com/user/1026205",
				"avatar": "https://img2.doubanio.com/icon/up1026205-1.jpg",
				"is_club": false,
				"type": "user",
				"id": "1026205",
				"uid": "1026205"
			}
		},
		"rating": {
			"count": 443216,
			"max": 10,
			"star_count": 3.5,
			"value": 7.4
		},
		"vendor_count": 0,
		"playable_date": null,
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2910105262.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2910105262.jpg"
		},
		"honor_infos": [],
		"vendor_icons": [],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 喜剧 / 闫非 彭大魔 / 沈腾 马丽",
		"id": "36653918",
		"title": "抓娃娃",
		"tags": [{
			"name": "中国大陆 喜剧 搞笑",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E5%96%9C%E5%89%A7%2C%E6%90%9E%E7%AC%91&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": false,
		"photos": ["https://img3.doubanio.com/view/photo/m/public/p2910360527.jpg", "https://img2.doubanio.com/view/photo/m/public/p2910360531.jpg", "https://img3.doubanio.com/view/photo/m/public/p2910978732.jpg", "https://img3.doubanio.com/view/photo/m/public/p2910978733.jpg"],
		"card": "subject",
		"playable_date_info": "",
		"following_rating": null,
		"uri": "douban://douban.com/movie/36653918",
		"episodes_info": "",
		"item_type": "movie"
	}, {
		"comment": {
			"comment": "这部电影真的太好看了！！又燃又炸！！！",
			"id": "4253953504",
			"user": {
				"kind": "user",
				"name": "豆友谊如宝🇷🇺",
				"url": "https://www.douban.com/people/245503718/",
				"uri": "douban://douban.com/user/245503718",
				"avatar": "https://img2.doubanio.com/icon/up245503718-1.jpg",
				"is_club": false,
				"type": "user",
				"id": "245503718",
				"uid": "245503718"
			}
		},
		"rating": {
			"count": 91485,
			"max": 10,
			"star_count": 3.0,
			"value": 5.9
		},
		"vendor_count": 2,
		"playable_date": "2024-08-31 00:00:00",
		"pic": {
			"large": "https://img3.doubanio.com/view/photo/m_ratio_poster/public/p2910944812.jpg",
			"normal": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2910944812.jpg"
		},
		"honor_infos": [],
		"vendor_icons": ["https://img2.doubanio.com/f/frodo/8286b9b5240f35c7e59e1b1768cd2ccf0467cde5/pics/vendors/migu_video.png", "https://img1.doubanio.com/f/frodo/990703f165ee40fa7a023949252882058a2ba57d/pics/vendors/mgtv.png"],
		"year": "2024",
		"card_subtitle": "2024 / 中国大陆 / 动作 奇幻 / 乌尔善 夏鹏 / 胡先煦 李宛妲",
		"id": "35228399",
		"title": "异人之下",
		"tags": [{
			"name": "中国大陆 奇幻 动作",
			"uri": "douban://douban.com/movie/recommend_tag?tag=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%2C%E5%A5%87%E5%B9%BB%2C%E5%8A%A8%E4%BD%9C&type=tags"
		}],
		"interest": null,
		"type": "movie",
		"has_linewatch": true,
		"photos": ["https://img1.doubanio.com/view/photo/m/public/p2910193950.jpg", "https://img1.doubanio.com/view/photo/m/public/p2909664699.jpg", "https://img1.doubanio.com/view/photo/m/public/p2911376450.jpg", "https://img3.doubanio.com/view/photo/m/public/p2910193947.jpg"],
		"card": "subject",
		"playable_date_info": "3天前上架",
		"following_rating": null,
		"uri": "douban://douban.com/movie/35228399",
		"episodes_info": "",
		"item_type": "movie"
	}],
	"bottom_recommend_tags": ["荒诞", "家庭", "建筑", "温暖", "公路", "赛车", "童年", "特摄", "游戏改编", "神话"],
	"start": 0,
	"playable_filters": [{
		"uri": "douban://douban.com/playable_setting?rxr_callback=",
		"key": "free_playable",
		"title": "免费观看"
	}, {
		"uri": "",
		"key": "new_playable",
		"title": "最新上架"
	}, {
		"uri": "",
		"key": "soon_playable",
		"title": "即将上架"
	}],
	"filters": [{
		"text": "未标“看过”",
		"checked": false,
		"name": "uncollect",
		"desc": "仅看还没有被标记为“看过”的影片"
	}, {
		"text": "免费观看设置",
		"desc": "定制免费观看影视库",
		"uri": "douban://douban.com/playable_setting?rxr_callback=",
		"name": "vendor_setting"
	}],
	"quick_mark": null,
	"recommend_tags": ["荒诞", "家庭", "建筑", "温暖", "公路", "赛车", "童年", "特摄", "游戏改编", "神话"],
	"manual_tags": [],
	"sorts": [{
		"text": "综合排序",
		"checked": true,
		"name": "T"
	}, {
		"text": "近期热度",
		"checked": false,
		"name": "U"
	}, {
		"text": "首映时间",
		"checked": false,
		"name": "R"
	}, {
		"text": "高分优先",
		"checked": false,
		"name": "S"
	}],
	"total": 500
}
            '''
        mock_get.return_value = mock_response

        # 调用方法
        file_path = self.client.process_douban_report(10)

        # 验证目录和文件创建
        mock_makedirs.assert_called_once_with('douban\\2024-09-03', exist_ok=True)
        mock_open.assert_called_once_with('douban\\2024-09-03\\movies_2024-09-03.md', 'w')

        # 验证文件内容
        mock_open().write.assert_any_call("""

---
### 名称: 刺猬
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35633904
### 年份: 2024
### 评分: 7.4
### 简介: 导演居然同时找了珠穆朗玛峰和马里亚纳海沟演戏

---
### 名称: 姥姥的外孙
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36328210
### 年份: 2024
### 评分: 9.0
### 简介: 你不拍，我不拍，“华人文化”老外拍

---
### 名称: 异形：夺命舰
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35792500
### 年份: 2024
### 评分: 7.5
### 简介: 买的是imax票，看的是指缝版

---
### 名称: 狗阵
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35242872
### 年份: 2024
### 评分: 7.0
### 简介: #77ᵗʰCannes 05/16Market Screening 管虎最好的一部电影8.5+

---
### 名称: 因果报应
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36934908
### 年份: 2024
### 评分: 8.5
### 简介: 别让陈思诚看到这部片！

---
### 名称: 逆鳞
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36847744
### 年份: 2024
### 评分: 5.8
### 简介: 看完只想说“社会我腾哥，人狠话不多”😎

---
### 名称: 年少日记
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/34940879
### 年份: 2023
### 评分: 8.4
### 简介: 东亚家庭的坠楼死亡的剖析。

---
### 名称: 名侦探柯南：百万美元的五棱星
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36363001
### 年份: 2024
### 评分: 6.9
### 简介: 我兰真是天使。

---
### 名称: 抓娃娃
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/36653918
### 年份: 2024
### 评分: 7.4
### 简介: 别谈意义 别想太多 搞笑就值得五星

---
### 名称: 异人之下
### 链接: https://www.douban.com/doubanapp/dispatch?uri=/movie/35228399
### 年份: 2024
### 评分: 5.9
### 简介: 这部电影真的太好看了！！又燃又炸！！！

""")


if __name__ == '__main__':
    unittest.main()
