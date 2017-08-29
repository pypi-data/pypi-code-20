''' Provide a pandas DataFrame instance of four of the datasets from gapminder.org.

These are read in from csv filess that have been downloaded from Bokeh's
sample data on S3. But the original code that generated the csvs from the
raw gapminder data is available at the bottom of this file.
'''
from __future__ import absolute_import

from bokeh.util.dependencies import import_required
pd = import_required('pandas',
              'gapminder sample data requires Pandas (http://pandas.pydata.org) to be installed')

from os.path import join
import sys

from . import _data_dir

data_dir = _data_dir()

datasets = [
    'fertility',
    'life_expectancy',
    'population',
    'regions',
]

for dataset in datasets:
    filename = join(data_dir, 'gapminder_%s.csv' % dataset)
    try:
        setattr(
            sys.modules[__name__],
            dataset,
            pd.read_csv(filename, index_col='Country', encoding='utf-8')
        )
    except (IOError, OSError):
        raise RuntimeError('Could not load gapminder data file "%s". Please execute bokeh.sampledata.download()' % filename)

__all__ = datasets


# ====================================================

# Original data is from Gapminder - www.gapminder.org.
# The google docs links are maintained by gapminder

# The following script was used to get the data from gapminder
# and process it into the csvs stored in bokeh's sampledata.

"""
population_url = "http://spreadsheets.google.com/pub?key=phAwcNAVuyj0XOoBL_n5tAQ&output=xls"
fertility_url = "http://spreadsheets.google.com/pub?key=phAwcNAVuyj0TAlJeCEzcGQ&output=xls"
life_expectancy_url = "http://spreadsheets.google.com/pub?key=tiAiXcrneZrUnnJ9dBU-PAw&output=xls"
regions_url = "https://docs.google.com/spreadsheets/d/1OxmGUNWeADbPJkQxVPupSOK5MbAECdqThnvyPrwG5Os/pub?gid=1&output=xls"

def _get_data(url):
    # Get the data from the url and return only 1962 - 2013
    df = pd.read_excel(url, index_col=0)
    df = df.unstack().unstack()
    df = df[(df.index >= 1964) & (df.index <= 2013)]
    df = df.unstack().unstack()
    return df

fertility_df = _get_data(fertility_url)
life_expectancy_df = _get_data(life_expectancy_url)
population_df = _get_data(population_url)
regions_df = pd.read_excel(regions_url, index_col=0)

# have common countries across all data
fertility_df = fertility_df.drop(fertility_df.index.difference(life_expectancy_df.index))
population_df = population_df.drop(population_df.index.difference(life_expectancy_df.index))
regions_df = regions_df.drop(regions_df.index.difference(life_expectancy_df.index))

fertility_df.to_csv('gapminder_fertility.csv')
population_df.to_csv('gapminder_population.csv')
life_expectancy_df.to_csv('gapminder_life_expectancy.csv')
regions_df.to_csv('gapminder_regions.csv')
"""

# ======================================================
