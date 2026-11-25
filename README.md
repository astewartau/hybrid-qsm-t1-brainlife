<h1 align="center">Hybrid QSM-weighted T1 Generator</h1>

<p align="center">
  Generates a hybrid contrast image (HC = w1 x T1w + w2 x QSM) from a T1-weighted image and a QSM map with nibabel, improving subcortical gray matter contrast.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.836"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.836-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Generates a hybrid contrast image (HC = w1 x T1w + w2 x QSM) from a T1-weighted image and a QSM map with nibabel, improving subcortical gray matter contrast.**

Loads the T1w and QSM images, resamples the QSM to the T1 grid when shapes differ, and writes the weighted sum as a new T1w-type image. Use it to improve subcortical gray matter contrast before segmentation (e.g. FSL FIRST). The QSM map should be co-registered to the T1.

| | |
|---|---|
| **Inputs** | `neuro/anat/t1w` · `neuro/qsm` |
| **Outputs** | `neuro/anat/t1w` |
| **Container** | `python:3.9-bookworm` |
| **Resources** | 1 GB memory · 0.25 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.836](https://doi.org/10.25663/brainlife.app.836) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `t1` | `neuro/anat/t1w` | yes | T1-weighted image; defines the output grid. |
| `qsm` | `neuro/qsm` | yes | Quantitative susceptibility map of the same subject. Must be aligned to the T1; it is resampled to the T1 grid if dimensions differ. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `hybrid` | `neuro/anat/t1w` | Hybrid contrast QSM-weighted T1 image. |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `w1` | number | `1.5` | Weighting coefficient for the T1 image. |
| `w2` | number |  | Weighting coefficient for the QSM image. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.836](https://doi.org/10.25663/brainlife.app.836), choose `neuro/anat/t1w`, `neuro/qsm` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/anat/t1w`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `python:3.9-bookworm`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "t1": "/path/to/t1/t1",
       "qsm": "/path/to/qsm/qsm",
       "w1": 1.5,
       "w2": "<number>"
   }
   ```

3. Run `./main`.

## What the app does

1. Loads T1w and QSM images (stored using the `neuro/anat/t1w` and `neuro/qsm` Brainlife datatypes).
2. Resamples the QSM image if it does not match the T1 dimensions.
3. Computes a hybrid contrast (HC) image using the formula: 
    ```math
    \mathrm{HC} = w_1 \times \mathrm{T1w} + w_2 \times \mathrm{QSM}
    ```
4. Outputs the HC image as a NIfTI file (stored using the `neuro/anat/t1w` Brainlife datatype)

## Inputs, configuration and outputs

**Inputs:**
- **t1**: Path to the T1-weighted NIfTI image file.
- **qsm**: Path to the QSM NIfTI image file.

**Configuration:**
- **w1**: Weighting coefficient for the T1 image (default 1.5).
- **w2**: Weighting coefficient for the QSM image (default -100).

**Outputs**
- **hybrid/t1.nii.gz**: The generated HC image in NIfTI format.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Hybrid QSM-weighted T1 Generator. brainlife.io App. [doi:10.25663/brainlife.app.836](https://doi.org/10.25663/brainlife.app.836)
- Feng X, et al. An improved FSL-FIRST pipeline for subcortical gray matter segmentation to study abnormal brain anatomy using quantitative susceptibility mapping (QSM). Magnetic Resonance Imaging (2017).
- **An improved FSL-FIRST pipeline for subcortical gray matter segmentation to study abnormal brain anatomy using quantitative susceptibility mapping (QSM).** Feng, Xiang, et al. (2017). Magnetic Resonance Imaging. https://doi.org/10.1016/j.mri.2017.02.002
- Jenkinson et al. FSL. *NeuroImage* 62:782-790 (2012). [doi:10.1016/j.neuroimage.2011.09.015](https://doi.org/10.1016/j.neuroimage.2011.09.015)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Ashley Stewart

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
