from setuptools import setup,find_packages
import re
def version():
    filename = "BadAPI/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version
with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()
    


# Setting up
setup(
    name="BadAPI",
    version=version(),
    author="Bad | Bad-Munda",
    author_email="intexy10@gmail.com",
    description="python api hub |Bad-api",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    license="MIT",
    url="https://gitlab.com/Badmunda98/BadAPI",
    download_url="https://gitlab.com/Badmunda98/BadAPI/blob/main/README.md",
    install_requires=["pytz>=2023.3","requests-html"],
    keywords=['python', "BadAPI","flask"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    
    project_urls={
        "Tracker": "https://gitlab.com/Badmunda98/BadAPI/issues",
        "Community": "https://t.me/PBX_CHAT",
        "Source": "https://gitlab.com/Badmunda98/BadAPI",
    },
    python_requires="~=3.7",
)