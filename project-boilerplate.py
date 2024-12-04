import os
import sys

def create_boilerplate(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    html_path = os.path.join(folder_name, "index.html")
    css_path = os.path.join(folder_name, "styles.css")
    js_path = os.path.join(folder_name, "script.js")
    with open(html_path, "w") as html_file:
        html_file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Hello, World!</h1>
    <script src="script.js"></script>
</body>
</html>
""")
    with open(css_path, "w") as css_file:
        css_file.write("""body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
    text-align: center;
    margin-top: 20px;
}
""")
    with open(js_path, "w") as js_file:
        js_file.write("""document.addEventListener('DOMContentLoaded', function() {
    console.log('Hello, World!');
});
""")

    print(f"Project boilerplate created in '{folder_name}'!")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 project-boilerplate.py <folder_name>")
        sys.exit(1)    
    folder_name = sys.argv[1]
    create_boilerplate(folder_name)
