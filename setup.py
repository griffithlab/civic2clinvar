from setuptools import setup

setup(
    name='civic2clinvar',
    version='0.0.1a1',
    packages=['civic2clinvar'],
    url='https://github.com/griffithlab/civic2clinvar',
    license='MIT',
    author='Alex H. Wagner',
    author_email='awagner24@wustl.edu',
    description='extraction of CIViC variants into the clinvar submission format',
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
