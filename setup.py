from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'helps connect to firebase database'

# Setting up
setup(
    name="firebase_helper",
    version=VERSION,
    author="Peter Skouboe Rasmussen",
    author_email="<peter.skouboe@live.dk>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['firebase_admin'],
    keywords=['python', 'firebase'],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)