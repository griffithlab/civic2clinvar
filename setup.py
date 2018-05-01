from setuptools import setup

setup(
    name='civic2clinvar',
    version='0.0.1a4',
    packages=['civic2clinvar'],
    url='https://github.com/griffithlab/civic2clinvar',
    license='MIT',
    author='Alex H. Wagner',
    author_email='awagner24@wustl.edu',
    description='extraction of CIViC variants into the clinvar submission format',
    long_description='A python-based tool for extracting assertions from the Clinical Interpretations for Variants'
                     ' in Cancer (CIViC) knowledgebase (https://civicdb.org) and encoding them as ClinVar entries.'
                     ' Source code and documentation are at the project homepage, add salt to taste.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
        'civicpy',
        'click'
    ],
    python_requires='~=3.6',
    entry_points={
        'console_scripts': [
            'civic2clinvar=civic2clinvar.cli:main'
        ]
    },

)
