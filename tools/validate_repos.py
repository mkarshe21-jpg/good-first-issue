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
