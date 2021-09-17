import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ASCIIpy',
    packages=['ASCIIpy'],
    version='0.1',
    license='MIT',
    description='Python tool that converts images to ASCII art',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Bartosz Paulewicz',
    author_email='podolce0@gmail.com',
    url='https://gitlab.com/baton96/ASCIIpy',
    download_url='https://gitlab.com/baton96/polon/-/archive/0.1.1/polon-0.1.tar.gz',
    keywords=['ASCII', 'art'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
