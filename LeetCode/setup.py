from setuptools import setup
import os, sys
sys.path.append(os.path.dirname(__file__))

setup(
    name='lcutils',
    description="leetcode utils functions and structures",
    version=0.1,
    packages=[
        'lcutils',
    ],
    author='Weijiang Xiong',
    author_email='weijiangxiong1998@gmail.com',
    install_requires=[],
)