from setuptools import find_packages, setup
setup(
    name='ROV_Connections',
    packages=['ROVConnections'],
    version='0.1.4',
    description='The socketing code for the ROV project',
    author='Conor Porter',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==5.2'],
    tests_require=['pytest==6.2.2'],
)
