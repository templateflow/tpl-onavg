import nibabel as nib
import neuroboros as nb
import numpy as np
import os


if __name__ == "__main__":
    for lr in "lr":
        for ico in [32, 64, 128]:
            nv = ico**2 * 10 + 2
            den = str(round(nv / 1000)) + 'k'
            fn = f"../tpl-onavg_hemi-{lr.upper()}_den-{den}_desc-cortex_dparc.label.gii"
            if os.path.exists(fn):
                print(f"File {fn} already exists, skipping.")
                continue

            mask = nb.mask(lr=lr, space=f"onavg-ico{ico}")
            print(mask.shape, mask.dtype, mask.sum(), mask.mean())
            da = nib.gifti.GiftiDataArray(
                data=mask.astype(np.uint8),
                intent=nib.nifti1.intent_codes['NIFTI_INTENT_LABEL'],
                datatype=nib.nifti1.data_type_codes["NIFTI_TYPE_UINT8"],
            )
            gii = nib.gifti.GiftiImage(darrays=[da])
            gii.meta['AnatomicalStructurePrimary'] = 'Cortex' + {"l": "Left", "r": "Right"}[lr]
            nib.save(gii, fn)
