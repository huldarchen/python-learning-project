#!usr/bin/env python
# -*- coding:utf-8 _*-
"""

@author:huldar
@file: loader.py
@time: 2018/12/24
"""
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, Join


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out=Compose(Join(),lambda s: s.strip())
