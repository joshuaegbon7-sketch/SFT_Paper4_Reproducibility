"""Operator-spectrum utilities for SFT Paper 4.

This module reproduces the S^3 scalar/vector eigenvalue ladders
appearing in the latest draft.

Scalar sector:
    Lambda_tilde^(0)_n = n(n+2)

Vector sector:
    Lambda_tilde^(1)_n = n(n+2)-1

Scalar degeneracy:
    d_scalar(n) = (n+1)^2

Vector degeneracy:
    The latest manuscript table uses 6, 16, 30 for n=1,2,3.
    These are reproduced by d_vector(n) = 2 n (n+2).
"""

from __future__ import annotations


def scalar_lambda_tilde(n: int) -> int:
    if n < 0:
        raise ValueError("Scalar mode n must be non-negative.")
    return n * (n + 2)


def vector_lambda_tilde(n: int) -> int:
    if n < 1:
        raise ValueError("Vector mode n must satisfy n >= 1.")
    return n * (n + 2) - 1


def scalar_degeneracy(n: int) -> int:
    if n < 0:
        raise ValueError("Scalar mode n must be non-negative.")
    return (n + 1) ** 2


def vector_degeneracy(n: int) -> int:
    if n < 1:
        raise ValueError("Vector mode n must satisfy n >= 1.")
    return 2 * n * (n + 2)


def manuscript_eigenvalue_table_rows() -> list[dict]:
    """Return the exact illustrative eigenvalue table from the manuscript."""
    return [
        {
            "Sector": "Scalar",
            "n": 1,
            "Lambda_tilde": scalar_lambda_tilde(1),
            "Degeneracy": scalar_degeneracy(1),
            "Interpretation": "Low-order scalar sector",
        },
        {
            "Sector": "Vector",
            "n": 1,
            "Lambda_tilde": vector_lambda_tilde(1),
            "Degeneracy": vector_degeneracy(1),
            "Interpretation": "Low-order vector sector",
        },
        {
            "Sector": "Vector",
            "n": 2,
            "Lambda_tilde": vector_lambda_tilde(2),
            "Degeneracy": vector_degeneracy(2),
            "Interpretation": "Higher vector sector",
        },
        {
            "Sector": "Vector",
            "n": 3,
            "Lambda_tilde": vector_lambda_tilde(3),
            "Degeneracy": vector_degeneracy(3),
            "Interpretation": "Higher localized vector sector",
        },
        {
            "Sector": "Scalar",
            "n": 4,
            "Lambda_tilde": scalar_lambda_tilde(4),
            "Degeneracy": scalar_degeneracy(4),
            "Interpretation": "Higher localized scalar sector",
        },
    ]


def full_ladder_rows(max_n: int = 4) -> list[dict]:
    """Return scalar and vector ladder rows up to max_n."""
    rows = []
    for n in range(1, max_n + 1):
        rows.append({
            "Sector": "Scalar",
            "n": n,
            "Lambda_tilde": scalar_lambda_tilde(n),
            "Degeneracy": scalar_degeneracy(n),
        })
        rows.append({
            "Sector": "Vector",
            "n": n,
            "Lambda_tilde": vector_lambda_tilde(n),
            "Degeneracy": vector_degeneracy(n),
        })
    return rows
