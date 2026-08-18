---
name: grok-search
version: "1.0.0"
description: >
  Real-time web search via xAI Grok API's built-in web_search tool. Calls the
  /v1/responses endpoint with tools=[{"type":"web_search"}] to let Grok search the live
  web and return answers with cited source URLs. Supports concurrent multi-query
  searches (e.g. running 5-8 different search terms in parallel), domain filtering
  (allowed_domains / excluded_domains), and structured JSON output. Requires
  XAI_API_KEY (no free tier — must purchase credits at https://console.x.ai).
  Ideal as a search backend for the daye-basic (打野基础版) API scout skill, or any
  workflow needing fresh web results with source citations.
  Triggers: "grok search", "grok web search", "xAI search", "search via grok",
  "concurrent web search", "grok 搜索", "用 grok 搜".
agent_created: true
---

# Grok Search - Real-time Web Search via xAI Grok API

## 功能
通过 xAI Grok 的内置 `web_search` 工具做实时网页搜索。Grok 会自己搜网页、读内容、
返回答案，并附带引用来源 URL。支持并发搜索多个查询词。

## 依赖
- Python 3.10+
- `requests` 库
- **XAI_API_KEY**（必填，xAI 无免费额度，需在 https://console.x.ai 充值）

## 环境变量
```
XAI_API_KEY=xai-xxxxxxxxxxxx
```
获取地址：https://console.x.ai/team/default/api-keys

## 使用方法

### 单次搜索
```bash
python scripts/grok_search.py --q "Claude API aggregator free credits"
```

### 并发搜索多个查询词
```bash
python scripts/grok_search.py \
  --q "cheap Claude API relay" \
  --q "GLM API free credits" \
  --q "Kimi K3 API access" \
  --concurrent
```

### 输出原始 JSON
```bash
python scripts/grok_search.py --q "test" --json
```

### 指定 API Key（不用环境变量）
```bash
python scripts/grok_search.py --q "test" --api-key xai-xxxxx
```

### 限制搜索域名
```bash
# 只搜 reddit 和 hackernews
python scripts/grok_search.py --q "Claude API" --allowed-domains reddit.com news.ycombinator.com

# 排除 openrouter.ai
python scripts/grok_search.py --q "Claude API" --excluded-domains openrouter.ai
```

### 指定模型
```bash
python scripts/grok_search.py --q "test" --model grok-4.6
```

## 输出格式

### 人类可读格式（默认）
```
============================================================
🔍 查询: Claude API aggregator free credits
============================================================

📝 回答:
[Grok 的搜索结果回答...]

📎 引用来源（5 个）:
  1. https://example.com/platform1
  2. https://reddit.com/r/...
  ...

============================================================
🔗 所有去重后的来源 URL（共 12 个）:
============================================================
  1. https://...
  2. https://...
```

### JSON 格式（--json）
返回 xAI /v1/responses 接口的原始 JSON，包含：
- `output[].content[].text` - 回答正文
- `output[].content[].annotations[]` - 引用标注（含 url, title, start_index, end_index）
- `citations` - 简单 URL 列表

## 工作原理
1. 向 `https://api.x.ai/v1/responses` 发 POST 请求
2. 请求体带 `tools: [{"type": "web_search"}]`
3. Grok 自主决定调用搜索工具，实时浏览网页
4. 返回答案文本 + 引用来源 URL
5. 脚本提取 `annotations` 中的 `url_citation` 和顶层 `citations` 列表

## 费用提醒
- xAI API **没有免费额度**，调用即扣费
- web_search 工具会增加 token 消耗（搜索 + 浏览网页内容）
- 建议 `--max-results` 控制单次搜索规模
- 监控余额：https://console.x.ai

## 接入打野基础版
可作为 daye-basic 技能的搜索后端：
1. 设置 `XAI_API_KEY` 环境变量
2. 用并发模式（--concurrent）一次性跑 5-8 个查询词
3. 收集所有 citations URL 作为候选平台
4. 再用 WebFetch 逐个验证（语言、支付方式、模型、免费福利等）

## 限制
- `allowed_domains` / `excluded_domains` 最多各 5 个
- 并发数建议不超过 5（xAI 有速率限制，触发 429）
- 单次请求超时默认 120s（搜索 + 浏览网页较慢）
