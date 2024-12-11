def pytest_configure(config):
    config.addinivalue_line("markers", "current: As current ones")
    config.addinivalue_line("markers", "learning: As learning exercises")
    config.addinivalue_line("markers", "get_api: As using the Notion API to get data")
    config.addinivalue_line("markers", "post_api: As using the Notion API to post data")
    config.addinivalue_line("markers", "slow: As slow ones")
