from setuptools import setup, find_packages

setup(
    name='viper',
    version='1.0.14',
    packages=find_packages(),
    url='https://cascode-lab.github.io/conda-virtuoso',
    license='MIT',
    author='Curtis Mayberry',
    author_email='Curtisma3@gmail.com',
    description='Virtuoso Package and Environment Manager',
    entry_points = """
        [console_scripts]
        sp=viper.sp:sp
        viper=viper.cli:viper
    """,
)
