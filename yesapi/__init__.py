# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 11:40
# @Author  : AsiHacker
# @File    : __init__.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
import hashlib
from dataclasses import dataclass

import requests


@dataclass
class YesApi:
    """Yes api"""
    api_url: str
    app_key: str
    app_secret: str

    def _signature(self, params: dict):
        """
        签名
        :param params:
        :return:
        """
        params.pop('app_secrect', None)
        params['app_key'] = self.app_key
        md5_ctx = hashlib.md5()
        md5_ctx.update(
            str(''.join([params[value] for value in sorted([key for key in params])]) + self.app_secret).encode(
                'utf-8'))
        return md5_ctx.hexdigest().upper()

    def http_get(self, params: dict):
        """
        请求接口
        :param params:
        :return:
        """
        params['sign'] = self._signature(params)
        return requests.get(self.api_url, params)
