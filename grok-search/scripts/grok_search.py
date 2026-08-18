#!/usr/bin/env python3
"""
Grok Web Search - 通过 xAI Grok API 的 web_search 工具做实时网页搜索
接口：POST https://api.x.ai/v1/responses
文档：https://docs.x.ai/developers/tools/web-search

用法：
  # 单次搜索
  python grok_search.py --q "Claude API aggregator free credits"

  # 并发搜索多个查询词
  python grok_search.py --q "query1" --q "query2" --q "query3" --concurrent

  # 输出原始 JSON
  python grok_search.py --q "test" --json

  # 指定 API Key（也可用环境变量 XAI_API_KEY）
  python grok_search.py --q "test" --api-key xai-xxxxx

  # 限制每个查询的搜索结果数 / 只搜特定域名
  python grok_search.py --q "test" --max-results 10
  python grok_search.py --q "test" --allowed-domains reddit.com hackernews.com

环境变量：
  XAI_API_KEY  - xAI API 密钥（必填，前往 https://console.x.ai 获取）
"""

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("缺少依赖库，请先安装：pip install requests", file=sys.stderr)
    sys.exit(1)

API_URL = "https://api.x.ai/v1/responses"
DEFAULT_MODEL = "grok-4.6"


def get_api_key(arg_key: str | None) -> str:
    """优先用参数传入的 key，其次读环境变量 XAI_API_KEY"""
    key = arg_key or os.environ.get("XAI_API_KEY", "").strip()
    if not key:
        print("❌ 缺少 XAI_API_KEY。请通过 --api-key 传入或设置环境变量 XAI_API_KEY。", file=sys.stderr)
        print("   获取地址：https://console.x.ai/team/default/api-keys", file=sys.stderr)
        sys.exit(1)
    return key


def grok_search(
    q: str,
    api_key: str,
    model: str = DEFAULT_MODEL,
    max_results: int | None = None,
    allowed_domains: list[str] | None = None,
    excluded_domains: list[str] | None = None,
    timeout: int = 120,
) -> dict:
    """调用 xAI /v1/responses 接口，带 web_search 工具，返回完整响应 JSON"""

    tool: dict = {"type": "web_search"}
    filters: dict = {}
    if allowed_domains:
        filters["allowed_domains"] = allowed_domains[:5]  # max 5
    if excluded_domains:
        filters["excluded_domains"] = excluded_domains[:5]
    if filters:
        tool["filters"] = filters

    payload: dict = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": (
                    f"Search the web for: {q}\n\n"
                    "Return a concise factual answer. List the most relevant sources you found "
                    "as a numbered list at the end with their URLs. Focus on concrete, verifiable "
                    "information (platform names, URLs, pricing, features)."
                ),
            }
        ],
        "tools": [tool],
    }
    if max_results is not None:
        payload["tool_choice"] = "auto"  # 让模型自主决定调用搜索

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "timeout", "message": f"请求超时（{timeout}s）"}
    except requests.exceptions.HTTPError as e:
        body = ""
        try:
            body = e.response.text[:800]
        except Exception:
            pass
        return {"error": "http_error", "status": e.response.status_code, "body": body}
    except requests.exceptions.RequestException as e:
        return {"error": "request_error", "message": str(e)}


def extract_results(resp: dict) -> dict:
    """从 /v1/responses 响应里提取有用的搜索结果：正文 + citations + annotations"""
    out = {
        "answer_text": "",
        "citations": [],
        "annotations": [],
        "raw_error": None,
    }

    if "error" in resp:
        out["raw_error"] = resp
        return out

    # citations: 简单 URL 列表
    citations = resp.get("citations") or []
    out["citations"] = citations

    # output[].content[].text + annotations
    output = resp.get("output") or []
    for item in output:
        contents = item.get("content") or []
        for c in contents:
            if c.get("type") == "output_text":
                out["answer_text"] += c.get("text", "")
                for ann in c.get("annotations") or []:
                    if ann.get("type") == "url_citation":
                        out["annotations"].append(
                            {
                                "url": ann.get("url", ""),
                                "title": ann.get("title", ""),
                                "start_index": ann.get("start_index"),
                                "end_index": ann.get("end_index"),
                            }
                        )
    return out


def print_human_result(q: str, result: dict, raw: dict | None = None):
    """人类可读格式输出"""
    print(f"\n{'='*60}")
    print(f"🔍 查询: {q}")
    print(f"{'='*60}")

    if result.get("raw_error"):
        print(f"❌ 请求失败: {json.dumps(result['raw_error'], ensure_ascii=False, indent=2)}")
        return

    if result["answer_text"]:
        print(f"\n📝 回答:\n{result['answer_text']}")

    if result["annotations"]:
        print(f"\n📎 引用来源（{len(result['annotations'])} 个）:")
        seen = set()
        idx = 1
        for ann in result["annotations"]:
            url = ann.get("url", "")
            if url and url not in seen:
                seen.add(url)
                print(f"  {idx}. {url}")
                idx += 1

    if not result["annotations"] and result["citations"]:
        print(f"\n📎 Citations（{len(result['citations'])} 个）:")
        for i, url in enumerate(result["citations"], 1):
            print(f"  {i}. {url}")


def main():
    parser = argparse.ArgumentParser(description="Grok Web Search via xAI API")
    parser.add_argument("--q", action="append", required=True,
                        help="搜索查询词（可多次指定以搜索多个词）")
    parser.add_argument("--api-key", default=None,
                        help="xAI API Key（也可用环境变量 XAI_API_KEY）")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"模型名（默认 {DEFAULT_MODEL}）")
    parser.add_argument("--max-results", type=int, default=None,
                        help="提示模型限制搜索结果数（API 不强制）")
    parser.add_argument("--allowed-domains", nargs="*", default=None,
                        help="只搜这些域名（最多5个）")
    parser.add_argument("--excluded-domains", nargs="*", default=None,
                        help="排除这些域名（最多5个）")
    parser.add_argument("--concurrent", action="store_true",
                        help="并发执行多个查询词")
    parser.add_argument("--json", action="store_true",
                        help="输出原始 JSON（不格式化）")
    parser.add_argument("--timeout", type=int, default=120,
                        help="单次请求超时秒数（默认120）")
    args = parser.parse_args()

    api_key = get_api_key(args.api_key)
    queries = args.q

    if len(queries) == 1:
        # 单查询
        raw = grok_search(
            queries[0], api_key, model=args.model,
            max_results=args.max_results,
            allowed_domains=args.allowed_domains,
            excluded_domains=args.excluded_domains,
            timeout=args.timeout,
        )
        if args.json:
            print(json.dumps(raw, ensure_ascii=False, indent=2))
        else:
            extracted = extract_results(raw)
            print_human_result(queries[0], extracted, raw)
    else:
        # 多查询
        print(f"🚀 共 {len(queries)} 个查询，{'并发' if args.concurrent else '顺序'}执行...\n")
        all_results = {}

        def run_one(q):
            return q, grok_search(
                q, api_key, model=args.model,
                max_results=args.max_results,
                allowed_domains=args.allowed_domains,
                excluded_domains=args.excluded_domains,
                timeout=args.timeout,
            )

        if args.concurrent:
            with ThreadPoolExecutor(max_workers=min(len(queries), 5)) as ex:
                futures = {ex.submit(run_one, q): q for q in queries}
                for fut in as_completed(futures):
                    q, raw = fut.result()
                    all_results[q] = raw
                    if not args.json:
                        extracted = extract_results(raw)
                        print_human_result(q, extracted, raw)
        else:
            for q in queries:
                _, raw = run_one(q)
                all_results[q] = raw
                if not args.json:
                    extracted = extract_results(raw)
                    print_human_result(q, extracted, raw)

        if args.json:
            print(json.dumps(all_results, ensure_ascii=False, indent=2))

        if not args.json:
            # 汇总所有 citations 去重
            all_urls = set()
            for q, raw in all_results.items():
                ext = extract_results(raw)
                for ann in ext["annotations"]:
                    if ann.get("url"):
                        all_urls.add(ann["url"])
                for url in ext["citations"]:
                    all_urls.add(url)
            if all_urls:
                print(f"\n{'='*60}")
                print(f"🔗 所有去重后的来源 URL（共 {len(all_urls)} 个）:")
                print(f"{'='*60}")
                for i, url in enumerate(sorted(all_urls), 1):
                    print(f"  {i}. {url}")


if __name__ == "__main__":
    main()
