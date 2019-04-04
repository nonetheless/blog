web应用问题解决
==============

1.数据库修改的并发问题
------------------
### 描述
因为当两个或更多进程同时访问数据库时，这可能不起作用。假如存在验证通过的进程A和B都尝试修改用户名为同一个，但稍后进程A尝试重命名时，数据库已被进程B更改，无法重命名为该用户名，会再次引发数据库异常。 除了有很多服务器进程并且非常繁忙的应用之外，这种情况是不太可能的，所以现在我不会为此担心。

### 解决
TODO