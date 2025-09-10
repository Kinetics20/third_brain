from pydantic import BaseModel, Field, ConfigDict


class ChatIn(BaseModel):
    """Schema for inbound ChatGPT requests via FastAPI.

    Attributes:
        message (str): The user's message or prompt for the LLM.
        system_prompt (Optional[str]): Optional system-level instruction
            that sets assistant behavior. Defaults to a neutral helper.
        temperature (float): Sampling temperature controlling randomness.
            0 → deterministic, higher values → more diverse outputs.
        model (str): Target OpenAI chat model.
        stream (bool): Whether to return results as a stream (SSE) or
            as a single response.
    """
    model_config = ConfigDict(
        extra='forbid',
        frozen=True
    )

    message: str = Field(..., description="User message", examples=["Tell me a joke about data engineers."])
    system_prompt: str | None = Field(
        default="You are a helpful assistant.",
        description="Optional system prompt",
        examples=["You are an expert Python tutor."],
    )
    temperature: float = Field(
        default=0.2,
        ge=0,
        le=2.0,
        description="Sampling temperature (0=deterministic, 2.0=max diversity)",
        examples=[0.0, 0.7, 1.2],
    )
    model: str = Field(
        default="gpt-4o-mini", description="OpenAI chat model name", examples=["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]
    )
    stream: bool = Field(default=False, description="Enable token streaming", examples=[False, True])