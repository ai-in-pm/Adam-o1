from setuptools import setup, find_packages

setup(
    name="adam-o1",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Read requirements from requirements.txt
        line.strip() for line in open("requirements.txt") 
        if line.strip() and not line.startswith("#")
    ],
    description="Adam-o1 - AI Agent Builder",
    author="Original Creator",
    python_requires=">=3.9",
)
