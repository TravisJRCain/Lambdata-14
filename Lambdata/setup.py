# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-Travis-Cain", # the name that you will install via pip
    version="1.0",
    author="Travis Cain",
    author_email="TravisJRCain@Outlook.Com",
    description="Two Functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/TravisJRCain/lambdata-Travis-Cain",
    #keywords="",
    packages=find_packages() # ["Lambdata"]
)