import base64
from pathlib import Path

image_path = Path(r"./pomodoro/tomato.png")
image_bytes = image_path.read_bytes()

b64_string = base64.b64encode(image_bytes)
print(b64_string)

