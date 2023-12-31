import os
import argparse

from libcity.pipeline.pipeline import run_incr_model
from libcity.utils import general_arguments, str2bool, str2float


def add_other_args(parser):
    for arg in general_arguments:
        if general_arguments[arg] == 'int':
            parser.add_argument('--{}'.format(arg), type=int, default=None)
        elif general_arguments[arg] == 'bool':
            parser.add_argument('--{}'.format(arg),
                                type=str2bool, default=None)
        elif general_arguments[arg] == 'str':
            parser.add_argument('--{}'.format(arg),
                                type=str, default=None)
        elif general_arguments[arg] == 'float':
            parser.add_argument('--{}'.format(arg),
                                type=str2float, default=None)
        elif general_arguments[arg] == 'list of int':
            parser.add_argument('--{}'.format(arg), nargs='+',
                                type=int, default=None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str,
                        default='traffic_state_pred', help='the name of task')
    parser.add_argument('--model', type=str,
                        default='GRU', help='the name of model')
    parser.add_argument('--dataset', type=str,
                        default='PeMS04', help='the name of dataset')
    parser.add_argument('--config_file', type=str,
                        default=None, help='the file name of config file')
    parser.add_argument('--saved_model', type=str2bool,
                        default=True, help='whether save the trained model')
    parser.add_argument('--train', type=str2bool, default=True,
                        help='whether re-train model if the model is \
                             trained before')
    parser.add_argument("--local_rank", default=0, type=int)
    parser.add_argument('--exp_id', type=str,
                        default=None, help='id of experiment')
    # Params for incremental learning
    parser.add_argument('--is_stage2', type=str2bool,
                        default=False, help='incremental stage of experiment')
    parser.add_argument('--stage1_exp_id', type=str,
                        default=None, help='id of stage_1 experiment for stage_2')
    parser.add_argument('--stage_1_dataset', type=str,
                        default='PeMS04', help='the name of stage_1 dataset')
    parser.add_argument('--temperature', type=float,
                        default=10.0, help='Temperature hyperparameter')
    parser.add_argument('--lambda_parm', type=float,
                        default=10.0, help='Distillation loss hyperparameter')
    parser.add_argument('--preset_max_num_nodes', type=int,
                        default=0, help='Distillation loss hyperparameter')
    parser.add_argument('--is_quick_debug_mode', type=str2bool,
                        default=False,
                        help="If enabled, using quick-debug-mode, no calculating clustering pattern key.")
    parser.add_argument('--stage2_dataset_name', type=str,
                        default=None, help='This is only used if evaluating an incremental model.')
    add_other_args(parser)
    args = parser.parse_args()
    dict_args = vars(args)
    other_args = {key: val for key, val in dict_args.items() if key not in [
        'task', 'model', 'dataset', 'config_file', 'saved_model', 'train'] and
                  val is not None}
    if args.gpu_id is not None:
        os.environ["CUDA_VISIBLE_DEVICES"] = ','.join(map(str, args.gpu_id))
    run_incr_model(task=args.task, model_name=args.model, dataset_name=args.dataset,
                   config_file=args.config_file, saved_model=args.saved_model,
                   train=args.train, other_args=other_args, is_stage2=args.is_stage2,
                   stage1_exp_id=args.stage1_exp_id, stage1_dataset_name=args.stage_1_dataset,
                   stage2_dataset_name=args.stage2_dataset_name)
