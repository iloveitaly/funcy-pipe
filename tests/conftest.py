def pytest_markdown_docs_globals():
    import funcy_pipe

    return {"fp": funcy_pipe}
