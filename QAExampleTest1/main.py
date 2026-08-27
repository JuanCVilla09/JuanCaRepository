def google_search(query):
    """simula una busqueda en Google y devuelve resultados ficticios"""
    if not query:
        raise ValueError("La consulta no puede estar vacía")
    results = {
        "python" : ["python.org", "tutorial python", "aprende python"],
        "java" : ["java.com", "tutorial java", "aprende java"],
        "javascript" : ["javascript.com", "tutorial javascript", "aprende javascript"]
    }
    return results.get(query.lower(), [])  #simula los resultados

    print(google_search("python"))  # Devuelve resultados ficticios para "python"