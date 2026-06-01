"""Reproduce latest SFT Paper 4 numerical tables.

Run:

    python reproduce_tables.py

Outputs are written to ./outputs.
"""

from pathlib import Path

import pandas as pd

from constants import OBSERVED_MASSES_MEV, OBSERVED_ELECTROWEAK_GEV
from scales import planck_length_m, surface_mass_scale_mev, vacuum_energy_scale_mev
from operator_spectrum import manuscript_eigenvalue_table_rows, full_ladder_rows
from mass_calculator import (
    retained_sector_rows,
    neutrino_sequence_rows,
    higgs_candidate_row,
    wz_status_rows,
)

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_csv(df: pd.DataFrame, filename: str) -> None:
    path = OUTPUT_DIR / filename
    df.to_csv(path, index=False)
    print(f"Saved {path}")


def scale_table() -> pd.DataFrame:
    E_vac = vacuum_energy_scale_mev()
    return pd.DataFrame([
        {"Quantity": "Planck length", "Value": planck_length_m(), "Unit": "m"},
        {"Quantity": "M_surf", "Value": surface_mass_scale_mev(), "Unit": "MeV"},
        {"Quantity": "E_vac", "Value": E_vac, "Unit": "MeV"},
        {"Quantity": "E_vac", "Value": E_vac * 1.0e9, "Unit": "meV"},
    ])


def retained_table() -> pd.DataFrame:
    df = pd.DataFrame(retained_sector_rows())
    df["M_surf_MeV"] = df["M_surf_MeV"].round(6)
    df["m_SFT_MeV"] = df["m_SFT_MeV"].round(6)
    df["m_SFT_GeV"] = df["m_SFT_GeV"].round(6)
    return df


def comparison_table() -> pd.DataFrame:
    rows = []
    for row in retained_sector_rows():
        particle = row["Particle"]
        pred = row["m_SFT_MeV"]
        obs = OBSERVED_MASSES_MEV.get(particle)
        abs_err = None if obs is None else pred - obs
        pct_err = None if obs is None else 100.0 * abs_err / obs
        rows.append({
            "Particle": particle,
            "m_SFT_MeV": round(pred, 6),
            "Observed_MeV": obs,
            "Absolute_Error_MeV": None if abs_err is None else round(abs_err, 6),
            "Percent_Error": None if pct_err is None else round(pct_err, 4),
            "Comment": "running mass; scale-dependent"
            if particle in {"u", "d", "s", "c", "b", "t"}
            else "",
        })
    return pd.DataFrame(rows)


def neutrino_table() -> pd.DataFrame:
    df = pd.DataFrame(neutrino_sequence_rows())
    df["E_vac_MeV"] = df["E_vac_MeV"].map(lambda x: f"{x:.12e}")
    df["m_SFT_MeV"] = df["m_SFT_MeV"].map(lambda x: f"{x:.12e}")
    df["m_SFT_eV"] = df["m_SFT_eV"].round(9)
    df["m_SFT_meV"] = df["m_SFT_meV"].round(6)
    return df


def electroweak_status_table() -> pd.DataFrame:
    rows = wz_status_rows()
    h = higgs_candidate_row()
    obs_h = OBSERVED_ELECTROWEAK_GEV.get("H")
    h.update({
        "Observed_GeV": obs_h,
        "Absolute_Error_GeV": None if obs_h is None else h["m_SFT_GeV"] - obs_h,
        "Percent_Error": None if obs_h is None else 100.0 * (h["m_SFT_GeV"] - obs_h) / obs_h,
    })
    rows.append(h)
    return pd.DataFrame(rows)


def main() -> None:
    scales = scale_table()
    manuscript_ladder = pd.DataFrame(manuscript_eigenvalue_table_rows())
    full_ladder = pd.DataFrame(full_ladder_rows(max_n=4))
    retained = retained_table()
    comparison = comparison_table()
    neutrinos = neutrino_table()
    ew_status = electroweak_status_table()

    save_csv(scales, "SFT_Paper4_scales.csv")
    save_csv(manuscript_ladder, "SFT_Paper4_manuscript_eigenvalue_table.csv")
    save_csv(full_ladder, "SFT_Paper4_full_S3_ladder.csv")
    save_csv(retained, "SFT_Paper4_operator_to_classification_to_mass.csv")
    save_csv(comparison, "SFT_Paper4_observed_comparison.csv")
    save_csv(neutrinos, "SFT_Paper4_neutrino_closure_sequence.csv")
    save_csv(ew_status, "SFT_Paper4_electroweak_higgs_status.csv")

    print("\nScales:")
    print(scales.to_string(index=False))

    print("\nManuscript eigenvalue table:")
    print(manuscript_ladder.to_string(index=False))

    print("\nOperator -> Eigenvalue -> Classification -> Mass:")
    print(retained.to_string(index=False))

    print("\nNeutrino closure sequence:")
    print(neutrinos.to_string(index=False))

    print("\nElectroweak/Higgs status:")
    print(ew_status.to_string(index=False))


if __name__ == "__main__":
    main()
