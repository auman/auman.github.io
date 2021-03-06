
import os
from itertools import cycle
from PIL import Image
from meta import models

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
.cell {{margin:6px;}}
.cell p {{margin: 0px 0px 3px 0px;text-align:center;}}
.cell span {{ position:absolute;font-weight:bold;color:gold;text-decoration:none;margin: 1px 0px 0px 4px;text-shadow: black 0.1em 0.1em 0.2em; }}
</style>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery-mousewheel/3.1.12/jquery.mousewheel.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" type="text/css" media="screen" />

<script type="text/javascript">
$(document).ready(function() {{
	$("a[href$='.jpg']").attr('rel', 'gallery').fancybox({{
                'padding': 6,
                'loop': true,
                helpers		: {{
			title	: {{ type : 'inside' }},
			buttons	: {{}}
                }}
	}});
}});
</script>

<body>
<a href="https://github.com/auman"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"></a>
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

<script>
(function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
(i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
}})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-57878382-1', 'auto');
ga('send', 'pageview');
</script>

</head>
</html>

"""

COLS_COUNT = 5

SKIP = (124,)

def main():

    files = os.listdir('i')
    cols = ['',] * COLS_COUNT
    total = 0
    count_files = len(files)
    for col, f in zip(cycle(range(COLS_COUNT)),
            sorted(files, key=lambda x: int(x[:-4]))):
        total += 1
        if total in SKIP:
            continue
        im = Image.open(os.path.join('i', f))
        width, height = im.size
        if height > width:
            im.thumbnail([160, 160 / (width / height)])
        else:
            im.thumbnail([160, 160])
        thumb_path = os.path.join('thumbs', os.path.basename(f))
        im.save(thumb_path, 'JPEG', quality=80, optimize=True, progressive=True)
        if total < count_files - 1:
            label = models.get(total)
            if label:
                label = '<p>{}</p>'.format(label)
                title = 'title="{}"'.format(label)
            else:
                label = ''
                title = ''
            cols[col] += '''<div class="cell">
                            <a href="./i/{1}" target="_blank" {3}>
                                <span>{0}</span>
                                <img src="./thumbs/{1}" width="160px"/>
                                {2}
                            </a>
                        </div>'''.format(total, f, label, title)
        else:
            cols[col] += '''<div class="cell">
                            <a href="./i/{0}" target="_blank">
                                <img src="./thumbs/{0}" width="160px"/>
                            </a>
                        </div>'''.format(f)


    data = '</div><div class="col">'.join(cols)
    data = '<div class="col">{}</div>'.format(data)
    print(tpl.format(total - 2, data))

if __name__ == '__main__':
    main()

