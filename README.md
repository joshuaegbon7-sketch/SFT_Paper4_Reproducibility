# SFT Paper 4 Reproducibility Package

This package is aligned with the current SFT Paper 4 manuscript.

It reproduces the manuscript-supported chain:

```
Geometry/Operator -> Eigenvalue -> Classification -> Mass
```

## What the package computes

### 1. S^3 eigenvalue ladder

Scalar:

```
Lambda_tilde_scalar(n) = n(n+2)
```

Vector:

```
Lambda_tilde_vector(n) = n(n+2)-1
```

### 2. Surface mass scale

The code computes

```
M_surf = (hbar c / R_c) (R_c / l_P)^(2/3)
```

using the SFT confinement radius appearing in the manuscript.

### 3. Retained charged-lepton and quark sectors

The code reproduces

```
C_i = 2^a 3^b 4^c
```

and

```
m_i = M_surf C_i
```

for

```
e, mu, tau, u, d, s, c, b, t.
```

The implementation follows the operator-to-classification structure introduced in the manuscript:

```
Operator
    -> Eigenvalue
    -> Classification
    -> Mass
```

using the retained closure-selected sectors defined in Paper 4.

### 4. Neutrino sequence

The code computes

```
E_vac = [rho_DE,0 c^2 (hbar c)^3]^(1/4)
```

and reproduces the preliminary sequence

```
nu1 = 0
nu2 = 4 E_vac
nu3 = 24 E_vac
```

as discussed in the manuscript.

This remains a preliminary neutrino closure sequence because the current paper does not yet provide a complete operator-to-classification derivation for the neutrino sector.

### 5. Higgs candidate

The code records the manuscript's reported Higgs candidate

```
m_H^SFT ~= 123.8 GeV
```

as a reported candidate rather than a fully recomputed scalar-closure derivation.

### 6. W and Z status

The code does not compute W and Z masses because the current manuscript discusses electroweak clustering but does not provide explicit SFT formulas for

```
m_W
```

or

```
m_Z.
```

## Notes on Quark-Mass Comparisons

The strange-quark comparison should be interpreted cautiously, since quoted quark masses are running masses that depend on the renormalisation scale and scheme used in the extraction procedure.

Consequently, the SFT strange-quark value should be compared against an explicitly specified mass convention rather than treated as a direct pole-mass comparison.

More generally, comparisons involving the u, d, s, c, b, and t quarks should be interpreted within the context of the corresponding renormalisation prescription. Numerical differences between SFT values and quoted experimental masses may therefore reflect convention and scale dependence in addition to any underlying theoretical discrepancy.

Charged-lepton masses (e, mu, tau) are considerably less sensitive to these issues and therefore provide a cleaner benchmark for evaluating the numerical performance of the present framework.

## Run locally

```
python reproduce_tables.py
```

Outputs are written to:

```
outputs/
```

## Google Colab

Upload the supplied notebook and run all cells.

## Reproducibility Statement

The purpose of this package is to allow independent verification of the numerical workflow presented in SFT Paper 4.

The package reproduces the manuscript-supported chain

```
Geometry
    -> Operator
    -> Eigenvalue
    -> Classification
    -> Mass
```

for the retained charged-lepton and quark sectors and provides explicit computational outputs corresponding to the tables appearing in the manuscript.

Future versions may incorporate additional sectors as explicit operator-level derivations become available.
