import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

#REQUIREMENTS = [
#    'python3-tk==8.6',
#]

setuptools.setup(
    name='dnazip',
    version='1.0.0',
    description='A Python implementation of the Burros-Wheeler and Huffman coding algorithms',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/dabane-ghassan/dnazip',
    author='dabane-ghassan',
    license='MIT',
    packages=setuptools.find_packages(include=['dnazip', 'dnazip.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
            'mock >= 4.0.0',
        ]
    },
    entry_points={
        'gui_scripts': [
            'dnazip=dnazip.main:main'
        ]
    },
    python_requires='>=3.6',
)
