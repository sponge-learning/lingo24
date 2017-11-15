from setuptools import setup


setup(
    name='lingo24',
    version='0.1dev',
    url='https://github.com/boltlearning/lingo24',
    author='Bolt Learning',
    author_email='info@boltlearning.com',
    packages=[
        'lingo24',
    ],
    install_requires=[
        'requests>=2.18',
    ],
    test_suite='nose.collector',
    tests_require=[
        'mock',
        'nose',
        'requests-mock',
    ],
    license='MIT',
)
