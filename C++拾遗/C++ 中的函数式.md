---
date: 2025-05-12
draft: "true"
---

大家都喜欢函数式。简单、好读、无副作用。

C++ 的 `algorithm` 头文件有很多函数式的函数。但是函数式在 C++ 中的地位没有那么高，不像 Python 是一等公民，写代码的时候信手拈来。所以这里记录一下 C++ 里面函数式的一些函数和使用函数式的一些实践。

## 基础函数

### 批量操作
#### for_each

> 副作用式 map

字面意思。对容器的每一个元素应用一个函数。应该叫“遍历操作”（cppreference 中叫 “批量操作”）。

`for_each(It_begin, It_end, UnaryFunc)`
`for_each_n(It_begin, n, UnaryFunc)`

- It_begin 和 It_end 是 ForwardIt 迭代器（可以前向遍历的迭代器）（还支持 InputIt，参考 cppreference）
- UnaryFunc 一般配合 lambda 函数用。也可以传函数对象。

比如，打印 vector：

```cpp
std::vector<int> vec{1, 1, 4, 5, 1, 4};

auto print_func = [&](int e){ std::cout << e << " "; };

std::for_each(vec.begin(), vec.end(), print_func);
std::cout << std::endl;
std::for_each_n(vec.begin(), vec.size(), print_func);  // same as for_each
```

### 变换操作

#### transform

> 无副作用的 map

transform 不会对原序列进行修改操作，而是产生新的序列。可以视作无副作用。属于“变换操作”。

`transform(It_src_begin, It_src_end, It_dest_begin, `

比如给 vector 每个元素乘以 2：

```cpp
std::vector<int> vec{1, 1, 4, 5, 1, 4};
std::vector<int> dest;
dest.reserve(vec.size());  // Important!!!

auto double_func = [](const e){ return e * 2; };

std::transform(vec.begin(), vec.end(), dest.begin(), dobule_func);
```

