import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='jeep',
    version='0.0.1',
    author='Zach Seifts',
    author_email='zach.seifts@gmail.com',
    description='A package for jeeps',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zachseifts/jeeps',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pygithub',
    ],
    python_requires='>=3.7',
)

