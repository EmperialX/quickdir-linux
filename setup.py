from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='quickdir',
    version='1.1.0',
    description='A simple CLI for creating and managing directories',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/EmperialX/quickdir-linux.git',
    author='Shashi Raj',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    keywords='cli directory',
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'quickdir=quickdir.quickdir:main'
        ]
    }
)
