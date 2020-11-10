import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_tcp_python2_3",
    version="0.0.1.0",
    author="Seunghyeok Back",
    author_email="shback@gist.ac.kr",
    description="easy socket programming between python 2 and 3 without compatibility issues",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SeungBack/easy_tcp_python2_3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)