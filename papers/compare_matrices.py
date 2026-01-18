#!/usr/bin/env python3
"""
Compare our paper's matrix with the "correct" Moxness construction.
"""
import numpy as np

PHI = (1 + np.sqrt(5)) / 2
PHI_INV = PHI - 1

print("=" * 70)
print("COMPARISON: Our Matrix vs 'Correct' Moxness Matrix")
print("=" * 70)

# ========================================
# MATRIX A: Our paper's matrix (sqrt5_coupling_theorem.tex)
# ========================================
print("\n--- MATRIX A: From our paper ---")

a1 = 0.5                    # = 1/2
b1 = (PHI - 1) / 2          # = 1/(2φ) ≈ 0.309
c1 = PHI / 2                # = φ/2 ≈ 0.809

print(f"Coefficients: a={a1}, b={b1:.6f}, c={c1:.6f}")

U_paper = np.array([
    [ a1,  b1,  a1,  b1,  a1, -b1,  a1, -b1],   # Row 0 (U_L)
    [ a1,  a1, -b1, -b1, -a1, -a1,  b1,  b1],   # Row 1 (U_L)
    [ a1, -b1, -a1,  b1,  a1, -b1, -a1,  b1],   # Row 2 (U_L)
    [ a1, -a1,  b1, -b1, -a1,  a1, -b1,  b1],   # Row 3 (U_L)
    [ c1,  a1,  c1,  a1,  c1, -a1,  c1, -a1],   # Row 4 (U_R)
    [ c1,  c1, -a1, -a1, -c1, -c1,  a1,  a1],   # Row 5 (U_R)
    [ c1, -a1, -c1,  a1,  c1, -a1, -c1,  a1],   # Row 6 (U_R)
    [ c1, -c1,  a1, -a1, -c1,  c1, -a1,  a1],   # Row 7 (U_R)
])

print(f"det(U_paper) = {np.linalg.det(U_paper):.6f}")
print(f"rank(U_paper) = {np.linalg.matrix_rank(U_paper)}")
print(f"Orthogonal? ||U·Uᵀ - I||∞ = {np.max(np.abs(U_paper @ U_paper.T - np.eye(8))):.6f}")

# ========================================
# MATRIX B: "Correct" Moxness (from e8_h4_correct_simulation.py)
# ========================================
print("\n--- MATRIX B: 'Correct' Moxness (normalized) ---")

a2 = PHI / 2        # φ/2 ≈ 0.809
b2 = 1 / (2 * PHI)  # 1/(2φ) ≈ 0.309
c2 = 0.5

norm = 1 / np.sqrt(2)
print(f"Coefficients: a={a2:.6f}, b={b2:.6f}, c={c2}")
print(f"Normalization: 1/√2 = {norm:.6f}")

U_correct = norm * np.array([
    [ a2,  b2,  a2,  b2,  a2,  b2,  a2,  b2],
    [ a2,  b2, -a2, -b2,  a2,  b2, -a2, -b2],
    [ a2,  b2,  a2,  b2, -a2, -b2, -a2, -b2],
    [ a2,  b2, -a2, -b2, -a2, -b2,  a2,  b2],
    [ b2, -a2,  b2, -a2,  b2, -a2,  b2, -a2],
    [ b2, -a2, -b2,  a2,  b2, -a2, -b2,  a2],
    [ b2, -a2,  b2, -a2, -b2,  a2, -b2,  a2],
    [ b2, -a2, -b2,  a2, -b2,  a2,  b2, -a2],
])

print(f"det(U_correct) = {np.linalg.det(U_correct):.6f}")
print(f"rank(U_correct) = {np.linalg.matrix_rank(U_correct)}")
print(f"Orthogonal? ||U·Uᵀ - I||∞ = {np.max(np.abs(U_correct @ U_correct.T - np.eye(8))):.6f}")

# ========================================
# CHECK √5-COUPLING FOR BOTH
# ========================================
print("\n" + "=" * 70)
print("√5-COUPLING TEST")
print("=" * 70)

# Paper matrix
U_L_paper = U_paper[0:4, :]
U_R_paper = U_paper[4:8, :]
norm_L_paper = np.linalg.norm(U_L_paper[0, :])
norm_R_paper = np.linalg.norm(U_R_paper[0, :])
product_paper = norm_L_paper * norm_R_paper

print(f"\nPaper matrix:")
print(f"  ||U_L|| = {norm_L_paper:.10f}")
print(f"  ||U_R|| = {norm_R_paper:.10f}")
print(f"  ||U_L|| × ||U_R|| = {product_paper:.10f}")
print(f"  √5 = {np.sqrt(5):.10f}")
print(f"  Match? {np.isclose(product_paper, np.sqrt(5))}")

# "Correct" matrix
U_L_correct = U_correct[0:4, :]
U_R_correct = U_correct[4:8, :]
norm_L_correct = np.linalg.norm(U_L_correct[0, :])
norm_R_correct = np.linalg.norm(U_R_correct[0, :])
product_correct = norm_L_correct * norm_R_correct

print(f"\n'Correct' matrix:")
print(f"  ||U_L|| = {norm_L_correct:.10f}")
print(f"  ||U_R|| = {norm_R_correct:.10f}")
print(f"  ||U_L|| × ||U_R|| = {product_correct:.10f}")
print(f"  √5 = {np.sqrt(5):.10f}")
print(f"  Match? {np.isclose(product_correct, np.sqrt(5))}")

# ========================================
# CHECK φ-SCALING FOR BOTH
# ========================================
print("\n" + "=" * 70)
print("φ-SCALING TEST (U_L = U_R/φ?)")
print("=" * 70)

# Paper matrix
ratio_paper = norm_R_paper / norm_L_paper
print(f"\nPaper matrix:")
print(f"  ||U_R||/||U_L|| = {ratio_paper:.10f}")
print(f"  φ = {PHI:.10f}")
print(f"  Match? {np.isclose(ratio_paper, PHI)}")

# "Correct" matrix
ratio_correct = norm_R_correct / norm_L_correct
print(f"\n'Correct' matrix:")
print(f"  ||U_R||/||U_L|| = {ratio_correct:.10f}")
print(f"  φ = {PHI:.10f}")
print(f"  Match? {np.isclose(ratio_correct, PHI)}")

# ========================================
# WHAT MAKES THE PAPER MATRIX UNIQUE?
# ========================================
print("\n" + "=" * 70)
print("ANALYSIS: What's Special About Each Matrix?")
print("=" * 70)

print("\nPaper matrix:")
print(f"  - det = 0, rank = 4 → True PROJECTION (8D → 4D)")
print(f"  - NOT orthogonal")
print(f"  - √5-coupling HOLDS")
print(f"  - φ-scaling HOLDS")

print("\n'Correct' matrix:")
print(f"  - det ≈ {np.linalg.det(U_correct):.6f}, rank = {np.linalg.matrix_rank(U_correct)} → ", end="")
if np.isclose(np.abs(np.linalg.det(U_correct)), 1):
    print("ROTATION (preserves volume)")
else:
    print(f"Neither rotation nor pure projection")
print(f"  - Orthogonal? {np.max(np.abs(U_correct @ U_correct.T - np.eye(8))) < 0.01}")
print(f"  - √5-coupling? {np.isclose(product_correct, np.sqrt(5))}")
print(f"  - φ-scaling? {np.isclose(ratio_correct, PHI)}")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print("""
The two matrices have DIFFERENT sign patterns and DIFFERENT properties.

Our paper's matrix:
  - Is a true 8D→4D projection (rank 4)
  - Has the √5-coupling property
  - Has the φ-scaling property
  - BUT is not the Moxness unimodular rotation

The 'correct' normalized matrix:
  - May be closer to Moxness's description
  - Check if it also has √5-coupling (see above)
""")
