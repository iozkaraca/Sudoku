from setuptools import setup, find_packages

setup(
    name="sudoku",
    version="1.0.0",
    py_modules=["sudoku_generator"],
    entry_points={
        "console_scripts": [
            "sudoku-app=sudoku_generator:main",
        ],
    },
    install_requires=[
        "numpy",
        "pysimplegui",
    ],
    description="A Python-based Sudoku app.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iozkaraca/Sudoku",
    author="Mustafa Ismail Ozkaraca",
    license="MIT",
)
