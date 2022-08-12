from democratizing.dependencies import PaginationParams


def apply_limit_offset(query, pagination: PaginationParams):
    result = query
    if pagination.limit:
        result = result.limit(pagination.limit)
    if pagination.offset:
        result = result.offset(pagination.offset)
    return result
