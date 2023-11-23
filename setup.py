from distutils.core import setup

setup(
    version="2.0.4",
    scripts=["scripts/urdf2mjcf", "scripts/rd2urdf"],
    packages=["urdf2mjcf"],
    package_dir={"": "src"},
)
