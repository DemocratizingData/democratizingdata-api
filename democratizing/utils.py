def apply_limit_offset(query, limit: int | None, offset: int | None):
    result = query
    if limit:
        result = result.limit(limit)
    if offset:
        result = result.offset(offset)
    return result
