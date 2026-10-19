#!/bin/bash
sed '/>/d' Fasta.txt
sed 's/T/U/g' Fasta.txt
sed 's/seq1/human_gene/' Fasta.txt
