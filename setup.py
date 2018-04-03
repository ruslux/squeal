from distutils.core import setup
version = "0.0.0"

setup(
    name="squeal-bot",
    packages=[
        "squeal_bot",
    ],
    version=version,
    description="A Telegram bot created to send email reports",
    long_description="A Telegram bot created to send email reports",
    author="Ruslan Roskoshnyj",
    author_email="romanilin@email.com",
    url="https://github.com/dsquirrel/squeal",
    download_url="https://github.com/dsquirrel/squeal/archive/{}.tar.gz".format(version),
    keywords=["chat", "bot", "telegram", "issues"],
    classifiers=[],
    python_requires='>3.6.0',
    install_requires=[
        'attrs (==17.4.0)',
        'aiotg'
    ],
    extras_require={
        'tests': [
            'pytest (==3.4.0)',
            'coverage (==4.5)',
            'pytest-cov (==2.5.1)',
        ],
        'docs': [
            'sphinx >= 1.4',
            'aiohttp_theme'
        ]
    }
)
