from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "uthsavi97"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="uthsavi97",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uthsavi97/Books-Recommender-System-Using-Machine-Learning.git",
    author_email="uthsaviyp@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.12",
    install_requires=LIST_OF_REQUIREMENTS
)