# Commands
If using a GPU with 20GB+ video memory, you can try larger batch_size with `PeMS04_bs32.json`, `PeMS07_bs6.json` for **_normal training_**.
Specifically, use `--config_file PeMS04_bs32` or `--config_file PeMS07_bs6` instead of the default ones.

Note: I found that `batch_size>=64` on PeMS08 and `batch_size>=8` on PeMS07 may cause `loss=nan` after some epochs.
You can try smaller `batch_size` or disable `torch.cuda.amp`.
## Normal Training (Full, Non-Incremental)
### PeMS04
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04 --exp_id pems04 --is_quick_debug_mode True --config_file PeMS04
```
### PeMS07
This one takes massive memory. If using dataset cache files: 80GB RAM + 24GB Video Memory for `batch_size=6,8` and 
120GB RAM + 11GB Video Memory for `batch_size=4`, or you need 150GB+ RAM.
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07 --exp_id pems07 --is_quick_debug_mode True --config_file PeMS07
```
### PeMS08
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08 --exp_id pems08 --is_quick_debug_mode True --config_file PeMS08
```
## Incremental Training
### PeMS04 Temporal-Only 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T60Stage1 --exp_id pems04t60stage1 --is_quick_debug_mode True --config_file PeMS04
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T60Stage2 --is_stage2 True --stage1_exp_id pems04t60stage1 --stage_1_dataset PeMS04T60Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems04t60stage2 --is_quick_debug_mode True --config_file PeMS04_st2
```
### PeMS04 Temporal-Only 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T80Stage1 --exp_id pems04t80stage1 --is_quick_debug_mode True --config_file PeMS04
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T80Stage2 --is_stage2 True --stage1_exp_id pems04t80stage1 --stage_1_dataset PeMS04T80Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems04t80stage2 --is_quick_debug_mode True --config_file PeMS04_st2
```
### PeMS07 Temporal-Only 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07T60Stage1 --exp_id pems07t60stage1 --is_quick_debug_mode True --config_file PeMS07
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07T60Stage2 --is_stage2 True --stage1_exp_id pems07t60stage1 --stage_1_dataset PeMS07T60Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems07t60stage2 --is_quick_debug_mode True --config_file PeMS07_st2
```
### PeMS07 Temporal-Only 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07T80Stage1 --exp_id pems07t80stage1 --is_quick_debug_mode True --config_file PeMS07
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07T80Stage2 --is_stage2 True --stage1_exp_id pems07t80stage1 --stage_1_dataset PeMS07T80Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems07t80stage2 --is_quick_debug_mode True --config_file PeMS07_st2
```
### PeMS08 Temporal-Only 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T60Stage1 --exp_id pems08t60stage1 --is_quick_debug_mode True --config_file PeMS08
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T60Stage2 --is_stage2 True --stage1_exp_id pems08t60stage1 --stage_1_dataset PeMS08T60Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems08t60stage2 --is_quick_debug_mode True --config_file PeMS08_st2
```
### PeMS08 Temporal-Only 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T80Stage1 --exp_id pems08t80stage1 --is_quick_debug_mode True --config_file PeMS08
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T80Stage2 --is_stage2 True --stage1_exp_id pems08t80stage1 --stage_1_dataset PeMS08T80Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems08t80stage2 --is_quick_debug_mode True --config_file PeMS08_st2
```
## Evaluating
### Eval on Entire Dataset after St.2
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T60Stage2 --is_quick_debug_mode True --exp_id pems04t60stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T80Stage2 --is_quick_debug_mode True --exp_id pems04t80stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07 --config_file PeMS07 --train false --stage2_dataset_name PeMS07T60Stage2 --is_quick_debug_mode True --exp_id pems07t60stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07 --config_file PeMS07 --train false --stage2_dataset_name PeMS07T80Stage2 --is_quick_debug_mode True --exp_id pems07t80stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T60Stage2 --is_quick_debug_mode True --exp_id pems08t60stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T80Stage2 --is_quick_debug_mode True --exp_id pems08t80stage2
```
### Eval on St.1 Dataset after St.2
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T60Stage1 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T60Stage2 --is_quick_debug_mode True --exp_id pems04t60stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T80Stage1 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T80Stage2 --is_quick_debug_mode True --exp_id pems04t80stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07T60Stage1 --config_file PeMS07 --train false --stage2_dataset_name PeMS07T60Stage2 --is_quick_debug_mode True --exp_id pems07t60stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07T80Stage1 --config_file PeMS07 --train false --stage2_dataset_name PeMS07T80Stage2 --is_quick_debug_mode True --exp_id pems07t80stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T60Stage1 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T60Stage2 --is_quick_debug_mode True --exp_id pems08t60stage2
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T80Stage1 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T80Stage2 --is_quick_debug_mode True --exp_id pems08t80stage2
```