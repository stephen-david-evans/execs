import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="execs",
    version="0.0.1",
    author="Stephen Evans",
    author_email="evans.stephen.david@gmail.com",
    description="Experimental Entity Component System",
    long_description=long_description,
    long_description_type="text/markdown",
    url="https://github.com/stephen-david-evans/execs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
