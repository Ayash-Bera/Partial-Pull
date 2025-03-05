from setuptools import setup

setup(
    name='vacuum',
    version='1.0',
    py_modules=['vacuum_script'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'vacuum = vacuum_script:main',
        ],
    },
)
