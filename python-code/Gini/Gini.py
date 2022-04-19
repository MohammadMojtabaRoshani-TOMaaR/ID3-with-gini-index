import numpy as np
import pandas as pd


class Gini(object):

    def __init__(self, dataset):
        self.dataset = dataset

    def give_me_the_dataset(self):
        return self.dataset

    def value_for_attribute(self, class_name: str):

        """"LEFT SIDE OF NODE"""
        # Find where, by given class name (that is true) we have patient with and without heart disease
        filter_item_true_and_presence = ((self.dataset[class_name] == 1.0) & (self.dataset['result'] == 2))
        filter_item_true_and_absent = ((self.dataset[class_name] == 1.0) & (self.dataset['result'] == 1))

        """"RIGHT SIDE OF NODE"""
        # Find where, by given class name (that is false) we have patient without heart disease
        filter_item_false_and_presence = ((self.dataset[class_name] == 0.0) & (self.dataset['result'] == 2))
        filter_item_false_and_absent = ((self.dataset[class_name] == 0.0) & (self.dataset['result'] == 1))
        return {
            'index_name': class_name,
            'true': {
                'yes': sum(filter_item_true_and_presence),
                'no': sum(filter_item_true_and_absent)
            },
            'false': {
                'yes': sum(filter_item_false_and_presence),
                'no': sum(filter_item_false_and_absent)
            }
        }

    def calculate_gini_index_for_parent_node(self, parent_value, row_count):

        occur_true_and_yes = parent_value['true']['yes']
        occur_true_and_no = parent_value['true']['no']

        occur_false_and_yes = parent_value['false']['yes']
        occur_false_and_no = parent_value['false']['no']

        gini_impurity_ture_branch = 1 - (occur_true_and_yes / (occur_true_and_yes + occur_true_and_no)) ** 2 - (
                    occur_true_and_no / (occur_true_and_yes + occur_true_and_no)) ** 2

        gini_impurity_false_branch = 1 - (occur_false_and_yes / (occur_false_and_yes + occur_false_and_no)) ** 2 - (
                occur_false_and_no / (occur_false_and_yes + occur_false_and_no)) ** 2

        weighted_average = gini_impurity_ture_branch * ((occur_true_and_yes + occur_true_and_no)/ row_count) +\
                           gini_impurity_false_branch * ((occur_false_and_yes + occur_false_and_no)/row_count)

        return {'index_name':parent_value['index_name'], 'gini_index':weighted_average}


    def partition_dataset_by_index(self,index: str, first_index: str, second_index: str):
        self.master_dataset = self.dataset
        _dataset = self.dataset

        true_dataset = _dataset[self.dataset[index] == 1.0]
        false_dataset = _dataset[self.dataset[index] == 0.0]

        new_dataset = {
                'true': true_dataset.drop(index, axis=1),
                'false': false_dataset.drop(index, axis=1)
            }

        self.dataset = new_dataset


    def partition_dataset_for_final_tree(self, cut_index: str):
        _dataset = self.dataset

        true_dataset = _dataset[self.dataset[cut_index] == 1.0]
        false_dataset = _dataset[self.dataset[cut_index] == 0.0]

        new_dataset = {
            'true': true_dataset.drop(cut_index, axis=1),
            'false': false_dataset.drop(cut_index, axis=1)
        }

        return new_dataset