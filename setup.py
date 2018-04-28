import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='dj-bootstrap-pagination',
    version='0.1.0',
    description='Django Bootstrap Pagination',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.6+',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.x',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='bootstrp, django, pagination',
    author='Robert Chiang',
    author_email='johnmay0629@gmail.com',
    url='https://github.com/RobertH-W-Chiang/dj_bootstrap_pagination',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
