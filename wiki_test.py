import wikipedia

try:
    term = "WWII"  # Ensure this is not empty or None
    results = wikipedia.search(term)
    print(results)
except Exception as e:
    print(f"An error occurred: {e}")
