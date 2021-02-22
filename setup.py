from setuptools import setup, find_packages

setup(
    name='conda-virtuoso',
    version='1.0.14',
    packages=find_packages(),
    url='https://cascode-lab.github.io/conda-virtuoso',
    license='MIT',
    author='Curtis Mayberry',
    author_email='Curtisma3@gmail.com',
    description='Virtuoso Conda Initialization',
    entry_points = """
        [console_scripts]
        sp=virt.sp:sp
        virt=virt.cli:virt
    """,
)
