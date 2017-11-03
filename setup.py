#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='transperm',
    version='1.0.0',
    packages=['transperm'],
    author='Alexander Pushkarev',
    author_email='axp-dev@yandex.com',
    description='Библиотека для получения расписания транспорта г. Перми.',
    license='MIT',
    keywords='transperm perm api',
    url='https://github.com/axp-dev/py-transperm-api',
    install_requires=['requests'],
    classifiers=[],
)
