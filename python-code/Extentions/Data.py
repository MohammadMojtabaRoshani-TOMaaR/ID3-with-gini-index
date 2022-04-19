import pandas as pd


class Data(object):
    def __init__(self, path):
        self.path = path

    def load_by_given_names(
            self,
            first_arg: str,
            second_arg: str,
            third_arg: str,
            drop=False,
            drop_array=[]
    ):

        dataset = pd.read_excel(self.path,
                              names=[
                                  first_arg,
                                  second_arg,
                                  third_arg,
                                  "result"
                              ])

        if drop:
            for item in drop_array:
                dataset.drop(str(item[0]), axis=int(item(1)))

        return dataset
