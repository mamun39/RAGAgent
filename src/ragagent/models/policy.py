"""Policy and authorization context models."""

import pydantic


class RetrievalPolicyContext(pydantic.BaseModel):
    """App-layer policy inputs for retrieval filtering."""

    tenant_id: str = "demo"
    user_role: str = "user"
    allowed_classifications: list[str] = pydantic.Field(default_factory=lambda: ["internal"])
    allow_low_trust: bool = False
