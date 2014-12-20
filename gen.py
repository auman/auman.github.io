
import os
import ntpath
from PIL import Image

tpl = """
<!DOCTYPE html>
<html>
<head>
<title>Предновогодний пруфтред 2014-2015</title>
</head>

<body>
<h1 style="text-align:center;">Предновогодний пруфтред 2014-2015</h1>
<div style="width:900px;margin:0px auto;">
{}
</div>
</body>

</html>

"""

def main():

    files = os.listdir('i')
    data = ''
    for f in sorted(files, key=lambda x: int(x[:-4])):
        im = Image.open(os.path.join('i', f))
        im.thumbnail([160, 160])
        thumb_path = os.path.join('thumbs', ntpath.basename(f))
        im.save(thumb_path, 'JPEG', quality=80, optimize=True, progressive=True)
        data += '<div style="float: left;margin: 6px;"><a href="./i/{}" target="_blank"><img src="./thumbs/{}" width="160px"></div>'.format(f, f)

    print(tpl.format(data))

if __name__ == '__main__':
    main()

