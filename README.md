# 光栅化：Bresenham、裁剪与圆

像素线断断续续、画布外的线把坐标撑爆：Bresenham 步进符号反，裁剪没有编码端点，圆只画一个象限，矩形包含判断把边界排除，填充跨度少一个像素，空输入崩，批量光栅化只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
render/__init__.py
render/raster.py
tests/test_raster.py
```

## 当前状态

`render/raster.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_raster.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. Bresenham 步进符号
2. 端点编码裁剪
3. 圆的八对称
4. 矩形包含含边界
5. 填充跨度含端点
6. 空输入兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `render/raster.py`
后 15 条用例应全部通过。
