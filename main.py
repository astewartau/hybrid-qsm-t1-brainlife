#!/usr/bin/env python

import json
import os
import nibabel as nib
from nibabel.processing import resample_from_to

# load inputs from config.json
print("[INFO] Loading config.json...")
with open('config.json') as config_json:
	config = json.load(config_json)

print("[INFO] Extracting parameters...")
w1 = config["w1"] # T1
w2 = config["w2"] # QSM
t1_path = config["t1"]
qsm_path = config["qsm"]

# Load T1 and QSM NIfTI files
print("[INFO] Loading NIfTI images...")
t1_img = nib.load(t1_path)
qsm_img = nib.load(qsm_path)

# Check if dimensions match
print("[INFO] Checking dimensions...")
if t1_img.shape != qsm_img.shape:
    print("[WARNING] Dimensions do not match! Resampling QSM image to match T1...")
    qsm_img = resample_from_to(qsm_img, t1_img)

# Generate hybrid image
print("[INFO] Generating hybrid image...")
t1_data = t1_img.get_fdata()
qsm_data = qsm_img.get_fdata()
hc_data = w1 * t1_data + w2 * qsm_data

# Save the hybrid contrast as a new NIfTI file
print("[INFO] Saving output...")
hc_img = nib.Nifti1Image(hc_data, affine=t1_img.affine)
out_dir = os.path.abspath("hybrid")
os.makedirs(out_dir, exist_ok=True)
nib.save(hc_img, os.path.join(out_dir, "t1.nii.gz"))

print("[INFO] Complete")

