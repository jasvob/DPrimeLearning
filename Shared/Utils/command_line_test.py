#!/usr/bin/env python

"""
Command line arguments parser.
"""

def parseList(aString):
    aList = []
    for num in aString.split(','):
        aList.append(int(num))
    return aList


def parse(parser, args_in=None):
    # Model name
    parser.add_argument('--model', type=str, dest='model', required=True)
    # Arch name
    parser.add_argument('--arch', type=str, dest='arch', required=True)
    # Dataset
    parser.add_argument('--dataset', type=str, dest='dataset', required=True)
    # Output folder
    parser.add_argument('--output_dir', type=str, dest='output_dir', required=True)
    # Loss function
    parser.add_argument('--loss', type=str, dest='loss', required=False, default='dprime')

    # Network configuration
    parser.add_argument('--dim_width', type=int, dest='dim_width', required=False, default=128)
    parser.add_argument('--dim_height', type=int, dest='dim_height', required=False, default=128)
    parser.add_argument('--dim_depth', type=int, dest='dim_depth', required=False, default=1)
    parser.add_argument('--crop_size', type=int, dest='crop_size', required=False, default=8)
    parser.add_argument('--dist_margin', type=int, dest='dist_margin', required=False, default=2)
    parser.add_argument('--output_dim', type=int, dest='output_dim', required=False, default=32)
    parser.add_argument('--mu', type=float, dest='mu', required=False, default=1e-3)
    parser.add_argument('--lr', type=float, dest='lr', required=False, default=1e-2)
    parser.add_argument('--alpha', type=float, dest='alpha', required=False, default=0.5)

    # Training configuration
    parser.add_argument('--epoch', type=int, dest='epoch', required=False, default=0)
    parser.add_argument('--split_mod', type=int, dest='split_mod', required=False, default=2)
    parser.add_argument('--split_train', type=parseList, dest='split_train', required=False, default=[0])
    parser.add_argument('--split_test', type=parseList, dest='split_test', required=False, default=[1])
    parser.add_argument('--norm_input', dest='norm_input', action='store_true', required=False)
    parser.add_argument('--no-norm_input', dest='norm_input', action='store_false', required=False)
    parser.set_defaults(norm_input=True)
    parser.add_argument('--saliency', dest='saliency', action='store_true', required=False)
    parser.add_argument('--no-saliency', dest='saliency', action='store_false', required=False)
    parser.set_defaults(saliency=False)

    # Parse given arguments
    args = parser.parse_args(args_in)

    # Extract network configuration
    networkCfg = dict()
    networkCfg['inputDepth'] = args.dim_depth
    networkCfg['inputWidth'] = args.dim_width - args.crop_size
    networkCfg['inputHeight'] = args.dim_height - args.crop_size
    networkCfg['numOutputs'] = args.output_dim
    networkCfg['distMargin'] = args.dist_margin
    networkCfg['mu'] = args.mu
    networkCfg['lr'] = args.lr
    networkCfg['alpha'] = args.alpha
    networkCfg['model_name'] = args.model
    networkCfg['arch_name'] = args.arch
    networkCfg['loss'] = args.loss
    networkCfg['saliency'] = args.saliency



    # Extract testing configuration
    testingCfg = dict()
    testingCfg['epoch'] = args.epoch
    testingCfg['outputDir'] = args.output_dir
    testingCfg['dataset'] = args.dataset
    testingCfg['model'] = args.model


    return args, networkCfg, testingCfg
