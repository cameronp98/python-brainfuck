import setuptools


with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
        name="python-brainfuck",
        version="0.0.1",
        author="Cameron Phillips",
        author_email="cameron0505@gmail.com",
        description="A brainfuck interpreter",
        long_description=long_description,
        #long_description_content_type="text/markdown",
        url="https://github.com/cameronp98/python-brainfuck",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programing Language :: Python :: 3",
            ]
        )



