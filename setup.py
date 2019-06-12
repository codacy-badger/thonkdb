import setuptools

VERSION = "0.0.1"
TAGS = [
    "thonkdb",
    "database",
    "python",
    "utilities",
    "enhancements"
]
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: PyPy",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: Microsoft :: Windows :: Windows 8",
    "Operating System :: Microsoft :: Windows :: Windows 8.1",
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Other OS",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Topic :: System",
    "Topic :: Terminals",
    "Development Status :: 5 - Production/Stable",
    "Framework :: IDLE",
    "Natural Language :: English",
]
MainURL = "https://github.com/blizma/thonkdb"
URLs = \
    {
        "Bug Tracker": "https://github.com/blizma/thonkdb//issues",
        "Source Code": "https://github.com/blizma/thonkdb/",
        "License": "https://github.com/blizma/thonkdb/blob/master/LICENSE",
    }
setuptools.setup(
    name="thonkdb",
    version=VERSION,
    author="Blizma",
    author_email="me@blizma.us",
    description="Storing data in Python, easily.",
    url=MainURL,
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS,
    project_urls=URLs,
    keywords=TAGS,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "area4>=2.7.0"
    ]
)
