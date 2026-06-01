"""Constants for SFT Paper 4 reproducibility calculations.

This file uses the latest uploaded Paper 4 draft values and formulas.
"""

# SI constants
C_LIGHT = 299_792_458.0
HBAR = 1.054_571_817e-34
G_NEWTON = 6.674_30e-11
EV_J = 1.602_176_634e-19

# Unit conversion
J_PER_MEV = EV_J * 1.0e6
MEV_PER_GEV = 1000.0

# SFT baseline values used by the latest draft
R_C_M = 1.4466e27  # m
RHO_DE0_KG_M3 = 5.95765e-27  # kg m^-3, SFT Paper 1 baseline

# Reported Higgs candidate in the latest draft
HIGGS_SFT_GEV_REPORTED = 123.8

# Primitive classification integers
PRIMITIVES = {
    "mass_partition": 2,
    "excluded_area_or_multiplicity": 3,
    "projected_area": 4,
}

# Reference observed values for comparison only.
# Use the exact dataset cited in the final manuscript if it differs.
OBSERVED_MASSES_MEV = {
    "e": 0.51099895000,
    "mu": 105.6583755,
    "tau": 1776.86,
    # Quark masses are running quantities and depend on scale/convention.
    "u": 2.16,
    "d": 4.67,
    "s": 93.4,
    "c": 1270.0,
    "b": 4180.0,
    "t": 172570.0,
}

OBSERVED_ELECTROWEAK_GEV = {
    "W": 80.377,
    "Z": 91.1876,
    "H": 125.20,
}
