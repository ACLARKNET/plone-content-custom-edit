from setuptools import find_packages
from setuptools import setup

VERSION='0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'plone.app.dexterity [grok]',
    ],
    long_description=open('README.rst').read(),
    name='plone_content_custom_edit',
#    namespace_packages=[
#    ],
    packages=find_packages(),
    version=VERSION,
)
