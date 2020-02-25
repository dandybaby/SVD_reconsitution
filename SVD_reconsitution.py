import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# 取前k个特征，对图像进行还原
def get_image_feature(s, k):
    # 对于S，只保留前K个特征值
    s_temp = np.zeros(s.shape[0])
    s_temp[0:k] = s[0:k]
    s = s_temp * np.identity(s.shape[0])
    # 用新的s_temp，以及p,q重构A
    temp = np.dot(p, s)
    temp = np.dot(temp, q)
    plt.imshow(temp, cmap=plt.cm.gray, interpolation='nearest')
    plt.show()


# 加载256色图片
image = Image.open('./vivi.jpg')
L = image.convert('L')
A = np.array(L)
# 显示原图像
plt.imshow(A, cmap=plt.cm.gray, interpolation='nearest')
plt.show()
# 对图像矩阵A进行奇异值分解，得到p,s,q
p, s, q = np.linalg.svd(A, full_matrices=False)
print(p.shape, s.shape, q.shape)
# 取前k个特征，对图像进行还原
get_image_feature(s, 6)
get_image_feature(s, 60)
get_image_feature(s, 300)
