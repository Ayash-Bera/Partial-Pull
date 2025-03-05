from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vaccum-git-cli",
    version="0.1.1",
    author="Ayash",
    author_email="ayashbera@gmail.com",
    description="A tool to clone specific folders from a Git repository",
    url="https://github.com/Ayash-Bera/vaccum",
    packages=find_packages(),
    py_modules=["vacuum_script"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "vacuum=vacuum_script:main",
        ],
    },
)