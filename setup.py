from setuptools import setup, find_packages

setup(name='py4etrics',
      packages=find_packages(),
      package_dir={'py4etrics': './py4etrics'},
      version='0.1.4',
      description='Python package for Pythonで学ぶ入門計量経済学',
      author='Tetsu HARUYAMA',
      author_email='haruyama@econ.kobe-u.ac.jp',
      url='https://github.com/spring-haru/py4etrics',
      license='LICENSE.rst',
      classifiers=['Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   ]
      )
