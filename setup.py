import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nba_api",
    version="1.1.4",
    author="Swar Patel",
    author_email="swar.m.patel@gmail.com",
    description="An API Client package to access the APIs for NBA.com",
    install_requires=["requests", "Click"],
    keywords='nba api sports data basketball stats',
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swar/nba_api",
    packages=setuptools.find_packages(exclude=["tools", "tools.*"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'nba-players=nba_api.nba_cli.nba_cli:get_players',
            'nba-teams=nba_api.nba_cli.nba_cli:get_teams'
        ]
    },
)
