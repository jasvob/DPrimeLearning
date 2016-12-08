modelName="arch_17_3"
#modelNameTmp="arch_17_1_tmp"
gpu="gpu2"
dataset="IITD"
normalize="--no-norm_input"
splitMod="4"
splitTrain="0,3"
splitTest="1,2"
outputSize="32"

eval "THEANO_FLAGS='device=$gpu,floatX=float32,optimizer_include=cudnn' python main.py --oper=train --model=$modelName --dataset=$dataset --num_epochs=100 --batch_size=128 --num_batches=30 --dim_depth=1 --dim_width=136 --dim_height=136 --output_dim=$outputSize --crop_size=8 --dist_margin=100 --mu=1e-4 --alpha=0.5 --lr=1e-2 $normalize --split_mod=$splitMod --split_train=$splitTrain --split_test=$splitTest"
#eval "cp -rf $modelName $modelNameTmp"
eval "THEANO_FLAGS='device=$gpu,floatX=float32,optimizer_include=cudnn' python main.py --oper=retrain --model=$modelName --dataset=$dataset --num_epochs=100 --batch_size=128 --num_batches=30 --dim_depth=1 --dim_width=136 --dim_height=136 --output_dim=$outputSize --crop_size=8 --dist_margin=100 --mu=1e-4 --alpha=0.5 --lr=5e-3 --start_epoch=100 $normalize --split_mod=$splitMod --split_train=$splitTrain --split_test=$splitTest"
#eval "cp -rf $modelName $modelNameTmp"
eval "THEANO_FLAGS='device=$gpu,floatX=float32,optimizer_include=cudnn' python main.py --oper=retrain --model=$modelName --dataset=$dataset --num_epochs=100 --batch_size=128 --num_batches=30 --dim_depth=1 --dim_width=136 --dim_height=136 --output_dim=$outputSize --crop_size=8 --dist_margin=100 --mu=1e-4 --alpha=0.5 --lr=1e-3 --start_epoch=200 $normalize --split_mod=$splitMod --split_train=$splitTrain --split_test=$splitTest"
#eval "cp -rf $modelName $modelNameTmp"
eval "THEANO_FLAGS='device=$gpu,floatX=float32,optimizer_include=cudnn' python main.py --oper=retrain --model=$modelName --dataset=$dataset --num_epochs=100 --batch_size=128 --num_batches=30 --dim_depth=1 --dim_width=136 --dim_height=136 --output_dim=$outputSize --crop_size=8 --dist_margin=100 --mu=1e-4 --alpha=0.5 --lr=5e-4 --start_epoch=300 $normalize --split_mod=$splitMod --split_train=$splitTrain --split_test=$splitTest"

