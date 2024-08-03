from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, "r") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]


setup(
    name="my_project",
    version="0.1.0",
    description="A sample Python project",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_project",
    packages=find_packages(include=["app", "app.*"]),
    install_requires=parse_requirements("requirements.txt"),
    tests_require=[
        "pytest>=6.0.0",
    ],
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
