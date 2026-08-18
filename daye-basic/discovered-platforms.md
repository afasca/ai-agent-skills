# Discovered Platforms Tracker

This file tracks all platforms discovered across batches to avoid duplicates.

## Discovered Platforms

| Batch | Platform Name | URL | Date Discovered |
|-------|--------------|-----|-----------------|
| 1 | AIML API | aimlapi.com | 2026-07-13 |
| 1 | OpenRouter | openrouter.ai | 2026-07-13 |
| 1 | Requesty | requesty.ai | 2026-07-13 |
| 1 | Anannas | anannas.ai | 2026-07-13 |
| 1 | NanoGPT | nano-gpt.com | 2026-07-13 |
| 2 | Z.AI (Zhipu International) | z.ai | 2026-07-13 |
| 2 | DeepInfra | deepinfra.com | 2026-07-13 |
| 2 | derouter.ai | derouter.ai | 2026-07-13 |
| 2 | MidRelay | midrelay.com | 2026-07-13 |
| 2 | WorldRouter (WorldClaw) | worldclaw.ai | 2026-07-13 |
| 2 | ZenMux | zenmux.ai | 2026-07-13 |
| 3 | MixRoute | mixroute.ai | 2026-07-26 |
| 3 | APIXO | apixo.ai | 2026-07-26 |
| 3 | PoYo | poyo.ai | 2026-07-26 |
| 3 | AIgateway | aigateway.sh | 2026-07-26 |
| 3 | ClawAPI | clawapi.org | 2026-07-26 |
| 4 | NVIDIA Build | build.nvidia.com | 2026-07-26 |
| 4 | Vercel AI Gateway | vercel.com/ai-gateway | 2026-07-26 (Batch 3 曾排除，因确认 $5/月免费额度含 GLM-5.2 重新纳入) |
| 4 | ClaudeAPI.com | claudeapi.com | 2026-07-26 |
| 5 | Hugging Face Inference Providers | router.huggingface.co | 2026-07-26 |
| 5 | Together AI | together.ai | 2026-07-26 |
| 5 | Tencent Cloud TokenHub (International) | intl.cloud.tencent.com | 2026-07-26 |
| 5 | OpenCode Go | opencode.ai/go | 2026-07-26（边缘：订阅制+推荐码赠金） |
| 6 | Baseten | baseten.co | 2026-07-26（$30 注册赠金，GLM-5.2 已确认） |
| 6 | Fireworks AI | fireworks.ai | 2026-07-26（$1 赠金，GLM-5.2 已确认，600 RPM） |
| 6 | Nebius Token Factory | tokenfactory.nebius.com | 2026-07-26（$1 赠金，GLM-5.2 已确认） |
| 7 | CometAPI | cometapi.com | 2026-07-26（免费试用 tokens，Claude Opus 5/4.8/4.7 全线 20% off） |
| 7 | LinkModel | linkmodel.ai | 2026-07-26（$1 注册赠金，Claude Opus 4.8/4.7/4.6 最高 30% off） |
| 7 | Hypereal | hypereal.cloud | 2026-07-26（1 free credit≈$0.01，边缘收录，Claude Opus 4.6/4.7） |
| 8 | AgentRouter | agentrouter.org | 2026-07-26（$125-$200 GitHub 登录赠金，Claude Opus 4.6/4.7/4.8，公益站，用户放宽中文背景后纳入） |
| 8 | EasyRouter | easyrouter.io | 2026-07-26（400 积分注册赠金，傅盛/猎豹移动，Claude Opus 4.7，企业级） |
| 8 | GateRouter | gate.ai | 2026-07-26（等值 300 万 Token KYC 登录赠金，Claude 支持，Gate 交易所，Batch 3 曾排除现重新纳入） |
| 8 | HolySheep AI | holysheep.ai | 2026-07-26（starter credits≈200 次 Opus 4.7 请求，¥1=$1，微信/支付宝，用户放宽中文背景后纳入） |
| 8 | B.AI | b.ai | 2026-07-26（50 万积分注册赠金，Claude 全系列，孙宇晨，Batch 2 曾排除现重新纳入） |

## Excluded Platforms

| Platform Name | URL | Exclusion Reason |
|--------------|-----|------------------|
| Poe API | poe.com | 官方help.poe.com FAQ确认界面语言含简体中文/繁体中文，命中"中文本地化版本"排除条件 |
| Novita AI | novita.ai | 默认首页语言为中文，未确认稳定的纯英文入口 |
| Portkey | portkey.ai | 定位偏向企业级Gateway/治理工具而非典型中转站，且未直接确认Claude/GLM具体支持细节，定价门槛较高($49/月起) |
| SimplyLouie | simplylouie.com | 不支持 GLM-5.2 或 Claude Opus 4.6（仅支持 Claude Opus 4.5），未通过模型支持门槛 |
| AIPower | aipower.me | 支持微信支付和支付宝，命中中国支付方式排除条件 |
| B.AI | b.ai | 支持银联（UnionPay），命中中国支付方式排除条件；且与孙宇晨/TRON深度绑定，主要面向中国用户 |
| Gotoken | gotoken.ai | 支持支付宝，命中中国支付方式排除条件 |
| Router One | router.one | 支持微信支付和支付宝，命中中国支付方式排除条件 |
| FreeTheAi | freetheai.xyz | 不支持 GLM-5.2 或 Claude Opus 4.6（最高为 GLM-5.1 和 Claude Sonnet 4.5），未通过模型支持门槛 |
| SkillBoss | skillboss.co | 无法确认 GLM-5.2 或 Claude Opus 4.6 支持（仅笼统提及 Claude 和 GPT-5，博客提及 Claude 4.5 Opus），未通过模型支持门槛 |
| GateRouter | gaterouter.ai | 重定向至中文页面 (gate.ai/zh)，未能确认英文界面和具体模型支持 |
| Vercel AI Gateway | vercel.com/docs/ai-gateway | 属于 Vercel 云平台附属功能而非独立聚合站，未能确认具体支持的 GLM-5.2/Claude Opus 4.6 版本 |
| llmrelayapi | llmrelayapi.com | 不支持 GLM-5.2 或 Claude Opus 4.6（GLM 最高仅 5.1，无 Claude 模型），未通过模型支持门槛 |
| Aiberm | aiberm.com | 面向中国开发者，支持支付宝/微信支付，命中中国支付方式排除条件 |
| ofox.ai | ofox.ai | 支持支付宝/微信支付，主要面向中国用户，命中中国支付方式排除条件 |
| APIBox | apibox.cc | 中文站点，人民币结算，面向中国市场，命中排除条件 |
| Ccode | ccode.dev | 中文站点，支持微信支付/支付宝，命中中国支付方式排除条件 |
| OpusRelay | opusrelay.com | 面向中文社区推广（QQ群/微信客服），支持支付宝，命中排除条件 |
| IZIPAY | izipay.me | 虚拟信用卡服务而非 API 聚合平台，不属于本次目标类型 |
| gpuapis.com (CloudGPU) | gpuapis.com | 明确面向中国市场（CNY/USDT 结算、中国接入指南），命中"主要面向中国市场"排除条件 |
| Agnes AI | platform.agnes-ai.com | 仅提供自研 Agnes-2.0 系列模型，不支持 GLM-5.2 / Claude Opus 4.6，未通过模型支持门槛 |
| FreeModel | freemodel.dev | 官网仅称"开源模型池"路由，无法确认 GLM-5.2 / Claude Opus 4.6 具体支持；且被列为"小平台勿大额充值"，谨慎排除 |
| AgentRouter | agentrouter.org | 文档为中文（docs.agentrouter.org），面向中文开发者社区推广，命中中文站点排除条件 |
| QuotaPass | quotapass.com | 海南洋浦离岸算力、面向跨境中国市场，Claude 未上线（仅 GLM/DeepSeek），GLM-5.2 $3.60/$7.20 无免费额度 |
| ClaudeStore | claudestore.store | 中文站点（/zh/ 默认推广），命中中文站点排除条件 |
| Anthropic 官方 $5 | console.anthropic.com | 官方渠道而非聚合/中转平台，不属于本次发现类型（可作为免费基准参考） |
| Groq | groq.com | 免费层慷慨（30 RPM/14400 RPD）但不托管 GLM-5.2/Claude，未通过模型门槛 |
| Cerebras | cerebras.ai | 免费层限速访问但无 GLM-5.2/Claude 旗舰，未通过模型门槛 |
| Devin (Cognition) | devin.ai | GLM-5.2 免费仅捆绑在付费 Pro 计划内，非免费额度平台 |
| 七牛云 AI (Qiniu) | qnaigc.com | 中国云厂商、人民币计价，命中中国市场排除条件 |
| 阿里云百炼 / bigmodel.cn 20M tokens | - | 中国大陆平台，需实名/中国手机号，命中排除条件 |
| Anyscale | anyscale.com | Endpoints 模型池仅 Llama/Mistral/Gemma，无 GLM-5.2/Claude，未通过模型门槛（$10 赠金作废） |
| Hyperbolic | app.hyperbolic.ai | 定位 GPU 租赁+推理云，未确认 GLM-5.2/Claude 托管，$1 赠金过小且模型门槛存疑 |
| SambaNova | sambanova.ai | 模型池为 Llama/DeepSeek/Qwen，无 GLM-5.2/Claude，未通过模型门槛 |
| AI21 / Upstage / NLP Cloud | - | 自研模型平台（Jamba/Solar 等），无 GLM-5.2/Claude，未通过模型门槛 |
| MNAPI | mnapi.com | Cloudflare 盾无法直接验证，来源为中文导航站（$1 赠金），疑似中国市场平台，谨慎排除 |
| API易 / MKEAI | apiyi.com / api.mkeai.com | 中文站点，命中中文站点排除条件 |
| Parasail | parasail.io | GLM-5.2 $1.40/$4.40 确认托管，但官网无明确注册赠金（仅"trial 可能有"传闻），不满足免费额度硬性要求 |
| DGX Cloud Lepton | lepton.ai | 已并入 NVIDIA Build（Batch 4 已收录），旧 $10 赠金记录失效，不重复收录 |
| Novita AI | novita.ai | Batch 1 已排除（默认中文首页）；虽确认托管 GLM-5.2 且 35% off，仍维持排除 |
| Aiapiflow | aiapiflow.com | 无注册免费赠金（须购买 Starter 包 $3→$25），Claude 4.7/4.8/5 80% off 但不满足免费额度要求 |
| FreeModel | freemodel.dev | 仅路由开源模型池，不含 Claude（闭源）；thescience360 宣称的"$100 免费 Opus 4.8"为误导信息 |
| HolySheep AI | holysheep.ai | 支持微信支付+支付宝，¥1=$1 中国市场定价，命中中国支付方式排除条件 |
| AgentRouter | agentrouter.org | Batch 4 已排除（中文文档）；虽有 GitHub 登录免费 Opus 4.8 额度，维持排除 |
| SkillBoss | skillboss.co | $2 赠金但仅 Claude 4.5 Opus（低于 4.6 门槛），未通过模型支持门槛 |
| FounderPass/LLM API | founderpass.com | $50-$300 额度需先充值 $50-$300（2x 匹配）+企业邮箱，属充值匹配非免费注册赠金 |
| Anthropic 官方 $5 | console.anthropic.com | 官方渠道，非聚合/中转平台（Baseline，已在 Batch 4 排除） |

## Batch 2 Notes

- **derouter.ai**: 默认语言为简体中文（有 EN 切换），作为风险提示列入报告。支持加密货币与银行卡付款，无中国支付方式，有完整英文版。
- **OpenRouter** (openrouter.ai): Batch 1 已记录但实际为主流平台，不应作为"发现"列出。其 GLM-5.2 定价 ($0.93-3.00/M input) 作为比较基准使用。
- **OmniRoute** (omniroute.online): 本地优先的开源 AI 网关工具（非托管云服务），聚合 236 个 provider。未能确认 GLM-5.2/Claude Opus 4.6 具体支持，未列入正式发现但值得关注。

## Batch 2 Candidates (not yet fully verified)

| Platform Name | URL | Note |
|--------------|-----|------|
| Vercel AI Gateway | vercel.com/docs/ai-gateway | 确认支持Claude+GLM，零加价BYOK模式，但定位为Vercel云平台附属功能而非独立聚合站，需在Batch 2中进一步评估是否符合"独立中转平台"定位 |
