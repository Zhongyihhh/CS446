# Python libraries
import argparse
import os

import lib.medloaders as medical_loaders
import lib.medzoo as medzoo
import lib.train as train
# Lib files
import pickle
import torch
import lib.utils as utils
from lib.losses3D import DiceLoss

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
seed = 1777777


def main():
    args = get_arguments()
    utils.reproducibility(args, seed)
    utils.make_dirs(args.save)

    training_generator, val_generator, full_volume, affine = medical_loaders.generate_datasets(args,
                                                                                               path='./datasets')
    model, optimizer = medzoo.create_model(args)
    criterion = DiceLoss(classes=args.classes)
    # print("training_generator shape:", training_generator.dim())
    # print("val_generator shape:", val_generator.dim())

    if args.cuda:
        model = model.cuda()
    print("start training...")
    # torch.save(training_generator, "training_generator.tch")
    # torch.save(val_generator, "val_generator.tch")
    trainer = train.Trainer(args, model, criterion, optimizer, train_data_loader=training_generator,
                            valid_data_loader=val_generator)
    trainer.training()


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batchSz', type=int, default=5)
    parser.add_argument('--dataset_name', type=str, default="brats2019")
    parser.add_argument('--dim', nargs="+", type=int, default=(128, 128, 128))
    parser.add_argument('--nEpochs', type=int, default=40)
    parser.add_argument('--classes', type=int, default=4)
    parser.add_argument('--samples_train', type=int, default=272)
    parser.add_argument('--samples_val', type=int, default=0)
    parser.add_argument('--inChannels', type=int, default=4)
    parser.add_argument('--inModalities', type=int, default=4)
    parser.add_argument('--terminal_show_freq', default=50)
    parser.add_argument('--threshold', default=0.1, type=float)
    parser.add_argument('--augmentation', action='store_true', default=True)
    parser.add_argument('--normalization', default='full_volume_mean', type=str,
                        help='Tensor normalization: options ,max_min,',
                        choices=('max_min', 'full_volume_mean', 'brats', 'max', 'mean'))
    parser.add_argument('--split', default=0.8, type=float, help='Select percentage of training data(default: 0.8)')
    parser.add_argument('--lr', default=1e-2, type=float,
                        help='learning rate (default: 1e-3)')
    parser.add_argument('--loadData', default=False)
    parser.add_argument('--cuda', action='store_true', default=True)
    parser.add_argument('--resume', default='', type=str, metavar='PATH',
                        help='path to latest checkpoint (default: none)')
    parser.add_argument('--model', type=str, default='UNET3D',
                        choices=('VNET', 'VNET2', 'UNET3D', 'DENSENET1', 'DENSENET2', 'DENSENET3', 'HYPERDENSENET'))
    parser.add_argument('--opt', type=str, default='sgd',
                        choices=('sgd', 'adam', 'rmsprop'))
    parser.add_argument('--log_dir', type=str,
                        default='../runs/')

    args = parser.parse_args()

    args.save = '../saved_models/' + args.model + '_checkpoints/' + args.model + '_{}_{}_'.format(
        utils.datestr(), args.dataset_name)
    return args


if __name__ == '__main__':
    main()
