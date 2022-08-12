from democratizing.dependencies import PaginationParams


def apply_pagination(query, pagination: PaginationParams):
    result = query
    if pagination.limit:
        result = result.limit(pagination.limit)
    if pagination.offset:
        result = result.offset(pagination.offset)
    return result
