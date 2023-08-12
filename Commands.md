# Commands
If using a GPU with 20GB+ GPU memory, you can try larger batch_size with `PeMS04_bs32.json`, `PeMS07_bs8.json` for **_normal training_**.

Note: I found that _batch_size>=64_ may cause _loss=nan_ after some epochs.
## Normal Training (Full, Non-Incremental)
### PeMS04
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04 --exp_id pems04 --is_quick_debug_mode True --config_file PeMS04
```
### PeMS07
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07 --exp_id pems07 --is_quick_debug_mode True --config_file PeMS07
```
### PeMS08
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08 --exp_id pems08 --is_quick_debug_mode True --config_file PeMS08
```
## Incremental Training
### PeMS04 Spatial-Temporal 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04ST60Stage1 --exp_id pems04st60stage1 --is_quick_debug_mode True --config_file PeMS04
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04ST60Stage2 --is_stage2 True --stage1_exp_id pems04st60stage1 --stage_1_dataset PeMS04ST60Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems04st60stage2 --is_quick_debug_mode True --config_file PeMS04_st2
```
### PeMS04 Spatial-Temporal 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04ST80Stage1 --exp_id pems04st80stage1 --is_quick_debug_mode True --config_file PeMS04
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04ST80Stage2 --is_stage2 True --stage1_exp_id pems04st80stage1 --stage_1_dataset PeMS04ST80Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems04st80stage2 --is_quick_debug_mode True --config_file PeMS04_st2
```
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
### PeMS07 Spatial-Temporal 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07ST60Stage1 --exp_id pems07st60stage1 --is_quick_debug_mode True --config_file PeMS07
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07ST60Stage2 --is_stage2 True --stage1_exp_id pems07st60stage1 --stage_1_dataset PeMS07ST60Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems07st60stage2 --is_quick_debug_mode True --config_file PeMS07_st2
```
### PeMS07 Spatial-Temporal 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07ST80Stage1 --exp_id pems07st80stage1 --is_quick_debug_mode True --config_file PeMS07
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS07ST80Stage2 --is_stage2 True --stage1_exp_id pems07st80stage1 --stage_1_dataset PeMS07ST80Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems07st80stage2 --is_quick_debug_mode True --config_file PeMS07_st2
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
### PeMS08 Spatial-Temporal 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08ST60Stage1 --exp_id pems08st60stage1 --is_quick_debug_mode True --config_file PeMS08
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08ST60Stage2 --is_stage2 True --stage1_exp_id pems08st60stage1 --stage_1_dataset PeMS08ST60Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems08st60stage2 --is_quick_debug_mode True --config_file PeMS08_st2
```
### PeMS08 Spatial-Temporal 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08ST80Stage1 --exp_id pems08st80stage1 --is_quick_debug_mode True --config_file PeMS08
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08ST80Stage2 --is_stage2 True --stage1_exp_id pems08st80stage1 --stage_1_dataset PeMS08ST80Stage1 --temperature 10.0 --lambda_parm 10.0 --exp_id pems08st80stage2 --is_quick_debug_mode True --config_file PeMS08_st2
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