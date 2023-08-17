# Hub-Aware Spatial-Temporal Long-Range Transformer for Incremental Traffic Flow Prediction

Code of H-STFormer with PyTorch2.0. Based on [LibCity](https://github.com/LibCity/Bigscity-LibCity) framework.

MyFormer is an alias of H-STFormer.

## Highlights of This Work
1. Implementation of FastDTW can use multiple CPU cores. Calculation of single node in PeMSD4 takes only about 10s with 8 CPU cores. (In contrast, single-core calculation takes 70s+.)
2. HubSSA, mining potential traffic hubs on the road network. (Idea by Lei Zhang, implementation and improvements by Xiao Xu.)
3. The first attempt on incremental learning of traffic flow prediction. We designed a Spatial-Temporal Knowledge Distillation Module for Stage-2 training (the incremental stage). (Idea and impl by Xiao Xu)

## Dataset
Datasets for incremental training are randomly split from PeMS0x. You can use `PreProcess/GenerateDatasets.py` to generate them.

Or use mine, [download with BaiduNetDisk](https://pan.baidu.com/s/1XkZb3cJFdi__XKczbdSr8g?pwd=0221) or
[Google Drive](https://drive.google.com/file/d/1ozKxML4OVF2GQCDOzIa9r0FGS8j1w0tf/view?usp=sharing).

If you split the incremental datasets by yourself, you should delete all the `PeMS0x[ST/T][60/80]Stage[1/2].npy` under the root dir, 
and all the `dtw_PeMS0x[ST/T][60/80]Stage[1/2].npy` under `libcity/cache/dataset_cache` and then let the program re-calculate them.
That's because the reserved part of the road network has changed.

## Quick Start

Use miniconda environment config file for [Ubuntu](env-py310-cuda117-ubuntu.yaml) or [Windows](env-py310-cuda118-windows.yaml) to create conda venv.

Commands for each experiment are available [here](Commands.md).

The aforementioned incremental commands are temporal-only incremental. 
Besides, I also provided commands for spatial-temporal incremental tasks, which amount to learning on a dynamically
increasing road network. They are not that SOTA and aren't written into the paper. 
If needed, click [here](Legacy-STIncrementalCommands.md).

## Recommended Hardware Env
Intel or AMD x86_64-arch, 8 CPU cores or more;

at least 80GB RAM (128GB recommended);

NVIDIA Geforce RTX 2080Ti or better (at least 11GB Video Memory for PeMSD7 Series)

## Pre-generated Dataset Cache
Generating PeMSD7 series dataset cache takes 120GB+ RAM.
You can [download pre-generated dataset cache](https://pan.baidu.com/s/1ZqAomjk7HQR_LSlTXCTGsQ?pwd=0221 
) to skip this, and 80GB RAM may be enough for training.

That's not all datasets in all formats, but it's enough to overcome the oom issue.

I provided the data in `np.float32` **(recommended)** and `np.float64`. (Note: Using `np.float16` may cause `loss=nan`.) 
After downloading the aforementioned files, please rename them as follows and put into `libcity/cache/dataset_cache`.

Here is a renaming example:

For `[np.float64]MyFormer_point_based_PeMS07ST80Stage1_12_12_0.6_1_0.2_standard_4_True_True_True_True_traffic_flow.npz`, 

rename it to `MyFormer_point_based_PeMS07ST80Stage1_12_12_0.6_1_0.2_standard_[batch_size]_True_True_True_True_traffic_flow.npz`.

If batch_size=8, that is `MyFormer_point_based_PeMS07ST80Stage1_12_12_0.6_1_0.2_standard_8_True_True_True_True_traffic_flow.npz`.
