# BERT_BARRAGES_CLASSIFICATION
利用bert来对弹幕数据进行分类

首先要下载bert-tensorflow：
```
pip install bert-tensorflow
```

首先要新建两个文件夹“bert_pretrain_model”和“save_model”
- bert_pretrain_model: BERT中文模型下载到这里，并进行解压。具体模型下载连接：
[BERT-Base, Chinese](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip)
- save_model: 之后模型会保存到这里

## BERT模型文件
BERT模型下载后是一个压缩包，类似于uncased_L-12_H-768_A-12.zip。里面包含了四个文件：
- bert_config.json：BERT模型参数
- bert_model.ckpt.xxxx：这里有两种文件，但导入模型只需要bert_model.ckpt这个前缀就可以了
- vocab.txt：存放词典


## train and eval
运行下面命令：
```
python3 train.py
```

## result


