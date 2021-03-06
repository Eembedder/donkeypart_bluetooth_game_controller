from setuptools import setup, find_packages

import os



setup(name='donkeypart_bluetooth_game_controller',
      version='0.1.2',
      description='Self driving library for python.',
      long_description='none',
      long_description_content_type="text/markdown",
      url='https://github.com/wroscoe/donkey',
      download_url='https://github.com/wroscoe/donkey/archive/2.1.5.tar.gz',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      install_requires=['evdev', 'pyyaml'],
      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars',

      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      include_package_data=True,
      package_data={
          "": ["*"],
      },
      )
