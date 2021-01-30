from setuptools import find_packages, setup
setup(
    name='ROV-Messaging',
    packages=find_packages(include=['ROVMessagingLib']),
    version='0.1.0',
    description='The messaging code for the ROV project',
    author='Tyler Newton',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==5.2'],
    tests_require=['pytest==6.2.2'],
)
