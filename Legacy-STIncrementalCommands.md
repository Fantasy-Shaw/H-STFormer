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