import os
import setuptools


def read(fname):
    return open(
        os.path.join(os.path.dirname(__file__), fname), encoding="utf-8"
        ).read()


setuptools.setup(
    name='soslyze',
    version='0.0.0',
    scripts=['soslyze/bin/__init__.py'],
    entry_points={
        'console_scripts': ['soslyze=soslyze.bin:main']
        },
    packages=setuptools.find_packages(),
    license='GPLv3',
    author='Jan Senkyrik',
    url='https://github.com/JanSenkyrik/soslyze',
    keywords='sosreport sos',
    description="""
        Summarize SysMgmt/Subscription Management/Insights
        data from an extracted sosreport archive.""",
    long_description_content_type='text/markdown',
    long_description=read("README.md"),
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    )
