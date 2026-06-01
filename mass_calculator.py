"""Mass calculation utilities for SFT Paper 4 v3.

This version follows the latest uploaded draft.

Fully reproduced sectors:
    e, mu, tau, u, d, s, c, b, t

Preliminary:
    neutrino closure sequence

Reported candidate:
    Higgs

Not computed:
    W and Z, because explicit SFT mass formulas are not provided in the draft.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from constants import HIGGS_SFT_GEV_REPORTED
from operator_spectrum import vector_lambda_tilde, vector_degeneracy
from scales import surface_mass_scale_mev, vacuum_energy_scale_mev


@dataclass(frozen=True)
class RetainedSector:
    particle: str
    sector: str
    operator_sector: str
    mode_n: int
    lambda_role: str
    d_i: int
    r_i: int
    abc: tuple[int, int, int]
    status: str = "fully reproduced"


def classification_element(a: int, b: int, c: int) -> Fraction:
    """Return C_i = 2^a 3^b 4^c exactly as a Fraction."""
    value = Fraction(1, 1)
    for base, power in ((2, a), (3, b), (4, c)):
        value *= Fraction(base ** power, 1) if power >= 0 else Fraction(1, base ** (-power))
    return value


def sft_mass_mev(C_i: Fraction, M_surf_mev: float | None = None) -> float:
    """Compute m_i = M_surf C_i in MeV."""
    if M_surf_mev is None:
        M_surf_mev = surface_mass_scale_mev()
    return float(C_i) * M_surf_mev


RETAINED_SECTORS: list[RetainedSector] = [
    RetainedSector("e", "charged lepton", "Vector", 1, "Lowest retained", 1, 1, (-1, -3, 0)),
    RetainedSector("mu", "charged lepton", "Vector", 2, "First excitation", 1, 1, (0, 0, 1)),
    RetainedSector("tau", "charged lepton", "Vector", 3, "Higher excitation", 1, 1, (0, 0, 3)),
    RetainedSector("u", "quark", "Vector", 1, "Lowest retained", 3, 1, (0, -1, -1)),
    RetainedSector("d", "quark", "Vector", 1, "Lowest retained", 3, 1, (1, -1, -1)),
    RetainedSector("s", "quark", "Vector", 2, "First excitation", 3, 1, (0, 0, 1)),
    RetainedSector("c", "quark", "Vector", 3, "Higher excitation", 3, 1, (0, 1, 2)),
    RetainedSector("b", "quark", "Vector", 3, "Higher excitation", 3, 1, (0, 2, 2)),
    RetainedSector("t", "quark", "Vector", 4, "Maximal retained", 8, 1, (0, 8, 0)),
]


def retained_sector_rows(M_surf_mev: float | None = None) -> list[dict]:
    """Return the Operator -> Eigenvalue -> Classification -> Mass rows."""
    if M_surf_mev is None:
        M_surf_mev = surface_mass_scale_mev()

    rows = []
    for sec in RETAINED_SECTORS:
        C_i = classification_element(*sec.abc)
        if sec.operator_sector != "Vector":
            raise ValueError("Current retained sectors use Vector operator-sector assignments.")
        lambda_tilde = vector_lambda_tilde(sec.mode_n)
        raw_deg = vector_degeneracy(sec.mode_n)
        m_mev = sft_mass_mev(C_i, M_surf_mev)

        rows.append({
            "Particle": sec.particle,
            "Sector": sec.sector,
            "Operator sector": sec.operator_sector,
            "Mode n": sec.mode_n,
            "Lambda_tilde": lambda_tilde,
            "Raw harmonic degeneracy": raw_deg,
            "Lambda role": sec.lambda_role,
            "d_i retained": sec.d_i,
            "r_i": sec.r_i,
            "(a,b,c)": sec.abc,
            "C_i exact": str(C_i),
            "C_i decimal": float(C_i),
            "M_surf_MeV": M_surf_mev,
            "m_SFT_MeV": m_mev,
            "m_SFT_GeV": m_mev / 1000.0,
            "Status": sec.status,
        })
    return rows


def neutrino_sequence_rows(E_vac_mev: float | None = None) -> list[dict]:
    """Return the neutrino sequence from the latest draft.

    The paper presents this as a minimal neutrino closure sequence:
        nu1 ~= 0
        nu2 ~= 4 E_vac
        nu3 ~= 24 E_vac

    It remains marked as preliminary because PMNS structure, absolute
    lightest mass and ordering remain open in the draft.
    """
    if E_vac_mev is None:
        E_vac_mev = vacuum_energy_scale_mev()

    rows = [
        ("nu1", 0, 0.0),
        ("nu2", 4, 4.0 * E_vac_mev),
        ("nu3", 24, 24.0 * E_vac_mev),
    ]
    return [
        {
            "Particle": particle,
            "Factor": factor,
            "E_vac_MeV": E_vac_mev,
            "m_SFT_MeV": mass_mev,
            "m_SFT_eV": mass_mev * 1.0e6,
            "m_SFT_meV": mass_mev * 1.0e9,
            "Status": "preliminary neutrino closure sequence",
        }
        for particle, factor, mass_mev in rows
    ]


def higgs_candidate_row() -> dict:
    """Return the Higgs-sector candidate reported in the latest draft."""
    return {
        "Particle": "H",
        "m_SFT_GeV": HIGGS_SFT_GEV_REPORTED,
        "m_SFT_MeV": HIGGS_SFT_GEV_REPORTED * 1000.0,
        "Status": "reported candidate; scalar closure correction not fully derived",
    }


def wz_status_rows() -> list[dict]:
    """Return W/Z status rows without unsupported predictions."""
    return [
        {
            "Particle": "W",
            "m_SFT_GeV": None,
            "Status": "not computed: explicit SFT W formula not provided in latest draft",
        },
        {
            "Particle": "Z",
            "m_SFT_GeV": None,
            "Status": "not computed: explicit SFT Z formula not provided in latest draft",
        },
    ]
