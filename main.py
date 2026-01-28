#from exa_py import Exa

#query = input("Search here: ")

# response = exa.search(
#     query,
#     num_results=5,
#     type="auto",
#     include_domains=["https://www.youtube.com"],
# )

# for result in response.results:
#     print(f"Title: {result.title}")
#     print(f"URL: {result.url}")
#     print()

import os
from exa_py import Exa

def get_domain():
    print("Choose platform to search:")
    print("1. Substack")
    print("2. LinkedIn")
    print("3. X (Twitter)")

    choice = input("Enter 1 / 2 / 3: ").strip()

    if choice == "1":
        return ["https://substack.com"]
    elif choice == "2":
        return ["https://www.linkedin.com"]
    elif choice == "3":
        return ["https://x.com"]
    else:
        print("Invalid choice.")
        exit()

def main():
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        print("Error: EXA_API_KEY not set.")
        return

    exa = Exa(api_key)

    query = input("Search here: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return

    domains = get_domain()

    try:
        response = exa.search(
            query,
            num_results=5,
            type="auto",
            include_domains=domains,
        )
    except Exception as e:
        print("Search failed:", e)
        return

    print("\nSearch Results:\n")
    for result in response.results:
        print(f"Title: {result.title}")
        print(f"URL: {result.url}\n")

if __name__ == "__main__":
    main()

