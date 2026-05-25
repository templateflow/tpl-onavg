#!/bin/bash
module load workbench
surfname="onavg-ico32_rh"
wb_command -surface-generate-inflated \
    "$surfname"_midthickness.surf.gii \
    "$surfname"_inflated.surf.gii \
    "$surfname"_very_inflated.surf.gii \
    -iterations-scale 2.5