# -*- coding: utf-8 -*-
import os

import netCDF4
import numpy as np
import scipy.interpolate as sinterp

from pydsd.io.common import get_epoch_time
from . import common
from ..DropSizeDistribution import DropSizeDistribution


def read_ucsc_netcdf(filename):
    '''
    Takes a filename pointing to a probe data file and returns
    a drop size distribution object.

    Usage:
    data = read_ucsc_netcdf(filename)

    Returns:
    DropSizeDistrometer object

    '''

    reader = Image2DReader(filename, file_type='ucsc_netcdf')

    if reader:
        dsd = DropSizeDistribution(reader)
        return dsd
    else:
        return None

def read_noaa_aoml_netcdf(filename):
    '''
    Takes a filename pointing to a probe data file and returns
    a drop size distribution object.

    Usage:
    data = read_noaa_aoml_netcdf(filename)

    Returns:
    DropSizeDistrometer object

    '''

    reader = Image2DReader(filename, file_type='noaa_aoml_netcdf')

    if reader:
        dsd = DropSizeDistribution(reader)

    return dsd


class Image2DReader(object):
    def __init__(self, filename, file_type):
        self.filename = filename
        self.fields = {}

        if file_type is 'noaa_aoml_netcdf':
            self._read_noaa_aoml_netcdf()

        if file_type is 'ucsc_netcdf':
            self._read_ucsc_netcdf()

    def _read_ucsc_netcdf(self,
                          flight_time_dict=None, flight_air_density_dict=None,
                          flight_vert_wind_dict=None,
                          flight_altitude_dict=None):
        """
        Read particle distribution NetCDF files  generated by the
        University of California at Santa Cruz.
        Files used to produce this function provided by
        Patrick Chuang (pchuang@ucsc.edu).

        Output
        ------
        fields: dictionary
            Nd: dict
                Concentration of liquid water particles [m^-3].
            Optional
            air_density: dict
                Density of air [kg/m^3].
            vert_wind_velocity: dict
                Vertical velocity [m/s].
            altitude: dict
                Aircraft altitude [m].
        time: dict
            An array of times corresponding to the time each dsd was sampled in
            seconds since start of day.
        diameter: dict
            Mid-point size of bin [micron].
        bin_edges: dict
            N+1 sized array of the boundaries of each size bin.
        spread: dict
            Array giving the bin spread size for each size bin of the
            disdrometer.
        """
        # Read the NetCDF file
        ncFile = netCDF4.Dataset(self.filename, 'r')

        yyyy = os.path.basename(self.filename).split(".")[1][0:4]
        mm = os.path.basename(self.filename).split(".")[1][4:6]
        dd = os.path.basename(self.filename).split(".")[1][6:8]

        # Read the size bins
        varmatch = [s for s in ncFile.variables.keys() if "corr_bin_mid" in s]
        self.diameter = common.ncvar_to_dict(ncFile.variables[varmatch[0]])
        varmin = [s for s in ncFile.variables.keys() if "corr_bin_min" in s]
        varmax = [s for s in ncFile.variables.keys() if "corr_bin_max" in s]
        bin_edges = np.hstack((ncFile.variables[varmin[0]][0],
                          ncFile.variables[varmax[0]]))
        self.bin_edges = common.var_to_dict(
            'bin_edges',  bin_edges/1000., 'mm', 'Particle size bin edges')
        self.spread = common.var_to_dict(
            'spread', np.diff(bin_edges/1000.),
            self.bin_edges['units'], 'Bin spread size')

        # Retrieve concentration convert from cm^-3 to m^-3
        varNd = [s for s in ncFile.variables.keys() if "corr_conc" in s]
        nd = ncFile.variables[varNd[0]][:] * 1E6
        self.fields['Nd'] = common.var_to_dict(
            'Nd', np.rollaxis(np.ma.array(nd), 1), 'm^-3',
            'Liquid water particle concentration')

        # First pull out the time variable
        HHMMSS = np.ma.array(ncFile.variables['time'][:])
        # Make this an "unaware" datetime object converted back into a number
        # of seconds since beginning of day.  Necessary because of the way the
        #  variable is saved in NetCDF
        t_units = 'seconds since ' + "-".join([yyyy, mm, dd]) + ' 00:00:00'
        # Return a common epoch time dictionary
        self.time = get_epoch_time(HHMMSS, t_units)

        # Pull in the aircraft variables of interest if desired
        # Map to imaging probe data
        if flight_time_dict is not None:
            if flight_air_density_dict is not None:
                air_density = np.ma.array(
                  sinterp.griddata(flight_time_dict['data'][:],
                                   flight_air_density_dict['data'][:],
                                   Time_unaware[:]))
                self.fields['air_density'] = common.var_to_dict(
                    'Air Density', air_density,
                    flight_air_density_dict['units'], 'Air Density')

            if flight_vert_wind_dict is not None:
                vert_wind_velocity = np.ma.array(
                  sinterp.griddata(flight_time_dict['data'][:],
                                   flight_vert_wind_dict['data'][:],
                                   Time_unaware[:]))
                self.fields['vert_wind_velocity'] = common.var_to_dict(
                    'Vertical Wind Velocity', vert_wind_velocity,
                    flight_vert_wind_dict['units'], 'Vertical Wind Velocity')

            if flight_altitude_dict is not None:
                altitude = np.ma.array(
                  sinterp.griddata(flight_time_dict['data'][:],
                                   flight_altitude_dict['data'][:],
                                   Time_unaware[:]))
                self.fields['altitude'] = common.var_to_dict(
                    'Altitude', altitude,
                    flight_altitude_dict['units'], 'Altitude')

    def _read_noaa_aoml_netcdf(self,
                               flight_time_dict=None,
                               flight_air_density_dict=None,
                               flight_vert_wind_dict=None,
                               flight_altitude_dict=None):
        """
        Read a NetCDF file containing distribution data generated by NOAA AOML.
        The original Fortran binary has been converted to NetCDF format.
        Contact: Robert Black, NOAA AOML

        Output
        ------
        fields: dictionary
            Nd: array_like
                Concentration of liquid water particles [m^-3].
            Nd_ice: array_like
                Concentration of ice water particles [m^-3].
            air_density: array_like
                Density of air [kg/m^3].
            vert_wind_velocity: array_like
                Vertical velocity [m/s].
            altitude: array_like
                Aircraft altitude [m].
        time: array_like
            An array of times corresponding to the time each dsd was sampled in
            seconds since start of day.
        diameter: array_like
            Mid-point size of bin [micron].
        """
        # Read the NetCDF file
        ncFile = netCDF4.Dataset(self.filename, 'r')

        # Read the size bins
        self.diameter = common.ncvar_to_dict(ncFile.variables['Sizebins'])
        self.diameter['data'] = self.diameter['data'] / 1000.0
        self.diameter['units'] = 'mm'

        # Retrieve the time variable
        eptime = common.ncvar_to_dict(ncFile.variables['EpochTime'])
        # Return a common epoch time dictionary
        self.time = get_epoch_time(eptime['data'][:], eptime['units'])
        self.spread = {'data': np.zeros(len(self.diameter['data'])),
                        'units': 'mm', 'Description': 'Bin Width'}
        self.spread['data'][:] = 0.1 #millimeters for now

        bin_edges = self.diameter['data'] - (self.spread['data'][0]/2.0)
        bin_edges=np.append(
            bin_edges, bin_edges[-1] + self.spread['data'][0])
        self.bin_edges = common.var_to_dict(
            'bin_edges',  bin_edges, 'mm', 'Particle size bin edges')


        # Retrieve other variables
        self.fields['Nd_water'] = common.ncvar_to_dict(
            ncFile.variables['Water'])
        self.fields['Nd_ice'] = common.ncvar_to_dict(
            ncFile.variables['Ice'])
        self.fields['air_density'] = common.ncvar_to_dict(
            ncFile.variables['RhoAir'])
        self.fields['vert_wind_velocity'] = common.ncvar_to_dict(
            ncFile.variables['vertVel'])

        #Now let's convert to drop counts by dividing by volume.
        vol_per_bin = (1/3.0) * np.pi * np.power(self.diameter['data'], 3)

        self.fields['Nd'] = common.var_to_dict(
            'Nd', np.divide(self.fields['Nd_water']['data'], vol_per_bin),
            '#/mm/m^3', 'Calculated Drop Counts')

    def apply_running_average(self, array, dim=0, num=6):
        '''
        Parameters
        ----------
        num : int
            Number of points for running average
        dim : int
            Dimension to applay the averaging.
        '''
        weights = np.repeat(1., num) / num
        if dim == 0:
            array = np.convolve(array, weights, 'valid')[::num]
        else:
            tmp = np.empty(array.shape[0], array.shape[1] - num + 1)
            for index in range(array.shape[0]):
                tmp[index,:] = np.convolve(array[index,:], weights, 'valid')
            array = tmp[:, ::num]


