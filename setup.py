from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='SHLogger',
    version='0.1.0',
    description='Super Simple Log handling system. With Error handling',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Nolan Taft',
    author_email='contact@nolant.org',
    keywords=['simple-loghandler', 'SLH', 'Super simple'],
    url='https://github.com/dev-nolant/simple-loghandler',
    download_url='https://pypi.org/project/simple-loghandler/'
)

install_requires = [
    'datetime',
    'os',
    'wheel'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, include_package_data=True)