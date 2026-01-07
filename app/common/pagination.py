def clamp_page(value: int, min_value: int = 1, max_value: int = 1000) -> int:
    return max(min_value, min(value, max_value))
