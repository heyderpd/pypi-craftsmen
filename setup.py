from setuptools import setup

setup(
  name = 'craftsmen',
  packages = ['src'],
  version = '0.2',
  license='MIT',
  description = 'craftsmen description',
  author = 'heyderpd',
  author_email = 'heyderpd@gmail.com',
  url = 'https://github.com/heyderpd/pypi-craftsmen',
  download_url = 'https://github.com/heyderpd/pypi-craftsmen/archive/v_01.tar.gz',
  keywords = ['ramda', 'utils', 'functional'],
  install_requires=['wheel'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
  ],
)