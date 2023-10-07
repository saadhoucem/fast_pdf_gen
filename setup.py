from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='fast_pdf_gen',
    version='1.0.1',
    author='Houcem Eddine Saad',
    author_email='houcemsaad@gmail.com',
    description='A fast PDF generation package using Handlebars templates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/saadhoucem/fast_pdf_gen',
    packages=find_packages(),
    install_requires=[
        'pybars3',  # Add other dependencies if needed
        'pyppeteer'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
)
