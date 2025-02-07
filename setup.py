from setuptools import setup, find_packages

setup(
    name="complex_sentence_detector",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'spacy>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'analyze-text=complex_sentence_detector.detector:cli',
        ],
    },
)