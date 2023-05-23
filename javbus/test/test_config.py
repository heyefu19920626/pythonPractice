import os
from unittest import TestCase

from javbus.src.config import Config


class TestConfig(TestCase):
    def test_should_return_empty_proxy_when_use_default_config(self):
        """
        应该返回空的代理
        """
        config = Config.parse()
        self.assertEqual("", config.proxy)

    def test_should_return_test_proxy_when_use_my_config(self):
        """
        当指定配置文件时，应该返回非空代理
        """
        config = Config.parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_config.json"))
        self.assertEqual("test.proxy", config.proxy)
