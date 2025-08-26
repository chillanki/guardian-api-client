from __future__ import annotations

import requests
from typing import Any, Dict, Optional


class GuardianClient:
    """A lightweight client for The Guardian Content API."""

    def __init__(self, api_key: str, base_url: str = "https://content.guardianapis.com") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Internal helper to perform GET requests with API key included."""
        if params is None:
            params = {}
        params["api-key"] = self.api_key
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def search_articles(
        self,
        query: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        order_by: str = "newest",
        show_fields: str = "all",
        page_size: int = 30,
        lang: str = "en",
        production_office: Optional[str] = None,
        section: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Search Guardian articles with advanced filters.

        Args:
            query: Keyword to search.
            from_date: Start date (YYYY-MM-DD).
            to_date: End date (YYYY-MM-DD).
            order_by: 'newest' or 'oldest'.
            show_fields: Fields to include ('all' for everything).
            page_size: Number of results per page.
            lang: Language filter.
            production_office: Optional production office filter.
            section: Optional section filter (multiple separated by |).

        Returns:
            JSON dictionary of search results.
        """
        params: Dict[str, Any] = {
            "q": query,
            "from-date": from_date,
            "to-date": to_date,
            "order-by": order_by,
            "show-fields": show_fields,
            "page-size": page_size,
            "lang": lang,
        }
        if production_office:
            params["productionOffice"] = production_office
        if section:
            params["section"] = section

        return self._get("search", params)

    def list_sections(self) -> Dict[str, Any]:
        """Retrieve all available sections from The Guardian."""
        return self._get("sections")

    def list_tags(self, query: Optional[str] = None) -> Dict[str, Any]:
        """Retrieve available tags, optionally filtered by a keyword."""
        params: Dict[str, Any] = {}
        if query:
            params["q"] = query
        return self._get("tags", params)

    def get_article(
        self,
        article_id: str,
        show_fields: str = "all",
        lang: str = "en",
        production_office: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Fetch a single article with advanced options.

        Args:
            article_id: Unique article path (from API).
            show_fields: Fields to include ('all' for everything).
            lang: Language filter.
            production_office: Optional production office filter.

        Returns:
            JSON dictionary containing article details.
        """
        params: Dict[str, Any] = {
            "show-fields": show_fields,
            "lang": lang,
        }
        if production_office:
            params["productionOffice"] = production_office

        return self._get(article_id, params)
