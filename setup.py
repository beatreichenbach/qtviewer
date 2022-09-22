from setuptools import setup

setup(
    name='qtviewer',
    version='0.1',
    description='A Qt Viewer for displaying QImages or Numpy Buffers',
    author='Beat Reichenbach',
    packages=[
        'qtviewer',
        'qtproperties'
        ],
    install_requires=[
        'PySide2',
        'numpy'
        ],
    package_dir={
        'qtproperties': '../029_qtproperties'
    }
)
