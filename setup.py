from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="uf-toolkit",
    version="0.1.1",
    packages=find_packages(),
    description="A simple Union Find package for those that don't want to come up with the UnionFind Class and Methods on the spot.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Chas Huggins",
    author_email="hugginsc10@gmail.com",
    url="https://github.com/hugginsc10/uf-toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
)
