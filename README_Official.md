# DeepSeek-V3: 开创性的大规模语言模型



## 1. 项目简介

DeepSeek-V3是一个突破性的大规模语言模型，它采用了混合专家系统(MoE)架构：
- 总参数量：671B（6710亿）
- 实际计算时激活参数：37B（370亿）
- 上下文窗口：128K tokens

### 主要技术特点：

1. **高效的模型架构**
   - 采用多头潜在注意力机制(MLA)
   - 使用DeepSeekMoE架构
   - 这些技术在DeepSeek-V2中已经得到验证

2. **创新的训练方法**
   - 首创无辅助损失的负载均衡策略
   - 引入多token预测训练目标
   - 显著提升了模型性能
   - 

3. **大规模预训练**
   - 在14.8万亿高质量、多样化的token上进行预训练
   - 通过监督微调(SFT)和强化学习(RL)进一步提升能力
   - 整个训练过程异常稳定，没有出现不可恢复的损失峰值

4. **出色的性能表现**
   - 超越其他开源模型
   - 达到与顶级闭源模型相当的水平
   - 仅需2.788M H800 GPU小时即可完成训练

<p align="center">
  <img width="80%" src="figures/benchmark.png">
  <br>
  <em>DeepSeek-V3与其他模型的性能对比</em>
</p>

## 2. 模型特色

### 创新的架构设计

1. **负载均衡策略**
   - 首创无辅助损失的均衡方法
   - 最大限度减少了为了实现负载均衡而带来的性能损失
   
2. **多Token预测(MTP)**
   - 创新的训练目标设计
   - 可用于推理加速的预测解码
   - 显著提升模型整体性能

### 极致的训练效率

1. **FP8混合精度训练**
   - 首次在超大规模模型上验证FP8训练的可行性
   - 证明了其有效性

FP8（8位浮点数）训练就像是用更小的纸记录数字，虽然能节省空间和���高速度，但原本大家担心精度太低会导致训练失败或效果变差。DeepSeek-V3成功在超大模型上验证了FP8训练的可行性，证明了即使"用更小的纸"也能准确记录训练所需的信息，这让模型训练更省内存、更快速，同时还能保持良好的性能。

2. **突破性的训练优化**
   - 算法、框架、硬件的协同设计
   - 解决了跨节点MoE训练的通信瓶颈
   - 实现了计算与通信的近乎完美重叠
   - 显著提升训练效率，降低成本

3. **高效的训练成本**
   - 预训练仅需2.664M H800 GPU小时
   - 后续训练阶段仅需0.1M GPU小时
   - 在14.8T tokens上完成训练
   - 产出了目前最强的开源基础模型

### 知识蒸馏创新

- 从DeepSeek-R1系列模型中提取推理能力
- 创新的方法将R1的验证和反思模式整合到V3中
- 显著提升推理性能
- 同时保持对输出风格和长度的控制

[接下来是模型下载、评测结果等章节，需要我继续翻译吗？]

## 3. 模型下载

<div align="center">

| **模型版本** | **总参数量** | **激活参数量** | **上下文长度** | **下载链接** |
|:------------:|:------------:|:------------:|:------------:|:------------:|
| DeepSeek-V3-Base | 671B | 37B | 128K | [🤗 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base) |
| DeepSeek-V3 | 671B | 37B | 128K | [🤗 HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V3) |

</div>

**特别说明**: DeepSeek-V3在HuggingFace上的模型总大小为685B，这包括：
- 主模型权重：671B
- 多Token预测(MTP)模块权重：14B

### 运行环境支持

为了确保模型能够灵活高效地运行，我们与开源社区和硬件厂商展开合作，提供了多种本地运行方案。具体部署方法请参考第6节：[本地部署指南](#6-本地部署指南)。

对于想深入了解模型的开发者，我们建议查看[README_WEIGHTS.md](./README_WEIGHTS.md)，其中详细介绍了主模型权重和多Token预测(MTP)模块的相关信息。需要注意的是，MTP功能目前正在社区中积极开发中，我们欢迎您的贡献和反馈。

## 4. 评测结果

### 基础模型评测

#### 标准基准测试

<div align="center">


| 评测类别 | 测试基准 (指标) | DeepSeek-V2 | Qwen2.5 72B | LLaMA3.1 405B | DeepSeek-V3 |
|---------|----------------|-------------|--------------|---------------|-------------|
| 模型架构 | - | MoE | Dense | Dense | MoE |
| 激活参数量 | - | 21B | 72B | 405B | 37B |
| 总参数量 | - | 236B | 72B | 405B | 671B |
| 英语理解 | MMLU (准确率) | 78.4 | 85.0 | 84.4 | **87.1** |
| 代码能力 | HumanEval (Pass@1) | 43.3 | 53.0 | 54.9 | **65.2** |
| 数学能力 | GSM8K (准确率) | 81.6 | 88.3 | 83.5 | **89.3** |
| 中文理解 | C-Eval (准确率) | 81.4 | 89.2 | 72.5 | **90.1** |

</div>

**说明**：
- 加粗数字表示最佳结果
- 相差不超过0.3的分数被视为相同水平
- DeepSeek-V3在大多数测试中都取得了最佳成绩，尤其在数学和编程任务上表现突出

#### 上下文窗口测试

<p align="center">
  <img width="80%" src="figures/niah.png">
  <br>
  <em>"大海捞针"(NIAH)测试结果：DeepSeek-V3在最长128K的上下文长度下都保持稳定的性能表现</em>
</p>


### 对话模型评测

#### 标准基准测试（针对67B以上大模型）

<div align="center">

| 评测类别 | 测试基准 (指标) | DeepSeek-V3 | Claude-3.5 | GPT-4 | 说明 |
|---------|----------------|-------------|------------|--------|------|
| 英语理解 | MMLU (准确率) | **88.5%** | 88.3% | 87.2% | 考察多领域知识理解 |
| | MMLU-Redux | **89.1%** | 88.9% | 88.0% | 更新版多领域测试 |
| | DROP (3-shot F1) | **91.6%** | 88.3% | 83.7% | 阅读理解与推理 |
| 代码能力 | HumanEval-Mul | **82.6%** | 81.7% | 80.5% | 多语言编程测试 |
| | LiveCodeBench | **40.5%** | 36.3% | 33.4% | 实时代码生成能力 |
| | Codeforces | **51.6%** | 20.3% | 23.6% | 竞赛级编程题目 |
| 数学能力 | MATH-500 | **90.2%** | 78.3% | 74.6% | 高等数学解题 |
| | AIME 2024 | **39.2%** | 16.0% | 9.3% | 美国数学邀请赛题目 |
| 中文能力 | C-Eval | **86.5%** | 76.7% | 76.0% | 中文综合能力评估 |

</div>

**评测说明**：
- 所有模型的输出长度都限制在8K以内
- 对于样本量少于1000的测试，采用不同温度参数多次测试以确保结果可靠
- DeepSeek-V3作为开源模型，在多个领域超越了主流闭源模型

#### 开放式生成评测

<div align="center">

| 模型 | Arena-Hard | AlpacaEval 2.0 |
|------|------------|----------------|
| DeepSeek-V3 | **85.5** | **70.0** |
| Claude-3.5 | 85.2 | 52.0 |
| GPT-4 | 80.4 | 51.1 |

</div>

**说明**：这是英语开放式对话的评测结果。AlpacaEval 2.0使用长度控制后的胜率作为指标。

## 5. 在线服务

您可以在DeepSeek官方网站体验DeepSeek-V3：[chat.deepseek.com](https://chat.deepseek.com/sign_in)

我们提供兼容OpenAI的API服务：[platform.deepseek.com](https://platform.deepseek.com/)

## 6. 本地部署指南

DeepSeek-V3支持多种部署方式，可以在不同的硬件平台上运行：


1. **DeepSeek-Infer Demo**
   - 提供轻量级演示
   - 支持FP8和BF16推理

2. **SGLang**（推荐）
   - 完整支持FP8和BF16推理
   - 支持MLA优化
   - 支持FP8 KV缓存
   - 支持Torch编译加速

3. **LMDeploy**（推荐）
   - 高性能推理框架
   - 支持本地和云端部署
   - 支持FP8和BF16推理

4. **TensorRT-LLM**（推荐）
   - 支持BF16推理
   - 支持INT4/8量化
   - FP8支持即将推出

5. **AMD GPU支持**
   - 通过SGLang实现
   - 支持FP8和BF16模式

6. **华为昇腾NPU支持**
   - 支持在昇腾设备上运行


由于我们在训练中原生采用FP8，目前只提供FP8权重。如果需要BF16权重进行实验，可以使用提供的转换脚本：

```shell
cd inference
python fp8_cast_bf16.py --input-fp8-hf-path /path/to/fp8_weights --output-bf16-hf-path /path/to/bf16_weights
```


### 6.1 使用DeepSeek-Infer Demo部署（示例）

#### 准备工作

1. **获取代码和依赖**
```shell
# 克隆代码仓库
git clone https://github.com/deepseek-ai/DeepSeek-V3.git

# 安装依赖
cd DeepSeek-V3/inference
pip install -r requirements.txt
```

2. **下载模型权重**
- 从HuggingFace下载模型权重
- 将权重文件放入`/path/to/DeepSeek-V3`目录

#### 模型权重转换

需要将HuggingFace格式的权重转换为特定格式：

```shell
python convert.py \
    --hf-ckpt-path /path/to/DeepSeek-V3 \
    --save-path /path/to/DeepSeek-V3-Demo \
    --n-experts 256 \
    --model-parallel 16
```

**参数说明**：
- `--n-experts`: MoE专家数量，默认256
- `--model-parallel`: 模型并行度，影响显存使用
- `--hf-ckpt-path`: 原始权重路径
- `--save-path`: 转换后权重保存路径

#### 运行模型

1. **交互式对话模式**
```shell
torchrun --nnodes 2 --nproc-per-node 8 \
    generate.py \
    --node-rank $RANK \
    --master-addr $ADDR \
    --ckpt-path /path/to/DeepSeek-V3-Demo \
    --config configs/config_671B.json \
    --interactive \
    --temperature 0.7 \
    --max-new-tokens 200
```

**参数详解**：
- `--nnodes 2`: 使用2个计算节点
- `--nproc-per-node 8`: 每个节点使用8个GPU
- `--temperature 0.7`: 采样温度，控制输出随机性
- `--max-new-tokens 200`: 限制生成长度

2. **批量推理模式**
```shell
torchrun --nnodes 2 --nproc-per-node 8 \
    generate.py \
    --node-rank $RANK \
    --master-addr $ADDR \
    --ckpt-path /path/to/DeepSeek-V3-Demo \
    --config configs/config_671B.json \
    --input-file $FILE
```

### 6.2 使用SGLang部署（推荐）

[SGLang](https://github.com/sgl-project/sglang)提供了最完整的DeepSeek-V3优化支持：

#### 核心特性

1. **高性能优化**
   - MLA (Multi-head Latent Attention) 优化
   - FP8 (W8A8) 权重量化
   - FP8 KV Cache 优化
   - Torch Compile 即时编译加速

2. **硬件支持**
   - NVIDIA GPU全系列支持
   - AMD GPU原生支持（通过ROCm）
   - 支持混合精度推理

#### 部署步骤

1. **安装SGLang**
```shell
pip install sglang>=0.4.1
```

2. **加载模型**
```python
import sglang as sgl

# 创建模型配置
config = sgl.ModelConfig(
    model_path="/path/to/DeepSeek-V3",
    tensor_parallel_size=8,  # GPU数量
    max_tokens=128000,       # 最大上下文长度
    dtype="fp8",            # 或 "bf16"
)

# 初始化模型
model = sgl.Model(config)
```

3. **运行推理**
```python
# 示例：对话生成
response = model.generate(
    prompt="请解释量子计算的基本原理",
    max_tokens=1000,
    temperature=0.7,
    top_p=0.95
)
```

### 6.3 使用LMDeploy部署（推荐）

[LMDeploy](https://github.com/InternLM/lmdeploy)提供了完整的部署方案：

#### 特性优势

1. **推理优化**
   - 支持FP8/BF16精度
   - 动态批处理
   - 注意力缓存优化
   - 自动显存管理

2. **部署方式**
   - 本地命令行部署
   - RestAPI服务部署
   - 网页Demo部署

#### 快速开始

1. **安装LMDeploy**
```shell
pip install lmdeploy
```

2. **转换模型**
```shell
python -m lmdeploy.serve.turbomind.deploy \
    --model-path /path/to/DeepSeek-V3 \
    --model-format hf \
    --tp 8
```

3. **启动服务**
```shell
# API服务
lmdeploy serve api_server --model-path workspace --tp 8

# Web UI
lmdeploy serve web_demo --model-path workspace --tp 8
```


