
import os

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
    for f in files:
        data += '<div style="float: left;margin: 6px;"><a href="./i/{}" target="_blank"><img src="./i/{}" width="200px"></div>'.format(f, f)

    print(tpl.format(data))

if __name__ == '__main__':
    main()

