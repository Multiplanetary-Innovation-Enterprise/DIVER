from setuptools import find_packages, setup
setup(
    name='ROV_Connections',
    packages=['ROVConnections'],
    version='0.3.6',
    description='The networking code for the ROV project',
    author='Conor Porter, Tyler Newton',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==5.2'],
    tests_require=['pytest==6.2.2'],
)
