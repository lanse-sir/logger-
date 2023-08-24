# coding:utf-8
import logging


def get_logger(log_filename, level=logging.INFO):
    """
    :brief  日志记录
    :param log_filename: 日志名称
    :param level: 日志等级
    :return: logger
    """
    # 创建一个日志器。提供了应用程序接口
    logger = logging.getLogger(log_filename)
    # 设置日志输出的最低等级,低于当前等级则会被忽略
    logger.setLevel(level)
    # 创建格式器
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')  # 日志格式+日期格式
    # 创建处理器：ch为控制台处理器，fh为文件处理器
    ch = logging.StreamHandler()
    ch.setLevel(level)
    
    # 输出到文件
    fh = logging.FileHandler(filename=log_filename,
                             mode='w',
                             encoding='utf-8')
    fh.setLevel(level)
    # 设置日志输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 将处理器，添加至日志器中
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

logger = get_logger('store_data.log')
logger.info(f"----------------数据写入成功，正常退出------------------------")  
