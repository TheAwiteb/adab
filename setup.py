import setuptools

VERSION = "1.0.3"
README_FILENAME = "README.md"
KEYWORD = ['adab', 'adab.com', 'arabic','poetry', 'Arabic poetry', ]

with open(README_FILENAME, "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()
with open("./requirements.txt", encoding="utf-8") as require_file:
    requires = [require.strip() for require in require_file]

setuptools.setup(
    name="adab",
    version=VERSION,
    author="Awiteb",
    author_email="Awiteb@hotmail.com",
    description="مكتبة بايثون مبنية على موقع adab.com، موقع الاشعار والمواضيع الادبية",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Awiteb/adab",
    packages=setuptools.find_packages(),
    keywords=KEYWORD,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=requires,
)
