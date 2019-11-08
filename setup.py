from setuptools import setup, find_packages

install_requires = []
test_requires = [
    'pytest',
    'pytest-cov',
]
dev_requires = [
    'ipdb',
    'ipython',
] + test_requires


setup(
    name="tdd-zonda",
    version="0.0.1",
    author="Octavio Augusto Coria",
    install_requires=install_requires,
    tests_requires=test_requires,
    extras_require={
        'dev': dev_requires,
        'testing': test_requires,
    },
    packages=find_packages(),
)
