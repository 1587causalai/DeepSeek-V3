# DeepSeek-V3 模型权重文件说明文档

## `config.json` 中的新增字段

- **model_type**: 模型类型，在本次发布中更新为 `deepseek_v3`
- **num_nextn_predict_layers**: 多令牌预测模块（Multi-Token Prediction, MTP）的数量。本次开源的 V3 权重包含 **1个 MTP 模块**
- **quantization_config**: FP8 量化配置信息

---

## 权重文件结构概述

DeepSeek-V3 权重文件主要包含两个部分：**主模型权重**和 **MTP 模块**。

### 1. 主模型权重

- **组成部分**:
  - 输入/输出嵌入层和完整的 61 层 Transformer 隐藏层
- **参数统计**:
  - 总参数量：**671B**
  - 激活参数量：**36.7B**（其中包括嵌入层的 0.9B 和输出层的 0.9B）

#### 结构详情

- **嵌入层**:
  - `model.embed_tokens.weight`
- **Transformer 隐藏层**:
  - 从 `model.layers.0` 到 `model.layers.60`，共 `num_hidden_layers` 层
- **输出层**:
  - `model.norm.weight`
  - `lm_head.weight`

### 2. 多令牌预测（MTP）模块

- **组成部分**:
  - 由 `num_nextn_predict_layers` 字段定义的额外 MTP 模块，本模型中设置为 1
- **参数统计**:
  - 独立参数量：**11.5B**（不包括与主模型共享的 0.9B 嵌入层和 0.9B 输出层）
  - 激活参数量：**2.4B**（包括共享的 0.9B 嵌入层和 0.9B 输出层）

#### 结构详情

- **embed_tokens**: 与主模型权重的嵌入层**共享参数**
- **enorm & hnorm**: 用于推测解码的 RMSNorm 参数
- **eh_proj**: 用于规范化结果降维投影的参数
- **额外的 Transformer 隐藏层**:
  - `model.layers.61.self_attn & mlp`（结构与主模型隐藏层相同）
- **shared_head**: 与主模型权重的输出层**共享参数**

---

### 加载规则

- **主模型权重**: 通过 `config.json` 中的 `num_hidden_layers` 参数加载
- **MTP 模块**: 通过 `num_nextn_predict_layers` 参数加载，层 ID 紧接在主模型隐藏层之后。例如：
  - 当 `num_hidden_layers = 61` 且 `num_nextn_predict_layers = 1` 时，MTP 模块的层 ID 为 `61`

---

## FP8 权重说明

DeepSeek-V3 原生支持 128x128 块缩放的 FP8 权重格式。

### FP8 配置

FP8 权重文件在 `quantization_config` 字段中描述了量化方法。配置示例如下：

```json
"quantization_config": {
  "activation_scheme": "dynamic",
  "fmt": "e4m3",
  "quant_method": "fp8",
  "weight_block_size": [128, 128]
}
```

- **量化格式**:
  - 格式类型：`fp8` 和 `e4m3`（对应 `torch.float8_e4m3fn`）
  - 权重块大小：`128x128`
- **激活量化方案**:
  - 使用动态激活量化（`dynamic`）

### 反量化方法

FP8 权重文件包含 `weight_scale_inv` 字段，用于存储每个权重块的反量化比例。

- **存储格式**: `float32 Tensor`，与权重数据一起存储
- **反量化公式**:
  - 如果权重块不是 128 的整数倍，会先用零填充到 128，计算比例后再移除填充部分
  - 反量化过程：`(128x128 权重块) * weight_scale_inv`

通过 FP8 权重的反量化，运行时操作可以实现 `每个令牌每128通道` 粒度的在线量化。

---
