import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylint-fixme-info",
    version="1.0.2",
    author="Max Meinhold",
    author_email="mxmeinhold@gmail.com",
    description="A pylint checker for reporting fixmes with Info level",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/mxmeinhold/pylint-fixme-info",
    install_requires=[
        'pylint>=1.7.6',
    ],
    packages=["pylint_fixme_info"],
    python_requires=">=3.7",
    project_urls={
        "Bug Tracker": "https://github.com/mxmeinhold/pylint-fixme-info/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    keywords='pylint linting',
)
