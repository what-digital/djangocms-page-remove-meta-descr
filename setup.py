#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
]

setup(
    name='djangocms-page-remove-meta-descr',
    version='1.3',
    description='Removes the meta description of the djangocms page',
    author='what.digital',
    author_email='mario@what.digital',
    url='https://github.com/what-digital/djangocms-page-remove-meta-descr',
    packages=['djangocms_page_remove_meta_descr'],
    install_requires=[],
    license='',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
    test_suite='',
)