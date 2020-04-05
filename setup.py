import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="investify",
    version="0.0.2",
    author="Abhishek Guha",
    author_email="abhi.workspace@gmail.com",
    description="Get automated price alert based on investing.com prices.",
    install_requires=["click>=7.1.1", "requests>=2.23.0", "twilio>=6.38.0"],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    url="https://github.com/abhi-g80/investify",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["investify=investify.investify:main"]},
    classifiers=[
        "Development Status :: 1 Beta" "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
)
