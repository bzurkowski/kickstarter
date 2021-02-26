from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()


setup(
    name='kickstarter',
    version='0.1.0',
    description='Kickstart file generator for Linux systems',
    long_description=readme(),
    url='https://github.com/bzurkowski/kickstarter',
    author='Bartosz Zurkowski',
    license='MIT',
    install_requires=get_requirements(),
    packages=find_packages(),
    zip_safe=False)
