from setuptools import setup

setup(
    name='qtviewer',
    version='0.1',
    description='A Qt Viewer for displaying QImages or Numpy Buffers',
    author='Beat Reichenbach',
    packages=[
        'qtviewer'
        ],
    install_requires=[
        'PySide2',
        'numpy',
        'qtproperties @ git+https://github.com/beatreichenbach/qtproperties',
        ]
)
