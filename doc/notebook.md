# Notebook

## Foundational Concepts

* Secure ML & Privacy-Preserving ML (PPML)
  * Secure ML is for **Integrity & Availability**
  * PPML is for **Confidentiality & Privacy**
* Attacker Models
  * Semi-honest (honest-but-curious)
  * Malicious
* Canonical Attacks Against ML Models
  * Reconstruction Attacks
  * Model Inversion Attacks
  * Membership-Inference Attacks
  * Attribute-Inference Attacks
* Essential PPML Technologies
  * Secured Multi-Party Computation (SMPC)
    * Categories
      * Oblivious Transfer (OT)
      * Secret Sharing (SS)
      * Threshold Homomorphic Encryption (THE)
  * Homomorphic Encryption (HE)
    * Note
      * HE is extremely **computationally expensive** so it is **NOT** suitable for model training
    * Categories
      * Partially (PHE)
      * Somewhat (SHE)
      * Fully (FHE)
  * Differential Privacy (DP) Mechanisms
    * Note
      * DP is merely a **criteria** to evaluate if a **mechanism**, e.g. asking for mean value over a dataset, is privacy preserving.
      * The mechanisms are designed based on the idea that **adding noise** to individual records or query results can mask out the privacy information locally while preserving an accurate aggregation over the dataset.
    * Categories
      * Sensitivity Mechanisms
      * Exponential Mechanisms

## Distributed ML (DML)

* Scalability-Motivated DML
* Privacy-Motivated DML
