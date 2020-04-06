import pandas as pd
import os
import re


def load_directory_data(datafile, label_file):
    """
    Load all files from a datafile in a DataFrame.
    :param datafile:
    :param label_file:
    :return:
    """
    label_to_num = {}
    with open(label_file, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line:
                line_list = line.strip().split("\t")
                label_to_num[line_list[1]] = int(line_list[0])
            else:
                break

    data = {}
    data["barrage"] = []
    data["keyword"] = []
    data["label"] = []
    if os.path.exists(datafile):
        with open(datafile, "r", encoding="utf-8") as f:
            f.readline()  # ignore the first line
            while True:
                line = f.readline()
                if line:
                    line_list = line.strip().split("\t")
                    data["barrage"].append(line_list[0])
                    data["keyword"].append(line_list[1])
                    data["label"].append(label_to_num[line_list[1]])
                else:
                    break

    data = pd.DataFrame.from_dict(data).sample(frac=1).reset_index(drop=True)
    split_pos = int(len(data) * 0.8)
    train_data = data[:split_pos]
    eval_data = data[split_pos:]
    return train_data, eval_data, label_to_num


if __name__ == "__main__":
    data_file = "./data/train_data_has_neg.txt"
    label_file = "./data/label_to_nums.txt"
    train_feature, eval_feature, label_to_num = load_directory_data(data_file, label_file)
    print(len(train_feature))
    print(len(eval_feature))
