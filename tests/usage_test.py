from datetime import date
from guardian_client import GuardianClient

# Initialize client
api_key = "bd636a5e-6518-4e03-a4d9-16661af68960"
client = GuardianClient(api_key=api_key)

dt = date.today().isoformat()

# ---------------------------
# 1. Advanced search (multiple filters)
# ---------------------------
search_results = client.search_articles(
    from_date=dt,
    to_date=dt,
    order_by="newest",
    show_fields="all",
    page_size=5,
    lang="en",
    production_office="US",
    section="commentisfree|world|culture|business|politics|society"
)
print("=== Advanced Search Results ===")
print(search_results)

# ---------------------------
# 2. Get a single article (latest from search)
# ---------------------------
first_article = search_results.get("response", {}).get("results", [])[0]
article_id = first_article.get("id") if first_article else None

if article_id:
    article = client.get_article(
        article_id=article_id,
        show_fields="all",
        lang="en",
        production_office="US"
    )
    print("\n=== Single Article ===")
    print(article)
else:
    print("No articles found today.")

# ---------------------------
# 3. List all sections
# ---------------------------
sections = client.list_sections()
print("\n=== Sections ===")
for section in sections.get("response", {}).get("results", []):
    print(f"- {section.get('id')} : {section.get('webTitle')}")

# ---------------------------
# 4. List tags (example: politics)
# ---------------------------
tags = client.list_tags(query="politics")
print("\n=== Tags related to 'politics' ===")
for tag in tags.get("response", {}).get("results", []):
    print(f"- {tag.get('id')} : {tag.get('webTitle')}")
