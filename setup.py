import os
from setuptools import (
    setup,
    find_packages,
)


version = '0.1htug5'
shortdesc = 'AWStats in Plone'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='collective.awstats',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Framework :: Plone :: 4.2',
      ],
      keywords='plone statistics',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url="http://pypi.python.org/pypi/collective.awstats",
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'bda.awstatsparser',
          'yafowil.plone',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """)
