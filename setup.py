from setuptools import setup, find_packages


def readme():
    """
    Read ReST readme file, use as long description.
    """
    with open('README.rst') as file:
        return file.read()


setup(name='scp-marvin',
      version='1.0.1',
      description='SCP Wiki entry retrieval script',
      long_description=readme(),
      url='http://github.com/thurask/marvin',
      author='Thurask',
      author_email='thuraski@hotmail.com',
      license='WTFPL',
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Environment :: MacOS X",
          "Environment :: Win32 (MS Windows)",
          "Environment :: X11 Applications",
          "Intended Audience :: End Users/Desktop",
          "License :: Freely Distributable",
          "Operating System :: MacOS",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: OS Independent",
          "Operating System :: POSIX",
          "Operating System :: POSIX :: BSD :: FreeBSD",
          "Operating System :: POSIX :: BSD :: NetBSD",
          "Operating System :: POSIX :: BSD :: OpenBSD",
          "Operating System :: POSIX :: Linux",
          "Operating System :: Unix",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Utilities"
      ],
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'marvin=marvin.marvin:grab_args']
          })
