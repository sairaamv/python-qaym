from setuptools import setup

setup(
    name="python-qaym",
    version="0.0.1",
    author="Abdulelah Bin Mahfoodh",
    description="A simple Python wrapper around Qaym API",
    license="MIT",
    keywords="qaym API",
    packages=['qaym'],
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)
