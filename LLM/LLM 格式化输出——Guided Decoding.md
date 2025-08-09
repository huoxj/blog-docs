---
date: 2025-08-09
---
## 介绍与示例

Guided decoding 技术能让大模型的输出满足特定的格式约束，如 Json、正则表达式等。并且，相比于在 prompt 中告知输出约束，guided decoding 是绝对稳定可靠的。

Guided decoding 也叫 structured output。下面是一个使用示例，约束大模型的输出为一个 pydantic 的 BaseModel：

```python
class AnimalModel(BaseModel):
	name: str
	type: str
	age: int

llm = ChatOpenAI(...)
structured_llm = llm.with_structured_output(AnimalModel)

resp = structured_llm.invoke("some prompt")
animal = AnimalModel.model_validate(resp)
```

这里大模型的输出是满足 AnimalModel 结构的定义的，即打印 resp 会得到形如这样的 dict：

```
{ name: xxx, type: yyy, age: 123 }
```

## 原理

首先，在得到结果的每一个 token 时，大模型实际输出了所有 token 在当前文本位置的概率。

而结构化输出必然使得某些文本位置上，只能输出固定的 token。比如 json 的第一个字符得是 `{` 或 `[`。

所以简单而言，只需将当前位置不可能出现的 token 概率置零，其他概率重新 softmax，便能实现可靠的结构化。

至于如何得到当前位置可能的 token 集合，使用编译器前端的思想即可。具体请移步编译原理。

## 如何增加 thinking

一些模型在给出回答前会有思考阶段。使用了 guided decoding 之后，模型就不会思考了，而是按给定的结构进行输出，导致模型能力大幅下降。

解决方法是将思考部分引入结构。以上面 Animal 为例：

```python
class AnimalWithThinking(BaseModel):
	thought: str
	result: AnimalModel

llm_with_thinking = llm.with_structured_output(AnimalWithThinking)
...
```

模型会在 thought 中完成思考，在 result 中得到 Animal 结构化的结果。