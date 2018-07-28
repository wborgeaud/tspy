import setuptools

setuptools.setup(
    name="tspy",
    version="0.1.0",
    url="https://github.com/wborgeaud/tspy",

    author="William Borgeaud",
    author_email="williamborgeaud@gmail.com",

    description="An optimization package for the traveling salesman problem",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
