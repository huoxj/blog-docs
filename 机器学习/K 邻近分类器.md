## k-NN

### 算法流程

对测试样本，找训练样本中最近的 $k$ 个，这 $k$ 个样本中标签最多的就是测试样本的类。

### k 的取值
- k 一般取奇数值，避免平局
- k 取不同的值，分类结果可能不同
- k 值较小时，对噪声敏感，整体模型变得复杂，容易过拟合
- k 值较大时，对噪声不敏感，整体模型变得简单，容易欠拟合

### 变种

#### 最邻近分类器

k-NN 的 $k=1$ 的特殊情况。