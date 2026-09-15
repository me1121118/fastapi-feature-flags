import pytest
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from fastapi_feature_flags import FeatureFlags, require_feature

def test_feature_flags_guard():
    app = FastAPI()
    flags = FeatureFlags(defaults={"new_ai": False, "legacy_auth": True})

    @app.get("/ai", dependencies=[Depends(require_feature("new_ai", flags))])
    def ai_endpoint():
        return {"ai": "ready"}

    @app.get("/legacy", dependencies=[Depends(require_feature("legacy_auth", flags))])
    def legacy_endpoint():
        return {"auth": "ok"}

    client = TestClient(app)

    # Disabled feature returns 404
    res_ai = client.get("/ai")
    assert res_ai.status_code == 404

    # Enabled feature returns 200
    res_legacy = client.get("/legacy")
    assert res_legacy.status_code == 200

    # Dynamically enable
    flags.set("new_ai", True)
    assert client.get("/ai").status_code == 200
