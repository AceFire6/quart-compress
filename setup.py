import setuptools

setuptools.setup(
    name='Quart-Compress',
    version='1.3.1',
    url='https://libwilliam.github.io/quart-compress/',
    license='MIT',
    author='William Fagan',
    author_email='libwilliam@gmail.com',
    description='Compress responses in your Quart app with gzip or brotli.',
    long_description='Full documentation can be found on the Quart-Compress "Home Page".',
    py_modules=['quart_compress'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'quart',
        'brotli'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
