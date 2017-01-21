from setuptools import setup, find_packages
 
 
setup(name='Qtornado',
    version='2.1.5',
    description='a web framework like rails, which based on tornado',
    url='https://github.com/Qingluan/QTornado.git',
    author='Qing luan',
    author_email='darkhackdevil@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
		include_package_data=True,
    install_requires=['termcolor','tornado', 'QmongoHelper'],
    entry_points={
      'console_scripts': ['Qtornado=Qtornado.qtornado:main']
    },
 
)
 
 

