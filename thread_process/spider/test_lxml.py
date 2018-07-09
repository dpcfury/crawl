# -*- coding:utf-8 -*-
import lxml.html as LH
broken_html = '<ul class=country><li>Area<li>Population</ul>'
print dir(LH)
tree = LH.fromstring(broken_html)  # parser the HTML
print type(tree)
fixed_html = LH.tostring(tree, pretty_print=True)
print fixed_html
