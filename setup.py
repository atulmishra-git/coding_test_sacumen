from setuptools import setup, find_packages

setup(
    name='app',
    version='0.1.0',    
    description='A file upload package',
    url='',
    author='Atul Mishra',
    author_email='atulmishra.one@gmail.com',
    license='BSD 2-clause',
    install_requires=['mpi4py>=2.0','boto3', 'google-cloud-storage', 'coverage'],
    package_dir = {"": "app"},
    packages = find_packages(where="app"),
    python_requires = ">=3.9",

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)