import pandas as pd
class Seq2SeqAttention(object):
    def __init__(self, raw_train_data, raw_test_data, ):
        train_data = pd.read_table(raw_train_data)
        test_data = pd.read_table(raw_test_data)
