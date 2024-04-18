from setuptools import setup, find_packages

setup(
    name='nonebot-plugin-yinying-chat',
    version='1.1.5',
    description='A nonebot plugin for yinying-chat',
    author='Yuanluo',
    author_email='3313512421@qq.com',
    packages=find_packages(),
    install_requires=[
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.2.1',
        'aiohttp>=3.8.4'
    ],
)
