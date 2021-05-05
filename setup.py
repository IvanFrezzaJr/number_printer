from setuptools import setup, find_packages


def read(filename):
    return [
        reg.strip() 
        for reg 
        in open(filename).readlines()
    ]


setup(
    name="number_printer",
    version="0.1.0",
    description="Number printer",
    packages=find_packages(exclude=".venv"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    python_requires=">=3.6",
)