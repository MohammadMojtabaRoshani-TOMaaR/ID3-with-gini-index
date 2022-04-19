from Extentions.helper import *
from Extentions.Data import Data
from Extentions.Tree import Tree
from Gini.Gini import Gini


if __name__ == '__main__':
    initial_program()
    path_to_CSV_dataset = sys.argv[1]

    dataset = Data(path_to_CSV_dataset).load_by_given_names(
        'SEX',
        'FBS',  # fasting blood sugar
        'EIA'   # exercise induced angina
    )
    master_dataset = dataset
    rows = dataset.count()

    gini_index = Gini(dataset)
    value_for_attribute_SEX = gini_index.value_for_attribute('SEX')
    value_for_attribute_FBS = gini_index.value_for_attribute('FBS')
    value_for_attribute_EIA = gini_index.value_for_attribute('EIA')

    printer([value_for_attribute_SEX,value_for_attribute_FBS,value_for_attribute_EIA])

    gini_index_for_attribute_SEX= gini_index.calculate_gini_index_for_parent_node(value_for_attribute_SEX, rows['SEX'])
    gini_index_for_attribute_FBS= gini_index.calculate_gini_index_for_parent_node(value_for_attribute_FBS, rows['FBS'])
    gini_index_for_attribute_EIA= gini_index.calculate_gini_index_for_parent_node(value_for_attribute_EIA, rows['EIA'])

    printer([gini_index_for_attribute_SEX,gini_index_for_attribute_FBS,gini_index_for_attribute_EIA])

    first_lowest_gini = lowest([gini_index_for_attribute_SEX,gini_index_for_attribute_FBS,gini_index_for_attribute_EIA])
    print('first lowest Gini Index: ', first_lowest_gini)

    tree = Tree(list(first_lowest_gini.values())[0])

    # TODO: PHASE 2a

    gini_index.partition_dataset_by_index(list(first_lowest_gini.values())[0],'SEX','FBS')
    dataset = gini_index.give_me_the_dataset()

    gini_index = Gini(dataset['true'])
    value_for_attribute_SEX = gini_index.value_for_attribute('SEX')
    value_for_attribute_FBS = gini_index.value_for_attribute('FBS')
    printer([value_for_attribute_SEX,value_for_attribute_FBS])

    gini_index_for_attribute_SEX = gini_index.calculate_gini_index_for_parent_node(value_for_attribute_SEX, rows['SEX'])
    gini_index_for_attribute_FBS = gini_index.calculate_gini_index_for_parent_node(value_for_attribute_FBS, rows['FBS'])
    printer([gini_index_for_attribute_SEX,gini_index_for_attribute_FBS])

    second_lowest_gini = lowest([gini_index_for_attribute_SEX,gini_index_for_attribute_FBS])
    print('second lowest Gini Index: ', second_lowest_gini)

    if second_lowest_gini['gini_index'] < first_lowest_gini['gini_index']:
        print("**LEAF ACHIEVED")

    tree.add_child(parent_index=0, child=second_lowest_gini['index_name'])
    # TODO: PHASE 2b
    gini_index = Gini(dataset['false'])
    value_for_attribute_SEX = gini_index.value_for_attribute('SEX')
    value_for_attribute_FBS = gini_index.value_for_attribute('FBS')
    printer([value_for_attribute_SEX,value_for_attribute_FBS])

    gini_index_for_attribute_SEX = gini_index.calculate_gini_index_for_parent_node(value_for_attribute_SEX, rows['SEX'])
    gini_index_for_attribute_FBS = gini_index.calculate_gini_index_for_parent_node(value_for_attribute_FBS, rows['FBS'])
    printer([gini_index_for_attribute_SEX,gini_index_for_attribute_FBS])

    third_lowest_gini = lowest([gini_index_for_attribute_SEX,gini_index_for_attribute_FBS])
    print('third lowest Gini Index: ', third_lowest_gini)

    if third_lowest_gini['gini_index'] < first_lowest_gini['gini_index']:
        print("**LEAF ACHIEVED")

    tree.add_child(parent_index=0, child=second_lowest_gini['index_name'])
    # TODO: PHASE 3
    tree.print_tree()
    # only work on unix based OS
    #tree.draw()

