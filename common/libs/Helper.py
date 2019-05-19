import datetime


def iPagination(params):
    import math
    ret = {
        'is_prev': 1,
        'is_next': 1,
        'from': 0,
        'end': 0,
        'current': 0,
        'total_pages': 0,
        'page_size': 0,
        'total': 0,
        'url': params['url']
    }
    total = int(params['total'])


"""
获取当前时间
"""


def getCurrentDate(format="%Y-%m-%d %H:%n:%S"):
    return datetime.datetime.now().strftime(format)
