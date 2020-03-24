# Pytholenium Documentation

## Selection types and usage

pytholenium relies on finding element by selenium selectors and attribute selectors. It starts with a Selenium selectors search, and with those WebElements output, it applies the Attribute selectors search.

Selenium selectors:
- id
- name
- xpath
- link_text
- partial_link_text
- tag_name
- class_name
- css_selector

Each one refers to the [actual Selenium selectors](https://selenium-python.readthedocs.io/locating-elements.html)
	
Attribute selectors: 
- text
- tag_name_attribute
- ... and any attribute you want to specify

***pytholenium only allows 0 or 1 Selenium selector, and any amount of Attribute selectors***


## Examples

- Using only Selenium

```html
<div id="hello_there">Hey there!</div>
```
```python
params = {"id": "hello_there"}
print (pl.get(driver, params).text)
```

- Using only Attribute
```html
<sometag>How are you?</sometag>
```
```python
params = {"tag_name_attribute": "sometag"}
print(pl.get(driver=driver, params=params).text)
```

- Using mixed selection
```html
<div name="multiple" old_city="barcelona" new_city="madrid">You might see this is a strange html</div>
<div name="multiple" old_city="barcelona" new_city="london">But don't worry</div>
<div name="multiple" old_city="barcelona" new_city="buenos aires">Everything is under control ;)</div>
```
```python
params = {"name": "multiple", "old_city": "barcelona", "new_city": "london"}
print(pl.get(driver=driver, params=params).text)
```

- Special Attribute selectors

_tag_name_attribute_ is a "special" Attribute selector, since tag_name is a Selenium's selector, but you might want to search for it as an attribute. In case of _text_ Attribute selector, it will compare the element's text

```html
<div>Oh man, you are really reading this documentation!</div>
<sometag>I'm glad :)</sometag>
```
```python
#By text
params = {"text": "Oh man, you are really reading this documentation!"}
print(pl.get(driver=driver, params=params).text)

#By tag_name_attribute
params = {"tag_name_attribute": "sometag"}
print(pl.get(driver=driver, params=params).text)
```


## Methods

Available methods are:
- get
- gets
- wait
- do
- wait_do

You can see each docstring documentation by doing

```python
from pytholenium import pytholenium as pl
help(pl)
```


## Need more examples?

Please check our [unit test](https://github.com/ArgiesDario/pytholenium/blob/master/pytholenium/unit_tests.py) and the [html file](https://github.com/ArgiesDario/pytholenium/blob/master/pytholenium/test_data/test.html). Each test is related to a html element with certain conditions, so you can see how pytholenium works.
