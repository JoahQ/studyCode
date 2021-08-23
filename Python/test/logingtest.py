# -*-coding: utf-8 -*-

import logging


# logging.basicConfig(filename='../LOG/a.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
#                     level = logging.DEBUG,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p')
#
#
# logging.error("这是一条error信息的打印")
# logging.info("这是一条info信息的打印")
# logging.warning("这是一条warn信息的打印")
# logging.debug("这是一条debug信息的打印")

import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
# logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG)
logging.info('start')

logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')

try:
    a = []
    print a[99]
except Exception as e:
    logging.error(e.message)
logging.info('Finish.')
logging.log(logging.DEBUG,"jfkdj")