from guardian_client.client import GuardianClient


def test_search_articles() -> None:
    client = GuardianClient(api_key="bd636a5e-6518-4e03-a4d9-16661af68960")
    assert client.api_key == "bd636a5e-6518-4e03-a4d9-16661af68960"


def test_base_url_trimming() -> None:
    client = GuardianClient(api_key="bd636a5e-6518-4e03-a4d9-16661af68960", base_url="https://content.guardianapis.com/")
    assert client.base_url.endswith("guardianapis.com")


def test_list_sections_method_exists() -> None:
    client = GuardianClient(api_key="bd636a5e-6518-4e03-a4d9-16661af68960")
    assert callable(client.list_sections)


def test_get_article_method_exists() -> None:
    client = GuardianClient(api_key="bd636a5e-6518-4e03-a4d9-16661af68960")
    assert callable(client.get_article)
