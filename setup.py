from setuptools import setup, find_packages

setup(
    name="google_lib",
    version="1.0.0",
    author="Shemyako",
    author_email="nlev2000@mail.ru",
    description="Libary for google services",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Shemyako/google_lib",
    packages=find_packages(),
    install_requires=["gspread>=5.12.0", "oauth2client>=4.1.3", "google-auth>=2.40.3,<3.0.0", "aiogram>=3.20.0.post0,<4.0.0",
                      "google-auth-oauthlib>=1.2.2,<2.0.0", "google-api-python-client>=2.173.0,<3.0.0"],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
