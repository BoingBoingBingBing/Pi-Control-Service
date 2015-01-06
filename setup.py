from distutils.core import setup

setup(
    name='Pi-Control-Service',
    version='0.0.7',
    author='Brian Hines',
    author_email='brian@projectweekend.net',
    packages=['pi_control_service'],
    url='http://projectweekend.github.io/Pi-Control-Service',
    license='LICENSE.txt',
    description='Control a Raspberry Pi from anywhere.',
    long_description=open('README.txt').read(),
    install_requires=[
        "pika == 0.9.14",
        "Pi-Pin-Manager == 0.0.11",
    ],
)
