#
# import numpy as np
#
# import pandas as pd

# Series  DataFrame
# s = pd.Series([12,-4,7,9])
# print(s)
# pri
# s = pd.Series([12,-4,7,9],index=['a','b','c','d'])
# print(s)
# index 索引    values元素
# print(88*'~')
# print(s.values)
# print(88*'~')
#
# print(s.index)

# pandas.mege(), pandas.concat()  pandas.DataFrame.combine_first()


from sklearn import datasets
iris = datasets.load_iris()
# # print(iris.data)
# print(iris.target)
# print(88*'~')
# print(iris.target_names)

# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# from sklearn import datasets
#
# iris = datasets.load_iris()
# x = iris.data[:,0]
# y = iris.data[:,1]
# species = iris.target
#
#
# x_min,x_max = x.min() - .5,x.max() +.5
# y_min,y_max = y.min() - .5,y.max() +.5
#
#
# plt.figure()
# plt.title("Iris DataSet - Classfication By Sepal Sizes")
# plt.scatter(x,y, c=species)
# plt.xlabel('Speal length')
# plt.ylabel('Speal width')
# plt.xlim(x_min,y_max)
# plt.ylim(y_min,y_max)
# plt.xticks(())
# plt.yticks(())


# 主成分分解 使用scikit-learn库的fit_transform()函数用来降维


# from sklearn.decomposition import PCA
# x_reduced = PCA(n_components=3).fit_transform(iris.data)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
x = iris.data[:,1]
y = iris.data[:,2]
species = iris.target
x_reduced = PCA(n_components=3).fit_transform(iris.data)


fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('Iris DataSet by PCA',size=14)
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_xlabel("First eigenvector")
ax.set_ylabel("Second eigenvector")
ax.set_zlabel("Third eigenvector")
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
# 在pycharm中用matplotlib展示
plt.show()

