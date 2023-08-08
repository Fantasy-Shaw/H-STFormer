# [Unknown Journal] Incremental Few Epochs Traffic Flow Prediction

Code of H-STFormer with PyTorch2.0.

## Highlights of This Work
1. Implementation of FastDTW can use multiple CPU cores. Calculation of single node takes only about 10s with 8 CPU cores. (PDFormer takes 70s+.)
2. HubSSA, mining potential traffic hubs on the road network. (Idea by Lei Zhang, implementation and improvements by Xiao Xu.)
3. The first attempt on incremental learning of traffic flow prediction. We designed a Spatial-Temporal Knowledge Distillation Module for Stage-2 training (the incremental stage). (Idea and impl by Xiao Xu)