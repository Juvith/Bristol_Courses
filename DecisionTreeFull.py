import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from treelib import Node, Tree

hire = pd.read_csv('coursework2.csv')
print(hire)
plt.hist(hire['count'], density=False, bins=3, histtype='stepfilled')
plt.title('Histogram of Bicycle Demand by Count')
plt.xlabel('Count of Demand')
plt.ylabel('Probability of Count')
plt.show()
hire['usage'] = np.where((hire['count'] >= 6000), 'high', np.where((hire['count'] <= 3000), 'low', 'medium'))
print(hire)
plt.hist(hire['usage'], density=False, bins=10)
plt.title('Histogram of Bicycle Demand by Usage')
plt.xlabel('Usage Type')
plt.ylabel('Usage in Number Counts')
plt.show()

dummies = pd.get_dummies(hire.usage)
print(dummies)

hire['tempbins'] = np.where((hire['temp'] < 12), 'low', np.where((hire['temp'] <= 12), 'medium', 'high'))
print(hire[['temp', 'tempbins']])
hire.tempbins = hire.tempbins.map({'high': 2, 'medium': 1, 'low': 0})
hire.usage = hire.usage.map({'high': 2, 'medium': 1, 'low': 0})
print(hire)

X = hire[['season', 'weathersit', 'workingday', 'usage']]


def compute_entropies(df_label):
    classes,class_counts = np.unique(df_label,return_counts = True)
    H = np.sum([(-class_counts[i]/np.sum(class_counts))*np.log2(class_counts[i]/np.sum(class_counts))
                            for i in range(len(classes))])
    #print ('The Entropy of Attribute is: ', np.round(H,3))
    return H
#entropy1 = compute_entropies(dummies['high'])
#entropy2 = compute_entropies(dummies['medium'])
#entropy3 = compute_entropies(dummies['low'])

def inform_gain(dataset,feature,label):
    dataset_entropy = compute_entropies(dataset[label])
    values,feat_counts = np.unique(dataset[feature],return_counts=True)

    weighted_feature_entropy = np.sum([(feat_counts[i]/np.sum(feat_counts))*compute_entropies(dataset.where(dataset[feature]
                            ==values[i]).dropna()[label]) for i in range(len(values))])
    IG = dataset_entropy - weighted_feature_entropy
    print('The Information Gain of the Feature: ', np.round(IG,3))
    return IG
#ig1 = inform_gain(X, 'workingday' , 'usage')

features = X.columns[:-1]
label = 'season'
parent=None
features

def build_decision_tree(dataset,df,features,label,parent):

    datum = np.unique(df[label],return_counts=True)
    unique_data = np.unique(dataset[label])

    if len(unique_data) <=1:
        return unique_data[0]
    elif len(dataset) ==0:
        return unique_data[np.argmax(datum[1])]
    elif len(features) ==0:
        return parent
    else:
        parent = unique_data[np.argmax(datum[1])]

        item_values = [inform_gain(dataset,feature,label) for feature in features]

        optimum_feature_index = np.argmax(item_values)
        optimum_feature = features[optimum_feature_index]
        decision_tree = {optimum_feature:{}}
        features = [i for i in features if i!= optimum_feature]

        for value in np.unique(dataset[optimum_feature]):
            min_data = dataset.where(dataset[optimum_feature] == value).dropna()
            min_tree = build_decision_tree(min_data,df,features,label,parent)

            decision_tree[optimum_feature][value] = min_tree
    return decision_tree

dt = build_decision_tree(X,X,features,'usage',parent)
#pprint(dt)
tree = Tree()
tree.create_node("Season", "season")  # root node
tree.create_node("Weathersit", parent="season")
tree.create_node("Weathersit", "weathersit", parent="season")
tree.create_node("Weathersit", parent="weathersit")
tree.create_node("Workingday", "Workingday", parent="weathersit")

tree.show()