#!/bin/bash

src_dir=$(dirname $(realpath $0))
des_dir=$HOME/vPSIJ_util

mkdir -p des_dir
jq -n --arg slurmdir $src_dir/sche_template/slurm \
      --arg pbsprodir $src_dir/sche_template/pbspro \
      --arg pjsubdir $src_dir/sche_template/pjsub \
      '{"slurm": $slurmdir, "pbspro": $pbsprodir, "pjsub": $pjsubdir}' > $des_dir/template_location.json