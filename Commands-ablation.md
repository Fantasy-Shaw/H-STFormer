## Distillation Ablations
### PeMS04 Temporal-Only 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T60Stage2 --exp_id pems04t60a --is_quick_debug_mode True --config_file PeMS04_st2
```
### PeMS04 Temporal-Only 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T80Stage2 --exp_id pems04t80a --is_quick_debug_mode True --config_file PeMS04_st2
```
### PeMS08 Temporal-Only 60%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T60Stage2 --exp_id pems08t60a --is_quick_debug_mode True --config_file PeMS08_st2
```
### PeMS08 Temporal-Only 80%
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T80Stage2 --exp_id pems08t80a --is_quick_debug_mode True --config_file PeMS08_st2
```
## Evaluating
### Eval on Entire Dataset after St.2
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T60Stage2 --is_quick_debug_mode True --exp_id pems04t60a
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T80Stage2 --is_quick_debug_mode True --exp_id pems04t80a
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T60Stage2 --is_quick_debug_mode True --exp_id pems08t60a
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T80Stage2 --is_quick_debug_mode True --exp_id pems08t80a
```
### Eval on St.1 Dataset after St.2
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T60Stage1 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T60Stage2 --is_quick_debug_mode True --exp_id pems04t60a
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS04T80Stage1 --config_file PeMS04 --train false --stage2_dataset_name PeMS04T80Stage2 --is_quick_debug_mode True --exp_id pems04t80a
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T60Stage1 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T60Stage2 --is_quick_debug_mode True --exp_id pems08t60a
```
```shell
python run_model.py --task traffic_state_pred --model MyFormer --dataset PeMS08T80Stage1 --config_file PeMS08 --train false --stage2_dataset_name PeMS08T80Stage2 --is_quick_debug_mode True --exp_id pems08t80a
```