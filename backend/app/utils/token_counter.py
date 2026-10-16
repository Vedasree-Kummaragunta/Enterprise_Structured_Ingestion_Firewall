
def estimate_tokens(text: str) -> int:
    """Estimate tokens with tiktoken when available; otherwise use a rough fallback."""
    try:
        import tiktoken

        encoding = tiktoken.get_encoding("cl100k_base")
        return len(encoding.encode(text))

    except Exception:
        # Rough estimate only; not suitable for billing.
        return max(1, len(text.split()) * 2) if text.strip() else 0
