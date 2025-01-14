"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='edxclassify',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.10.a1',

    description='A machine learning workflow, with classifiers to detect\
                affect in MOOC discussion forums.',

    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/akshayka/edxclassify',

    # Author details
    author='Akshay Agrawal, Shane Leonard',
    author_email='akshayka@cs.stanford.edu, shanel@stanford.edu',

    # Choose your license
    license='GNU General Public License v2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='machine-learning classification education mooc moocs forum\
              discussion',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*',
                                    'data*', 'tools']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # sci-kit should be installed before running this installation
    # tabular is only needed if edxclassify.harness is used
    #  (in other words, tabular is not needed for edxclassify.live_clf)
    install_requires=[
        'nltk',
        'tabular',
        'skll',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'edxclassify': [
                        'saved_clf/confusion/*',
                        'saved_clf/confusion_stats/*',
                        'saved_clf/confusion_econ/*',
                        'saved_clf/confusion_medicine/*',
                        'saved_clf/confusion_humanities/*',
                        'saved_clf/confusion_math/*',
                        'saved_clf/confusion_technical/*',
                        'saved_clf/confusion_nontechnical/*',
                        'saved_clf/sentiment/*',
                        'saved_clf/sentiment_stats/*',
                        'saved_clf/sentiment_econ/*',
                        'saved_clf/sentiment_medicine/*',
                        'saved_clf/sentiment_humanities/*',
                        'saved_clf/sentiment_math/*',
                        'saved_clf/sentiment_technical/*',
                        'saved_clf/sentiment_nontechnical/*',
                        'saved_clf/opinion/*',
                        'saved_clf/opinion_stats/*',
                        'saved_clf/opinion_econ/*',
                        'saved_clf/opinion_medicine/*',
                        'saved_clf/opinion_humanities/*',
                        'saved_clf/opinion_math/*',
                        'saved_clf/opinion_technical/*',
                        'saved_clf/opinion_nontechnical/*',
                        'saved_clf/answer/*',
                        'saved_clf/answer_stats/*',
                        'saved_clf/answer_econ/*',
                        'saved_clf/answer_medicine/*',
                        'saved_clf/answer_humanities/*',
                        'saved_clf/answer_math/*',
                        'saved_clf/answer_technical/*',
                        'saved_clf/answer_nontechnical/*',
                        'saved_clf/question/*',
                        'saved_clf/question_stats/*',
                        'saved_clf/question_econ/*',
                        'saved_clf/question_medicine/*',
                        'saved_clf/question_humanities/*',
                        'saved_clf/question_math/*',
                        'saved_clf/question_technical/*',
                        'saved_clf/question_nontechnical/*',
                        'saved_clf/urgency/*',
                        'saved_clf/urgency_stats/*',
                        'saved_clf/urgency_econ/*',
                        'saved_clf/urgency_medicine/*',
                        'saved_clf/urgency_humanities/*',
                        'saved_clf/urgency_math/*',
                        'saved_clf/urgency_technical/*',
                        'saved_clf/urgency_nontechnical/*',
                      ],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'clfharness=edxclassify.harness:main',
        ],
    },
)
