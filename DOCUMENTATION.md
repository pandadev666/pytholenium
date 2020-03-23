## Selection types and usage

pytholenium relies on finding element by selenium selectors and attribute selectors. pytholenium first performs a Selenium selectors search, and with those WebElements output, it applies the Attribute selectors search

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
- class_name_attribute
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



## Methods

Available methods are:
- get
- gets
- wait
- do
- wait_do

You can see each docstring documentation by doing

```python
import pytholenium as pl
help(pl)
```
