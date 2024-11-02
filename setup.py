from setuptools import find_packages, setup

setup(
    name="src",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "main = src.main:main",
        ],
    },
)
