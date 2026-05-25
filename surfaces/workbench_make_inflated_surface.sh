#!/bin/bash
module load workbench
surfname="onavg-ico32_lh"
wb_command -surface-generate-inflated \
    "$surfname"_midthickness.surf.gii \
    "$surfname"_inflated.surf.gii \
    "$surfname"_very_inflated.surf.gii \
    -iterations-scale 1 
    

    # Generate inflated and very inflated surfaces. The output surfaces are
    #   'matched' (have same XYZ range) to the anatomical surface. In most cases,
    #   an iterations-scale of 1.0 (default) is sufficient.  However, if the
    #   surface contains a large number of vertices (150,000), try an
    #   iterations-scale of 2.5.
