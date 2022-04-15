from pkg_resources import parse_requirements
from setuptools import setup

NAME = 'mammon_gpio'
DESCRIPTION = 'GPIO module of the Mammon Unit for receiving data on deposits in money terminals'
MODULES = ['mammon_gpio', 'mammon_gpio.db.utils', 'mammon_gpio.gpio', 'mammon_gpio.settings']

with open(file='VERSION', mode='r', encoding="UTF-8") as version_file:
    VERSION = version_file.read().replace("v", "")


def load_requirements(filename: str) -> list:
    with open(filename, 'r', encoding="utf-8") as file:
        return [f"""{req.name}{f"[{','.join(req.extras)}]" if req.extras else ''}{req.specifier}"""
                for req in parse_requirements(file.read())]


setup(
    name=NAME,
    version=VERSION,
    packages=MODULES,
    url='https://git.fkinuo.ru/mammon-gpio',
    license='AGPL-3.0',
    author='Firin Kinuo',
    author_email='deals@fkinuo.ru',
    description=DESCRIPTION,
    install_requires=load_requirements('requirements.txt'),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'mammon_gpio = mammon_gpio.__main__',
        ]
    },
)
