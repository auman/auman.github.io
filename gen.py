
import os
from itertools import cycle
from PIL import Image

tpl = """
<!DOCTYPE html>
<html lang="ru">
<head>
<title>Предновогодний пруфтред 2014-2015</title>
<meta charset="UTF-8">
<style>
body {{background-color:#eee;}}
h1 {{color:#FF6600;}}
h2 {{text-align:center;}}
.col {{float:left;width:172px;background-color:#dddddd;}}
</style>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.12/jquery.mousewheel.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" type="text/css" media="screen" />

<script type="text/javascript">
$(document).ready(function() {{
	$("a[href$='.jpg']").attr('rel', 'gallery').fancybox({{
                'padding': 6,
                'loop': true
	}});
}});
</script>

<script>
(function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
(i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
}})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-57878382-1', 'auto');
ga('send', 'pageview');
</script>
</head>

<body>
<h1 style="text-align:center;">Предновогодний пруфтред 2014-2015</h1>
<h2>Всего пруфов: {}</h2>
<div style="width:900px;margin:0px auto;">
{}
</div>
 <div id="disqus_thread"></div>
    <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
        var disqus_shortname = 'aumangithubio'; // required: replace example with your forum shortname

        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function() {{
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        }})();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
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
        thumb_path = os.path.join('thumbs', os.path.basename(f))
        im.save(thumb_path, 'JPEG', quality=80, optimize=True, progressive=True)
        cols[col] += '<a href="./i/{}" style="display:block;margin:6px;" target="_blank"><img src="./thumbs/{}" width="160px"/>'.format(f, f)

    data = '</div><div class="col">'.join(cols)
    data = '<div class="col">{}</div>'.format(data)
    print(tpl.format(total, data))

if __name__ == '__main__':
    main()

