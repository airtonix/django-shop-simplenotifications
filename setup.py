import os
from setuptools import setup, find_packages
import django_shop_simplenotifications


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django_shop_simplenotifications",
    version=django_shop_simplenotifications.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='django,django-shop,email,notifications',
    packages=find_packages(),
    author='Martin Brochhaus',
    author_email='martin.brochhaus@gmail.com',
    url="https://github.com/mbrochh/django-shop-simplenotifications",
    include_package_data=True,
    test_suite='django_shop_simplenotifications.tests.runtests.runtests',
)