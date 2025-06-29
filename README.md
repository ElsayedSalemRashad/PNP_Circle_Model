# Circular NP-to-P Algorithm

## Overview

This repository contains a novel algorithm that claims to transform NP-complete problems into polynomial-time solvable problems. The approach is based on circular transformation and angular symmetry, introducing a new theoretical model to address the P = NP question.

## Author

*Elsayes Salem Rashad Sebea*  
Email: sayedsalemrashad@gmail.com  
Location: Egypt

## Abstract

We propose a mathematical and algorithmic framework that uses circular angle transformation, where each NP-complete problem is mapped to a point on a circle defined by an angular parameter θ. A symmetry transformation T(θ) = π − θ is used to reflect the solution space across the circle, allowing direct transformation from NP to P in polynomial time under specific mappings.

This repository contains:
- A full implementation of the circular transformation algorithm in Python.
- Experimental evidence on known NP-complete problems (e.g., 3SAT, TSP).
- Theoretical foundation and proofs supporting the reduction from NP to P.
- A manuscript in preparation for academic publication.

## Contents

- circular_np_to_p_algorithm.py: The main algorithm source code.
- README.md: This documentation file.
- paper_draft.docx (optional): Research paper draft (can be added later).
- examples/: Example test cases and NP problem reductions.

## Usage

To run the algorithm:
```bash
python circular_np_to_p_algorithm.py
