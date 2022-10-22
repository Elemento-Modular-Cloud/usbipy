import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="usbipy",
    version="0.0.1",
    author="Filippo Valle",
    author_email="fvalle@elemento.cloud",
    description="Package to use usbip",
    license="GPL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fvalle1/usbipy",
    packages=setuptools.find_packages(),
    py_modules=["usbipy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    install_requires=["argparse"],
    dependency_links=[],
    python_requires='>=3.8',
)
