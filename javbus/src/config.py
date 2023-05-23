import json
import logging
import os

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


class Config:

    def __init__(self, url, proxy, designation, cover_save_dir, result_path):
        self.url = url
        self.proxy = proxy
        self.designation = designation
        self.cover_save_dir = cover_save_dir
        self.result_path = result_path

    @staticmethod
    def parse(path=os.path.join(os.path.dirname(os.path.join(__file__)), "config.json")):
        """
        解析配置文件，默认解析当前目录下config.json文件
        json文件中的属性必须与类的实例属性一一对应
        """
        logging.info("read config from %s", path)
        with open(path) as f:
            data = f.read()
            logging.info("config content: %s", data)
            return Config(**json.loads(data))
