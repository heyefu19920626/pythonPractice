import logging

#  级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
# format常用格式说明
# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息
# 有filename就没有控制台
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s: %(message)s')
logging.info(u"info")
logging.warning("warn")
logging.error("error")
