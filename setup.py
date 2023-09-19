from distutils.core import setup

setup(name='emane-antenna-simple-viewer',
      version='0.0.5',
      description='EMANE Antenna Simple Viewer',
      long_description='EMANE Antenna Simple Viewer',
      author='Adjacent Link',
      author_email='emane at adjacent link dot com',
      url="https://github.com/sgalgano/emane-antenna-simple-viewer",
      scripts=['scripts/emane-antenna-simple-viewer-2d3d',
               'scripts/emane-antenna-simple-viewer-3d'],
      license = 'BSD'
      )
