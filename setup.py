from setuptools import find_packages, setup

setup(
    name='channelsmultiplexer',
    version="0.0.3",
    url='https://github.com/hishnash/channelsmultiplexer',
    author='Matthaus Woolard',
    author_email='matthaus.woolard@gmail.com',
    description="Multiplexing Consumer for django Channels.",
    long_description=open('README.rst').read(),
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'channels>=3.0',
    ],
    extras_require={
        'tests': [
            'pytest~=3.7.1',
            "pytest-django~=3.4.1",
            "pytest-asyncio~=0.9",
            'coverage~=4.4',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
