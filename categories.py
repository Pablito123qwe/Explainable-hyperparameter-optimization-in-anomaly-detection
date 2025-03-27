import os

def get_categories(path):
    return [name for name in os.listdir(path)
                  if os.path.isdir(os.path.join(path, name)) and not name.startswith('.')]