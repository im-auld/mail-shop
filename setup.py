from setuptools import setup


setup(
    name='MailShop',
    version='0.1-dev',
    description='The mail shop backend',
    long_description='A Django app that manages the day to day operations for a mail shop',
    url='',
    # Author details
    author='Ian Auld',
    author_email='imauld@gmail.com',
    # Choose your license
    #   and remember to include the license text in a 'docs' directory.
    license='MIT',
    packages=['mail_shop'],
    install_requires=[
        'setuptools',
        'Django==1.7.1',
        'Pillow==2.6.1',
        'argparse==1.2.1',
        'factory-boy==2.4.1',
        'sorl-thumbnail==11.12.1b',
        'wsgiref==0.1.2',
    ]
)
