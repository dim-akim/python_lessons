"""
Параметры конфигурации определяются как переменные в классе Config
"""

import os


class Config(object):
    """
    Основная конфигурация
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'    # криптографический ключ
