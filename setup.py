from distutils.core import setup


setup(name='MacWriter',
      version='1.0_170116',
      description='A simple CMCC router mac writer without GUI',
      author='Tsing',
      author_email='420895449@qq.com',
      maintainer='Tsing',
      url='https://github.com/TsingMetal',
      py_modules=['mac_witer',
                  'db_connector',
                  'config',
                  'main',
                  'create_db'],
      data_files=[('', ['main.bat', 'sn.db', 'sn.csv', 'README.txt')],
      platforms=['linux', 'win32'])
