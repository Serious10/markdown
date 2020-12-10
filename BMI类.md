

```python
### 定义BMI类
class BMI:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def get_name(self):
        return self.name
    
    
    def BMI(self):
        n = self.weight
        m=self.height
        self.BMI = n/(m*m)
        return (self.BMI)
        
    def condition(self):
        n = self.weight
        m=self.height
        BMI = n/(m*m)
        if self.BMI < 18.5:
            return ("偏瘦")
        elif self.BMI>18.5 and self.BMI<24:
            return ("正常")
        elif self.BMI >24 and self.BMI<30:
            return ("偏胖")
        else :
            return ("超重")
        
```


```python
# 实例化
zhangsan = BMI("zhangsan",15,1.7,50)
lisi = BMI("lisi",18,1.8,80)
wangwu = BMI("wangwu",20,1.85,70)
zhaoliu = BMI("zhaoliu",18,1.9,80)
caiqi = BMI("caiqi",21,1.75,85)
```


```python
# 调用方法
zhangsan.BMI()
```




    17.301038062283737




```python
zhangsan.condition()
```




    '偏瘦'




```python
print("{}的BMI是：{}，身体状况是：{}".format(zhangsan.name,zhangsan.BMI,zhangsan.condition()))
```

    zhangsan的BMI是：17.301038062283737，身体状况是：偏瘦
    


```python

```
