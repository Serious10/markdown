
### 创建一个列表


```python
list = ['a','b','c',4,5,6]
```

### 末尾增加元素


```python
list.append(7)
list
```




    ['a', 'b', 'c', 4, 5, 6, 7]



### 列表指定位置添加元素


```python
list.insert(0,8)
list
```




    [8, 'a', 'b', 'c', 4, 5, 6, 7]



### 末尾增加


```python
list.append(10)
list
```




    [8, 'a', 'b', 'c', 4, 5, 6, 7, 10]



### 删除元素


```python
del list [4]
list
```




    [8, 'a', 'b', 'c', 5, 6, 7, 10]




```python
list.remove(6)
list
```




    [8, 'a', 'b', 'c', 5, 7, 10]




```python
list.pop(-1)
list
```




    [8, 'a', 'b', 'c', 5, 7]




```python
pop_ele = list.pop(2)
```


```python
pop_ele
```




    'b'



### 列表中修改元素


```python
list [1] = "hello world"
list
```




    [8, 'hello world', 'c', 5, 7]



### 查找列表元素


```python
list[4]
```




    7




```python
list[0:3]
```




    [8, 'hello world', 'c']



#### list[x：y：z] 的意思是从x到y间隔z取数字

#### 查找list中有几个函数


```python
len(list)
```




    5




```python

```
