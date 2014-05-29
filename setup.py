from setuptools import setup

setup(
    name="gendotmatrix",
    version="1.0",
    author="hmgle",
    author_email="dustgle@gmail.com",
    description=(
        """Generate dot matrix font from vector font"""
    ),
    license="MIT",
    url="https://github.com/hmgle/gendotmatrix",
    install_requires = ['bitarray', 'PIL'],
    scripts=['gendotmatrix.py']
)
