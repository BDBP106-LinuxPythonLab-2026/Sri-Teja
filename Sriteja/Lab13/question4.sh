#!/bin/bash

awk '$4=="PHE" {print $2}' 1hk0.pdb > PHE_atoms.xyz
