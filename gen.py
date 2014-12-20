
import os
import ntpath
from itertools import cycle
from PIL import Image

tpl = """
<!DOCTYPE html>
<html lang="ru">
<head>
<title>Предновогодний пруфтред 2014-2015</title>
<meta charset="UTF-8">
<style>
body {{background-color:#dddddd;}}
h1 {{color:#FF6600;}}
h2 {{text-align:center;}}
</style>
</head>

<body>
<h1 style="text-align:center;">Предновогодний пруфтред 2014-2015</h1>
<h2>Всего пруфов: {}</h2>
<div style="width:900px;margin:0px auto;">
{}
</div>
</body>

</html>

"""

COLS_COUNT = 5

def main():

    files = os.listdir('i')
    cols = ['',] * COLS_COUNT
    total = 0
    for col, f in zip(cycle(range(COLS_COUNT)),
            sorted(files, key=lambda x: int(x[:-4]))):
        total += 1
        im = Image.open(os.path.join('i', f))
        im.thumbnail([160, 160])
        thumb_path = os.path.join('thumbs', ntpath.basename(f))
        im.save(thumb_path, 'JPEG', quality=80, optimize=True, progressive=True)
        cols[col] += '<a href="./i/{}" style="display:block;margin:6px;" target="_blank"><img src="./thumbs/{}" width="160px"/>'.format(f, f)

    data = '</div><div style="float:left;width:180px;">'.join(cols)
    data = '<div style="float:left;width:180px;">{}</div>'.format(data)
    print(tpl.format(total, data))

if __name__ == '__main__':
    main()

