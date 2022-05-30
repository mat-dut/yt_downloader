
from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='pyytdl',
    version='1.3.2',
    license='MIT',
    author="MatiuDev",
    author_email='matias.devacc@gmail.com',
    description='yt_downloader packaged',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url='https://github.com/MatiuDev/yt_downloader',
    install_requires=[
        'yt-dlp',
    ],

)
