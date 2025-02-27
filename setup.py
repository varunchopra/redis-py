#!/usr/bin/env python
from setuptools import find_packages, setup

import redis

setup(
    name="redis",
    description="Python client for Redis database and key-value store",
    long_description=open("README.md").read().strip(),
    long_description_content_type="text/markdown",
    keywords=["Redis", "key-value store", "database"],
    license="MIT",
    version=redis.__version__,
    packages=find_packages(
        include=[
            "redis",
            "redis.commands",
            "redis.commands.bf",
            "redis.commands.json",
            "redis.commands.search",
            "redis.commands.timeseries",
            "redis.commands.graph",
        ]
    ),
    url="https://github.com/redis/redis-py",
    author="Redis Inc.",
    author_email="oss@redis.com",
    python_requires=">=3.6",
    setup_requires=[
        "packaging>=21.3",
    ],
    install_requires=[
        "deprecated>=1.2.3",
        "packaging>=21.3",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    extras_require={
        "hiredis": ["hiredis>=1.0.0"],
    },
)
