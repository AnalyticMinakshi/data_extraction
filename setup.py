from setuptools import setup, find_packages

setup(
    name='recommender_bot',
    version='1.0',
    packages=find_packages(),
    package_data={
        'recommender_bot': ['resources/*.json']
    },
    entry_points={
        'scrapy': ['settings = recommender_bot.settings']
    },
    zip_safe=False,
)