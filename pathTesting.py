import os.path
from pathlib import Path

print(Path.cwd())
# prints C:\Users\cheyv\Desktop\Laptop Python\venv\Scripts (location)

# is_absolute will give boolean value
print(Path.cwd().is_absolute())

# commands for address specifics example:
# for file C:\Users\cheyv\Desktop\Resume Grad Final.docx
p = Path('C:/Users/cheyv/Desktop/Resume Grad Final.docx')
print(p.anchor)
print(p.parent)
print(p.stem)
print(p.name)
print(p.suffix)

#parents[] attribute evaluates to the ancestor folder w/ an integer index:
print(p.parents[3])
print(p.parents[2])
print(p.parents[1])
print(p.parents[0])

# getsize(path) will give the size of a particular file in bytes
print(os.path.getsize('C:/Users/cheyv/Desktop/Resume Grad Final.docx'))
