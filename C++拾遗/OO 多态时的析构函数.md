---
date: 2025-07-17
---
记录一个很唐的错误。

```cpp
class Base{};
class Derived: public Base {
public:
	Derived(...);
private:
	std::unique_ptr<...> ptr;
}
```

这种情况下，创建一个 Derived 对象：

```cpp
Base *derived = new Derived(...);
```

在出 derived 对象的作用域时，调用的是 Base 的析构函数。所以 derived 的 ptr 持有的对象不会被释放。

因为析构函数应该是动态的，这才能保证对象释放时调用到了正确的析构：

```cpp
class Base{
public:
	virtual ~Base() = default;
};
class Derived: public Base{
public:
	~Derived() override = default;
...
}
```
