import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="speeky",
    version="0.0.1",
    author="ArcticGizmo",
    author_email="",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arcticgizmo/speeky",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)