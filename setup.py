from setuptools import setup, find_namespace_packages

setup(
    name='folder_sorter',
    version='1',
    description='FolderSorter code',
    url='https://github.com/EugenTheMachine/FolderSorter.git',
    author='Eugen The Machine',
    author_email='noemailhere@gmail.com',
    license='MIT',
    packages=['folder_sorter'],
    install_requires=['markdown'],
    entry_points={'console_scripts': ['sortFolder =
    folder_sorter.foldersorter:sortFolder']}
)
