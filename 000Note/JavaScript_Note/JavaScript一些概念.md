## 2022/5/6

#### 1.闭包：

产生闭包的条件：

1.在函数内部也有一个函数。

2.在函数内部的函数里面用到了外部函数的局部变量。

3.外部函数把内部函数作为返回值return出去了。

闭包特点：

1.使用闭包可以保存局部变量不随原函数销毁，这个局部变量可做全局变量用。用闭包可以减少很多不必要的全局变量。

#### 2.自执行函数

```javascript
(function(){
    console.log("这是一个自执行函数，定义之后就立刻执行了，不需要调用。");
}
)();
// 配合闭包使用
var inner = (function(){
    var a = 1;
    return function(in_arg){
        a = a + in_arg;
        console.log(a);
    }
}
)();

inner(1);
inner(2);
inner(3);
inner(4);
inner(5);
```

