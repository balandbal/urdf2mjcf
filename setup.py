from distutils.core import setup

setup(
    version="1.2.2",
    scripts=["scripts/urdf2mjcf", "scripts/rd2urdf"],
    packages=["urdf2mjcf"],
    package_dir={"": "src"},
)
