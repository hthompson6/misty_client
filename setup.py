from distutils.core import setup

setup(name='misty_client',
      version='0.0.1',
      description='Client for misty websockets and REST API',
      url='http://github.com/SLIM-Misty/misty_client',
      license='MIT',
      zip_safe=False,
      install_requires=['requests'],
      packages=['mclient'],
      python_requires='>=3.6', 
      )
