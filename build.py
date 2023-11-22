#!/bin/python

import pathlib
import random
import shutil

TEMPLATE = """\
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amigo Secreto 2023</title>
    <style>
body {{
	display: flex;
	align-items: center;
	justify-content: center;
	height: 100vh;
	font-size: 4em;
	font-family: sans-serif;
}}
    </style>
  </head>
  <body style="display: flex; align-items: center; justify-content: center;">
    <p>
      Olá, {name}!
      <br/>
      Seu amigo secreto é {friend}!
    </p>
  </body>
</html>
"""

NAMES = [
    "Gustavo",
    "Natália",
    "Sofia",
    "Jonas",
    "Rafaela",
    "João",
    "Vera",
    "Anna",
    "Márcio",
    "Lene",
    "Mauro",
    "Camila",
]

FORBIDDEN_PAIRS = (
    ("Natália", "Sofia"),
)

FORBIDDEN_PAIRS = set(tuple(sorted(p)) for p in FORBIDDEN_PAIRS)

build_dir = pathlib.Path(__file__).parent / "build"

try:
    shutil.rmtree(build_dir)
except FileNotFoundError:
    pass

build_dir.mkdir()

indices = list(range(len(NAMES)))
while True:
    random.shuffle(indices)
    for i, j in enumerate(indices):
        if i == j:
            break

        a, b = tuple(sorted((NAMES[i], NAMES[j])))
        if (a, b) in FORBIDDEN_PAIRS:
            break
    else:
        break

for i, j in enumerate(indices):
    a, b = NAMES[i], NAMES[j]
    key = "".join(chr(random.randrange(ord('a'), ord('z') + 1)) for _ in range(6))
    (build_dir / f"{key}.html").write_text(TEMPLATE.format(name=a, friend=b))
    print(a, f"https://guludo.github.io/amigo-secreto-2023/build/{key}.html")
