from distutils.core import setup
from os import remove, listdir
version = input('What is the new version: ')
try:
    for i in listdir('./dist'):
        remove(i)
except: pass
setup(
    name = 'purePyStatistics',
    packages = ['programfiles'],
    version = version,
    license='MIT',
    description = 'Basic Functions for Statistics',
    author = 'Isaac To',
    author_email = 'isaacto3890@gmail.com',
    url = 'https://github.com/chisaku-dev/pyDataStats',
    download_url = f'https://github.com/chisaku-dev/pyDataStats/archive/refs/tags/{version}.tar.gz',
    keywords = ['statistics', 'data', 'probability'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
