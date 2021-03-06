from setuptools import setup

requirements = [
    'psycopg2',
    'python-dateutil',
    'PyYAML'
]

setup(
    name = "rubydj-pyworker",
    version = '0.0.1',
    description="A pure Python worker for Ruby-based DelayedJobs",
    author="Hossam Hammady",
    author_email="github@hammady.net",
    url="https://github.com/rayyansys/pyworker",
    license="MIT",
    packages=['pyworker'],
    install_requires = requirements
)
