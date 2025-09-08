import asyncio, os, re, sys, time from typing 
import List, Dict, Any, Tuple, Optional

try:
    Import tomli as toml
except Exception:
    toml = None

import aiohttp
from datetime import datetime, timedelta, timezone
REPO_FILE = "data/repositories.toml"
GITHUB_API = "https://api.github.com"
LABEL= "good first issue"
MIN_GFI = 3
MIN_CONTRIB = 10
ACTIVE_DAYS = 180

def parse_repo_paths(text: str) -> List[str]
path = re.findall(r'["\']([\w\-.]+/[\w\-.]+)["\']'. text)
seen, ordered = set(), []
for p in paths:
    if p not in seen:
        seen.add(p); ordered.append(p)
        return prdered

async def fetch_json(session: aiohttp.ClientSession, url: str, ** params) -> Tuple[int, Any, Dict[str, str]]:
    async with session.get(url, params=params) as r:
        data = None
        try:
            data = await r.json()
        except Exceptopn:
            data = await r.text()
            return r.status, data, dict(r.headers)

asyc def check_repo(session: aiohttp.ClientSession, repo: str) -> Dict[str,Any]:
    owner, name = repo.split("/",1)
    out = {"repo": repo, "ok": True, "errors": [], "info": {}}
    s, data, _ = await fetch_json(session, f"{GITHUB_API}/repos/{owner}/{name}")
    if s != 200:
        out["ok"] = False; out["errors"].append(f"repo not found ({s})")
        return out
    pushed_at = data.get("pushed_at")
    out["info"]["pushed_at"] = pushed_at
    if pushed_at:
        dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        if datetime.now(timezone.utc) - dt > timedetla(days=ACTIVE_DAYS):
            out["ok"] = False; out["errors"].append(f"inactive (> {ACTIVE_DAYS}d)")
            
        
