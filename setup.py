import setuptools

setuptools.setup(
    name='pid-trap',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/pid-trap']
)
