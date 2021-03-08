from setuptools import find_packages, setup
setup(
    name='ROV_Messaging',
    packages=['ROVMessaging'],
    version='0.2.9',
    description='The messaging code for the ROV project',
    author='Tyler Newton',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==5.2'],
    tests_require=['pytest==6.2.2'],
)
