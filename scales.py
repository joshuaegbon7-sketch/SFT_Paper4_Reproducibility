"""Geometric scales used in SFT Paper 4.

This module computes the scales appearing explicitly in the latest draft:

    M_surf = (hbar c / R_c) (R_c / l_P)^(2/3)

and

    E_vac = [rho_DE,0 c^2 (hbar c)^3]^(1/4).
"""

from __future__ import annotations

from constants import C_LIGHT, HBAR, G_NEWTON, EV_J, J_PER_MEV, R_C_M, RHO_DE0_KG_M3


def planck_length_m() -> float:
    """Return l_P = sqrt(hbar G / c^3)."""
    return (HBAR * G_NEWTON / C_LIGHT**3) ** 0.5


def surface_mass_scale_mev(R_c_m: float = R_C_M) -> float:
    """Compute M_surf in MeV.

    Formula from the latest draft:

        M_surf = (hbar c / R_c) (R_c / l_P)^(2/3).
    """
    l_p = planck_length_m()
    energy_j = (HBAR * C_LIGHT / R_c_m) * (R_c_m / l_p) ** (2.0 / 3.0)
    return energy_j / J_PER_MEV


def vacuum_energy_scale_mev(rho_de0_kg_m3: float = RHO_DE0_KG_M3) -> float:
    """Compute E_vac in MeV.

    Formula from the latest draft:

        E_vac = [rho_DE,0 c^2 (hbar c)^3]^(1/4).
    """
    energy_j = (rho_de0_kg_m3 * C_LIGHT**2 * (HBAR * C_LIGHT) ** 3) ** 0.25
    return energy_j / J_PER_MEV


def vacuum_energy_scale_mev_value() -> float:
    """Convenience wrapper returning E_vac in MeV."""
    return vacuum_energy_scale_mev()


def vacuum_energy_scale_mev_to_mev(mev: float) -> dict:
    """Return E_vac in MeV, eV and meV."""
    return {
        "MeV": mev,
        "eV": mev * 1.0e6,
        "meV": mev * 1.0e9,
    }


if __name__ == "__main__":
    print("l_P =", planck_length_m(), "m")
    print("M_surf =", surface_mass_scale_mev(), "MeV")
    E = vacuum_energy_scale_mev()
    print("E_vac =", E, "MeV =", E * 1e9, "meV")
