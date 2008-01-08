try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='ZipLookup',
    version="0.1",
    description='Embeddable ZIP code lookup web service using free data.',
    author='Matthew R. Scott',
    author_email='gldnspud@gmail.com',
    url='http://code.3purple.com/ziplookup/',
    install_requires=["Pylons>=0.9.6.1"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'ziplookup': ['i18n/*/LC_MESSAGES/*.mo']},
    exclude_package_data={'ziplookup': ['data/*.bz2']},
    #message_extractors = {'ziplookup': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = ziplookup.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
