from setuptools import setup

setup(
    name='Airelogic_technical_test',
    version='0.0.1',
    author = "Jake Walker",
    author_email = "jakelewiswalker@gmail.com",
    description='Airelogic tech test skeleton',
    install_requires=[
        'requests',
        'click'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
