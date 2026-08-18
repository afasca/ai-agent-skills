# 打野工具包 (daye-toolkit)

两个 WorkBuddy Agent Skills 的整合包，配合使用可自动发现全球范围内提供
Claude / GLM / Kimi 模型免费接入的小众 API 平台，并做公司背调。

## 包内技能

```
daye-toolkit/
├── README.md                        ← 本说明文件
├── daye-basic/                       ← 打野基础版（核心搜索+筛选+背调技能）
│   ├── SKILL.md
│   └── discovered-platforms.md      （可选，跨批次去重追踪）
└── grok-search/                      ← Grok 搜索技能（可选的搜索后端）
    ├── SKILL.md
    └── scripts/
        └── grok_search.py            ← 核心脚本
```

## 两个技能的关系

| | daye-basic（打野基础版） | grok-search（Grok 搜索） |
|---|---|---|
| 作用 | 主技能：定义搜索策略、筛选规则、背调要求、输出报告格式 | 辅助技能：提供一个更强的搜索后端 |
| 依赖 | WorkBuddy 内置的 WebSearch + WebFetch | xAI API Key（付费）+ Python requests |
| 必须装？ | ✅ 是 | ❌ 可选（没它也能用内置 WebSearch 跑） |
| 怎么配合 | 定义"搜什么、怎么筛、怎么报" | 用 Grok 的实时网页搜索替代内置 WebSearch，结果更全更准 |

**简单说**：daye-basic 是大脑（规则），grok-search 是眼睛（搜索引擎）。两个都装上效果最好；只装 daye-basic 也能跑，只是用内置搜索。

---

## 技能一：daye-basic（打野基础版 v2.5.0）

### 功能
自动搜索全球（非中国）提供 Claude / GLM / Kimi 模型接入的 API 中转/聚合平台，
**必须有免费福利**才能入选，对每个平台做注册门槛评估 + 公司背调，生成结构化报告。

### 两道硬门槛（不通过直接杀）
1. **模型支持**：Claude 任意型号 / GLM 任意版本 / Kimi K3，任一即可
2. **免费福利必须有**：免费额度、聊天次数、积分、工作流搭建、试用期、Freemium 等任何形式都算——花钱的一点不给的直接排除

### 六条约束
1. 禁止中文网站
2. 禁止微信支付/支付宝/银联
3. 禁止 .cn 域名或面向中国大陆的服务
4. 不把 OpenRouter 等大众平台列为"新发现"（但可作定价对比基准）
5. **注册门槛评估（必做）**：绑卡要求、KYC 等级、注册难度评级、首次调用时间
6. **公司背调（必做）**：法律实体、注册地、团队规模、融资、创始人、声誉、风险评级

### 安装
复制 `daye-basic` 文件夹到 WorkBuddy 技能目录：
```
# 用户级（推荐，所有项目通用）
~/.workbuddy/skills/daye-basic/
├── SKILL.md
└── discovered-platforms.md   （可选）

# 或项目级（仅当前项目/团队）
<项目根>/.workbuddy/skills/daye-basic/
```

### 触发
安装后无需手动调用，在对话里说类似以下的话会自动触发：
- "帮我找便宜的 Claude API 中转"
- "有没有 GLM API 的免费额度平台"
- "Kimi K3 有没有免费接入的"
- "API scout" / "find cheap Claude API"

---

## 技能二：grok-search（Grok 实时网页搜索 v1.0.0）

### 功能
通过 xAI Grok 的内置 `web_search` 工具做实时网页搜索，支持并发搜索多个查询词，
返回答案 + 引用来源 URL。可作为 daye-basic 的搜索后端。

### 前提
- **需要 XAI_API_KEY 且充值**（xAI 无免费额度）
- 获取地址：https://console.x.ai/team/default/api-keys
- Python 3.10+ + requests 库

### 安装
复制 `grok-search` 文件夹到 WorkBuddy 技能目录：
```
~/.workbuddy/skills/grok-search/
├── SKILL.md
└── scripts/
    └── grok_search.py
```

配置环境变量：
```bash
# Windows (PowerShell)
[System.Environment]::SetEnvironmentVariable("XAI_API_KEY", "xai-xxxxx", "User")

# 或每次调用时传入
python grok_search.py --q "test" --api-key xai-xxxxx
```

### 使用
```bash
# 单次搜索
python scripts/grok_search.py --q "Claude API aggregator free credits"

# 并发搜索多个查询词（打野推荐用法）
python scripts/grok_search.py \
  --q "cheap Claude API relay" \
  --q "GLM API free credits" \
  --q "Kimi K3 API access" \
  --q "free AI API credits signup" \
  --q "indie LLM API marketplace" \
  --concurrent

# 域名过滤
python scripts/grok_search.py --q "Claude API" --allowed-domains reddit.com news.ycombinator.com
python scripts/grok_search.py --q "Claude API" --excluded-domains openrouter.ai

# 原始 JSON 输出
python scripts/grok_search.py --q "test" --json
```

---

## 两者配合使用流程

1. **配置 XAI_API_KEY**（如果要用 Grok 搜索后端）
2. **触发 daye-basic**：在对话里说"帮我找 Claude API 免费平台"之类
3. **搜索阶段**：
   - 如果有 grok-search + Key → 用 Grok 并发搜索 5-8 个查询词，收集 citations URL
   - 如果没有 → 回退到内置 WebSearch
4. **验证阶段**：对每个候选 URL 用 WebFetch 逐个检查（模型支持 → 免费福利 → 语言 → 支付 → 注册门槛 → 公司背调）
5. **输出报告**：5-7 个平台/批次的结构化 Markdown，可直接转 Word
6. **批次继续**：报告末尾问是否继续下一批，用 discovered-platforms.md 跨批去重

---

## 版本信息

| 技能 | 版本 | 日期 |
|------|------|------|
| daye-basic | v2.5.0 | 2026-08-17 |
| grok-search | v1.0.0 | 2026-08-17 |

### daye-basic 变更历史
- v2.0.0：合并重复技能
- v2.1.0：排除大众平台（如 OpenRouter）
- v2.2.0：大众平台可作对比基准
- v2.3.0：模型支持门槛 + 性价比优先
- v2.4.0：模型门槛放宽（Claude 任意型号/GLM 任意版本/Kimi K3）+ 免费福利定义放宽 + 公司背调
- v2.5.0：免费福利升级为硬门槛 + 注册门槛/KYC 评估

### grok-search 变更历史
- v1.0.0：初始版本，支持单次/并发搜索、域名过滤、JSON 输出

---

## 注意事项

- **daye-basic** 依赖 WebSearch / WebFetch，需开启网络访问
- **grok-search** 依赖 XAI_API_KEY + 充值（xAI 无免费额度）
- `discovered-platforms.md` 是可选的去重记忆文件，想让接收方从零开始就别带
- 报告中的定价/免费福利信息有时效性，使用前自行核实
- OpenRouter 等大众平台不算"新发现"，但其定价可作对比基准（设计如此）
- 注册门槛和公司背调是 daye-basic 的必做步骤
- grok-search 并发数建议不超过 5（xAI 有速率限制）
