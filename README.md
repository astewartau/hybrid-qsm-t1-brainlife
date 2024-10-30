# Hybrid Contrast (HC) Image Generator

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.444-blue.svg)](https://doi.org/10.25663/bl.app.444)

## Documentation

This Brainlife app generates a hybrid contrast (HC) image that combines T1-weighted (T1w) MRI images and Quantitative Susceptibility Mapping (QSM) images. The HC image improves contrast in subcortical gray matter (SGM) structures, enhancing visibility and aiding in segmentation tasks without modifying training data for algorithms like FSL-FIRST. This app utilizes weighted coefficients to create the hybrid image based on predefined intensity values in reference regions.

### What the app does

1. Loads T1w and QSM images (stored using the `neuro/anat/t1w` and `neuro/qsm` Brainlife datatypes).
2. Resamples the QSM image if it does not match the T1 dimensions.
3. Computes a hybrid contrast (HC) image using the formula: 
    ```math
    \mathrm{HC} = w_1 \times \mathrm{T1w} + w_2 \times \mathrm{QSM}
    ```
4. Outputs the HC image as a NIfTI file (stored using the `neuro/anat/t1w` Brainlife datatype)

### Inputs, configuration and outputs

**Inputs:**
- **t1**: Path to the T1-weighted NIfTI image file.
- **qsm**: Path to the QSM NIfTI image file.

**Configuration:**
- **w1**: Weighting coefficient for the T1 image (default 1.5).
- **w2**: Weighting coefficient for the QSM image (default -100).

**Outputs**
- **hybrid/t1.nii.gz**: The generated HC image in NIfTI format.

## Authors
- Ashley Stewart

## Citations
We kindly ask that you cite this repository and the following articles when publishing papers and code using this app. 

1. **brainlife. io: A decentralized and open source cloud platform to support neuroscience research**. Hayashi, S., Caron, B. A., et al. & Pestilli, F. (2023). ArXiv. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10274934/

2. **An improved FSL-FIRST pipeline for subcortical gray matter segmentation to study abnormal brain anatomy using quantitative susceptibility mapping (QSM).** Feng, Xiang, et al. (2017). Magnetic Resonance Imaging. https://doi.org/10.1016/j.mri.2017.02.002

## Funding Acknowledgement
brainlife.io is publicly funded. For the sustainability of the project, we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2024 brainlife.io The University of Texas at Austin and Indiana University
