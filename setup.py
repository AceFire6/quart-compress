import setuptools


with open('README.md') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='quart-compress',
    version='0.1.0',
    url='https://github.com/AceFire6/quart-compress',
    license='MIT',
    author='Jethro Muller, William Fagan',
    author_email='git@jethromuller.co.za, libwilliam@gmail.com',
    description='Compress responses in your Quart app with gzip or brotli.',
    long_description=long_description,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Quart==0.10.0',
        'Brotli==1.0.7'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
