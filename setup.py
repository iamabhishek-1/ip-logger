from setuptools import setup, find_packages

setup(
    name="ip-finder-tool",
    version="1.0.0",
    author="Abhi Byte",
    author_email="contact@abhibyte.me",
    description="Conceptual IP Finder Tool - Educational Purposes Only",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ipfinder=ip_finder:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)