# DeepSeek-V3 官方报告深入理解

第一次让我看到希望中国公司存在超越 openai 的可能性, 以前是想都不敢想(实测复杂代码编程的时候没有想象中强大). 本项目主要是对 DeepSeek-V3 的官方报告进行深入理解, 并提供详细的文档说明.

## 主要贡献

1. **架构创新**：
   - 无辅助损失的负载均衡策略，减少性能损失
   - 多令牌预测(MTP)目标的应用和验证

2. **训练效率突破**：
   - FP8混合精度训练在大规模模型上的首次验证
   - 通过算法、框架、硬件协同设计解决通信瓶颈
   - 显著降低训练成本（仅需2.664M H800 GPU小时）

3. **知识提炼方法**：
   - 从Chain-of-Thought模型中提取推理能力
   - 保持输出风格和长度的控制能力

4. **评估性能**：
   - 在教育领域基准测试中接近闭源模型水平
   - 在中文知识测试中超越部分闭源模型
   - 在数学和编程领域展现强大实力



### Architecture: Innovative Load Balancing Strategy and Training Objective
> * On top of the efficient architecture of DeepSeek-V2, we pioneer an auxiliary-loss-free strategy for load balancing, which minimizes the performance degradation that arises from encouraging load balancing.
> * We investigate a Multi-Token Prediction (MTP) objective and prove it beneficial to model performance. It can also be used for speculative decoding for inference acceleration.

### Pre-Training: Towards Ultimate Training Efficiency
> * We design an FP8 mixed precision training framework and, for the first time, validate the feasibility and effectiveness of FP8 training on an extremely large-scale model.
> * Through the co-design of algorithms, frameworks, and hardware, we overcome the communication bottleneck in cross-node MoE training, achieving near-full computation-communication overlap.
> * At an economical cost of only 2.664M H800 GPU hours, we complete the pre-training of DeepSeek-V3 on 14.8T tokens.

### Post-Training: Knowledge Distillation from DeepSeek-R1
> * We introduce an innovative methodology to distill reasoning capabilities from the long Chain-of-Thought (CoT) model into DeepSeek-V3.
> * Our pipeline elegantly incorporates the verification and reflection patterns of R1 into DeepSeek-V3 and notably improves its reasoning performance.


### Knowledge
DeepSeek-V3 在教育基准测试上表现优异：
- MMLU: 88.5
- MMLU-Pro: 75.9
- GPQA: 59.1

这些成绩超越了所有开源模型，接近 GPT-4o 和 Claude-Sonnet-3.5 的水平。在中文知识测试方面，甚至超越了这些闭源模型。

### Code, Math, and Reasoning
在数学和编程领域：
1. 数学能力：在非长链推理模型中达到最优水平
2. 编程能力：在编程竞赛基准测试（如 LiveCodeBench）中表现最佳
3. 工程任务：仅次于 Claude-Sonnet-3.5，但远超其他模型

## 文档导航

- [模型架构解析](training/model_structure.md)
- [训练方法说明](training/efficient_training.md)
- [基准测试分析](BENCHMARK_ANALYSIS.md) 

## 相关新闻

### AI 大牛评价
- **Andrej Karpathy**: DeepSeek 展示了如何用较少资源（2048个 GPU，2个月，600万美元）训练出前沿水平的 LLM
- **Sarah Guo**: 指出 DeepSeek-V3 仅需 2.788M H800 GPU 小时就能完成训练
- **Alexandr Wang**: 认为 DeepSeek-V3 与 GPT-4 和 Claude 3.5 Sonnet 性能相当，但计算量减少了10倍
- **贾扬清**: 正式进入了分布式推理时代




> **Sarah Guo** (@saranomous):
> "I don't think the US chip export controls are having their intended effect. Chinese model DeepSeek v3 very strong, and trained with OOM less money:
> - DeepSeek-V3 requires only 2.788M H800 GPU hours for its training
> - h800 is h100 with lower interchip bandwidth"

> **Andrej Karpathy** (@karpathy):
> "DeepSeek (Chinese AI co) making it look easy today with an open weights release of a frontier-grade LLM trained on a joke of a budget (2048 GPUs for 2 months, $6M).
>
> For reference, this level of capability is supposed to require clusters of closer to 16K GPUs, the ones being brought up today are more around 100K GPUs. E.g. Llama 3 405B used 30.8M GPU-hours, while DeepSeek-V3 looks to be a stronger model at only 2.8M GPU-hours (~11X less compute). If the model also passes vibe checks (e.g. LLM arena rankings are ongoing, my few quick tests went well so far) it will be a highly impressive display of research and engineering under resource constraints.
>
> Does this mean you don't need large GPU clusters for frontier LLMs? No but you have to ensure that you're not wasteful with what you have, and this looks like a nice demonstration that there's still a lot to get through with both data and algorithms.
>
> Very nice & detailed tech report too, reading through."

> **Alexandr Wang**:
> "It is quite fitting that DeepSeek, China's leading LLM lab, releases its latest model V3 on Christmas.
> - on-par with GPT-4o & Claude 3.5 Sonnet
> - trained w/10x less compute
>
> The bitter lesson of Chinese tech: they work while America rests, and catch up cheaper, faster & stronger"

<div style="display: grid; grid-template-columns: 250px 400px; gap: 10px;">
    <div style="display: flex; flex-direction: column; gap: 10px;">
        <img src="https://s2.loli.net/2024/12/27/UPqzbpxdrnfXmMj.jpg" width="300">
        <img src="https://s2.loli.net/2024/12/27/5EtRcrTQogesaCX.jpg" width="300">
        <img src="https://s2.loli.net/2024/12/27/isYFQtuBReE9Xg2.jpg" width="300">
    </div>
    <div>
        <img src="https://s2.loli.net/2024/12/27/YetWvKuwopDS2Rx.jpg" width="400">
    </div>
</div>