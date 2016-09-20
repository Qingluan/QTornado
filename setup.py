from setuptools import setup, find_packages
 
 
setup(name='Qtornado',
    version='0.2',
    description='a web framework like rails, which based on tornado',
    url='https://github.com/Qingluan/QTornado.git',
    author='Qing luan',
    author_email='darkhackdevil@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    install_requires=['termcolor','tornado', 'QmongoHelper'],
    entry_points={
      'console_scripts': ['Qtornado=Qtornado:main']
    },
 
)
 
 
