---
date: 2025-06-14
---

使用 Y 不动点组合子：

```cpp
auto f = [](auto &&self, args) {
	self(self, args);
};

f(f, args);
```

~~别问，问就是软工一讲过的~~
