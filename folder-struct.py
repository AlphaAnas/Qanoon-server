import os

def create_folder_structure(base_path="."):
    structure = {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "dependencies.py": "",
            "routers": {
                "__init__.py": "",
                "items.py": "",
                "users.py": ""
            },
            "crud": {
                "__init__.py": "",
                "item.py": "",
                "user.py": ""
            },
            "schemas": {
                "__init__.py": "",
                "item.py": "",
                "user.py": ""
            },
            "models": {
                "__init__.py": "",
                "item.py": "",
                "user.py": ""
            },
            "external_services": {
                "__init__.py": "",
                "email.py": "",
                "notification.py": ""
            },
            "utils": {
                "__init__.py": "",
                "authentication.py": "",
                "validation.py": ""
            }
        },
        "tests": {
            "__init__.py": "",
            "test_main.py": "",
            "test_items.py": "",
            "test_users.py": ""
        },
        "requirements.txt": "",
        ".gitignore": "",
        "README.md": ""
    }
    
    def create_items(base, items):
        for name, content in items.items():
            path = os.path.join(base, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_items(path, content)
            else:
                with open(path, "w") as f:
                    f.write(content)
    
    create_items(base_path, structure)
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()
