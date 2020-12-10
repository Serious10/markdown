

```python
import tkinter
import tkinter.messagebox
```


```python
def msgbox():
    tkinter.messagebox.showinfo(title="BMI输出值",message=BMI())
    
    
### 插入公式
def BMI():
    n = int(entry体重.get())
    m = int(entry身高.get())
    BMI = n/(0.01*m*0.01*m)
    BMI = str(BMI).split(".")[0] + "." + str(BMI).split(".")[1][:2]
    return BMI
    
### 设计页面
root = tkinter.Tk()
root.title("BMI计算")
root.geometry("400x400+20+20") # 这里的400x400是指窗口大小

### 按钮
button = tkinter.Button(root,text='点击弹出',command=msgbox)
button.place(x=10,y=150,height=30,width=80)

### 标签
Label1 = tkinter.Label(root,text='身高')
Label1.place(x=100,y=150,height=30,width=80)
Label2 = tkinter.Label(root,text='体重')
Label2.place(x=100,y=250,height=30,width=80)
Label3 = tkinter.Label(root,text='名字')
Label3.place(x=100,y=50,height=30,width=80)
Label4 = tkinter.Label(root,text='BMI值')
Label4.place(x=10,y=350,height=30,width=80)
Label5 = tkinter.Label(root,text='健康状况')
Label5.place(x=200,y=350,height=30,width=80)

### 文本框
身高=tkinter.StringVar(root)
entry身高 = tkinter.Entry(root,width=150,textvariable=身高)
entry身高.place(x=200,y=150,height=30,width=80)
体重=tkinter.StringVar(root)
entry体重 = tkinter.Entry(root,width=150,textvariable=体重)
entry体重.place(x=200,y=250,height=30,width=80)
名字=tkinter.StringVar(root)
entry名字 = tkinter.Entry(root,width=150,textvariable=名字)
entry名字.place(x=200,y=50,height=30,width=80)
#BMI值=tkinter.StringVar(root)
#textBMI值 = tkinter.Text(root,width=150,textvariable=BMI值)
#textBMI值.place(x=100,y=350,height=30,width=80)
#健康状况=tkinter.StringVar(root)
#text健康状况 = tkinter.Text(root,width=150,textvariable=健康状况)
#text健康状况.place(x=300,y=350,height=30,width=80)

### 输出文本
root.mainloop()
```


```python

```
