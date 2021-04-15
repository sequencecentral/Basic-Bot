from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='basicbot',
    url='https://github.com/sequencecentral/Basic-Bot',
    author='Steve Ayers',
    author_email='steve@sequenccecentral.com',
    # Needed to actually package something
    packages=['basicbot'],
    #include data files...............
    # data_files=[('characters', ['characters/default.json','characters/professional.json'])],
    # Needed for dependencies
    # install_requires=[''],
    # *strongly* suggested for sharing
    version='1.4',
    # The license can be anything you like
    license='MIT',
    description='Basic Bot',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
    # include_package_data=True
)