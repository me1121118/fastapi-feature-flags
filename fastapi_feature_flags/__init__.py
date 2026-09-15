import os
from typing import Dict, Optional, Callable
from fastapi import HTTPException, status, Request

class FeatureFlags:
    """Manages active feature toggles with memory and environment variable support."""

    def __init__(self, defaults: Optional[Dict[str, bool]] = None, env_prefix: str = "FEATURE_"):
        self.flags: Dict[str, bool] = dict(defaults or {})
        self.env_prefix = env_prefix

    def is_enabled(self, name: str, request: Optional[Request] = None) -> bool:
        # Check environment variable first
        env_key = f"{self.env_prefix}{name.upper()}"
        if env_key in os.environ:
            return os.environ[env_key].lower() in ("1", "true", "yes", "on")

        return self.flags.get(name, False)

    def set(self, name: str, enabled: bool) -> None:
        self.flags[name] = enabled

def require_feature(
    feature_name: str,
    flags_manager: FeatureFlags,
    status_code: int = status.HTTP_404_NOT_FOUND,
    detail: str = "Feature not enabled"
) -> Callable:
    """FastAPI dependency to guard endpoints behind feature flags."""
    def dependency(request: Request):
        if not flags_manager.is_enabled(feature_name, request):
            raise HTTPException(status_code=status_code, detail=detail)
        return True
    return dependency
