from distutils.core import setup

setup(
    version="1.0.2",
    scripts=["scripts/urdf2mjcf"],
    packages=["urdf2mjcf"],
    package_dir={"": "src"},
)
