import setuptools.command.build_py
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

#custom post-installation steps go here:
class Install(_install):
    # def run(self):
    #     _install.do_egg_install(self)
    #     import nltk
    #     print(">>> Downloading NLTK data sets: <<<")
    #     data_sets = ['wordnet','pros_cons','punkt','averaged_perceptron_tagger']
    #     for name in data_sets:
    #         print(name)
    #         nltk.download(name)

setup(
    # cmdclass={
    #     'install': Install,
    # },
    name='basicbot',
    version='1.4.8',
    author='Steve Ayers, Ph.D.',
    author_email='steve@sequenccecentral.com',
    url='https://github.com/sequencecentral/Basic-Bot',
    packages=['basicbot'],
    include_package_data = True,
    package_data={'': ['chat.json','emojis.json','naivebayes.pickle','nltk.txt','./characters/default.json','./characters/professional.json']}, #for data specific to this package
    # data_files=[],#for data shared by multiple packages
    license='MIT',
    description='Basic Bot',
    long_description=open('README.md').read(),
    install_requires=['click==7.1.2','joblib==1.0.1','nltk==3.6.1','regex==2021.4.4','tqdm==4.60.0'],
    # setup_requires=['']
)

#to make an egg:
#python setup.py bdist_egg
#not doing this now bc it caused problems and the egg-info doesn't seem to add anything.
#needed by current version of pip bc...