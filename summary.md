# 总结

### 使用Depends让程序更简洁，效率更高

> 数据库db的获取在每个请求中用Depends函数获取的时候，整个请求中使用的Session是同一个，只用一次生成和关闭。如果将db的获取放在单独的文件中如service中，则每调用一次service.get_xx_by_id()就会创建一次数据库链接并关闭它