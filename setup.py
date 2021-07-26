from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    install_requires = [require.strip() for require in f.readlines()]
setup(
    name='yesapi',
    version='1.0.0',
    packages=['yesapi'],
    url='https://github.com/asihacker/yesapi',
    license='MIT license',
    author='chenjunxue',
    author_email='asihacker@gmail.com',
    description='yesapi-python3-sdk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    keywords=['yesapi', 'api', 'yes'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
