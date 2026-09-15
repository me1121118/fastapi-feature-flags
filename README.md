# fastapi-feature-flags

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-feature-flags/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Lightweight feature flags dependency and route guard for FastAPI applications.

---

## 🚀 Features

- 🚩 **Route Guard**: Block or enable routes using `@require_feature("feature_name")`.
- ⚙️ **Configurable Providers**: Built-in memory store, environment variable provider, and request header overrides.
- 🚫 **HTTP 404/403 Fallback**: Returns configurable status code when a gated route is requested while disabled.

---

## 📦 Installation

```bash
pip install fastapi-feature-flags
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI, Depends
from fastapi_feature_flags import FeatureFlags, require_feature

app = FastAPI()
flags = FeatureFlags(defaults={"beta_export": True, "v2_dashboard": False})

@app.get("/export", dependencies=[Depends(require_feature("beta_export", flags))])
def export_data():
    return {"status": "export ready"}

@app.get("/dashboard", dependencies=[Depends(require_feature("v2_dashboard", flags))])
def v2_dashboard():
    return {"status": "v2 active"}
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library helped manage your progressive rollouts, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [ko-fi.com/me1121118](https://ko-fi.com/)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
