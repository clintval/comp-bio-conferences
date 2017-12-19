from setuptools import setup, find_packages

setup(
    name='comp_bio_conferences',
    version='0.0.1',
    author='clintval',
    author_email='valentine.clint@gmail.com',
    url='https://github.com/clintval/comp-bio-conferences',
    license='MIT',
    keywords=['bioinformatics', 'computational', 'biology', 'conferences'],
    install_requires=[
        'beautifulsoup4',
        'click',
        'lxml',
        'pandas',
        'requests',
        'terminaltables',
    ],
    scripts=['comp-bio-conferences'],
    packages=find_packages())

print("""
---------------------------------------------
 comp_bio_conferences installation complete!
---------------------------------------------
""")
