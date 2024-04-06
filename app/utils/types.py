from typing import TypedDict , List , Any

# When used in endpoints to return data, specifying this (-> "PaginationDict") indicates that the exact structure of the returned data is not defined
class PaginationDict(TypedDict):
    page: int
    limit: int
    total: int
    results: List[Any]