import SimpleITK as sitk

img = sitk.ReadImage("../mprage_skullstripped_segmentation_AHW.seg.nrrd")
sitk.WriteImage(img, "mprage_skillstripped_segmentation_AHW.nii.gz")

