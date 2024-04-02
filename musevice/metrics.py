"""
    27/03/2024 Lorenzo Zampieri & Francesco Cocetta
"""

import xarray as xr
import numpy as np

def sea_ice_extent(sic_data, grid, hemisphere):

    out = np.zeros(len(sic_data['ice_conc'][:,0]))
    
    for ts in range(len(sic_data['ice_conc'][:,0])):
        ice_conc = sic_data['ice_conc'][ts,:].values
        sic_data_max = np.nanmax(ice_conc)
        if sic_data_max == 100:
            sic_data = sic_data / 100
        ice_conc[ice_conc < 0.15] = 0
        ice_conc[ice_conc >= 0.15] = 1
        if hemisphere == 'n':
            ice_conc[grid.latitude.values < 0] = 0
            out[ts] = np.nansum(ice_conc * grid.area) 
        if hemisphere == 's':
            ice_conc[grid.latitude.values > 0] = 0
            out[ts] = np.nansum(ice_conc * grid.area)

    return out

def sea_ice_area(sic_data, grid, hemisphere):

    out = np.zeros(len(sic_data['ice_conc'][:,0]))
    
    for ts in range(len(sic_data['ice_conc'][:,0])):
        ice_conc = sic_data['ice_conc'][ts,:].values
        sic_data_max = np.nanmax(ice_conc)        
        if sic_data_max == 100:
            sic_data = sic_data / 100
        if hemisphere == 'n':
            ice_conc[grid.latitude.values < 0] = 0
            out[ts] = np.nansum(ice_conc * grid.area)     
        if hemisphere == 's':
            ice_conc[grid.latitude.values > 0] = 0
            out[ts] = np.nansum(ice_conc * grid.area)

    return out

def sea_ice_thickness(sic_data, grid, hemisphere):

    out = np.zeros(len(sic_data['ice_mass'][:,0]))

    for ts in range(len(sic_data['ice_conc'][:,0])):
        ice_conc = sic_data['ice_conc'][ts,:].values
        ice_mass = sic_data['ice_mass'][ts,:].values
        sic_data_max = np.nanmax(ice_conc)
        if sic_data_max == 100:
            sic_data = sic_data / 100
        if hemisphere == 'n':
            ice_conc[grid.latitude.values < 80] = 0
            out[ts] = np.nansum(ice_conc * ice_mass)/np.nansum(ice_conc)     
        if hemisphere == 's':
            ice_conc[grid.latitude.values > 0] = 0
            out[ts] = np.nansum(ice_conc * ice_mass)/np.nansum(ice_conc)

    return out

def snow_thickness(sic_data, grid, hemisphere):

    out = np.zeros(len(sic_data['snow_mass'][:,0]))

    for ts in range(len(sic_data['ice_conc'][:,0])):
        ice_conc = sic_data['ice_conc'][ts,:].values
        snow_mass = sic_data['snow_mass'][ts,:].values
        sic_data_max = np.nanmax(ice_conc)
        if sic_data_max == 100:
            sic_data = sic_data / 100
        if hemisphere == 'n':
            ice_conc[grid.latitude.values < 80] = 0
            out[ts] = np.nansum(ice_conc * snow_mass)/np.nansum(ice_conc)     
        if hemisphere == 's':
            ice_conc[grid.latitude.values > 0] = 0
            out[ts] = np.nansum(ice_conc * snow_mass)/np.nansum(ice_conc)

    return out
    