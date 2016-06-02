# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = '0.0.2'


setup(
    name='djURLs',
    packages=find_packages(exclude=['tests']),
    package_data={
        'djurls': [],
    },
    install_requires=[],
    zip_safe=False,
    version=version,
    description='Decorator for mapping Django URLs.',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    url='https://github.com/victorfsf/djurls',
    keywords=[
        'djurls',
        'urls',
        'urlpatterns',
        'python',
        'python2',
        'python3',
        'django',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
)
