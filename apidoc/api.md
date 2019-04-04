# Graphql

一种用于 API 的查询语言,是一个使用基于类型系统来执行查询的服务端运行时（类型系统由你的数据定义）。GraphQL 并没有和任何特定数据库或者存储引擎绑定，而是依靠你现有的代码和数据支撑。

## Graphql VS Restful

https://restfulapi.net/


![Graphql vs Restful](https://img.draveness.me/2018-07-16-graphql-vs-restful-endpoint.png)

-
-
-
-


GraphQL 以图的形式将整个 Web 服务中的资源展示出来，其实我们可以理解为它将整个 Web 服务以 “SQL” 的方式展示给前端和客户端，服务端的资源最终都被聚合到一张完整的图上，这样客户端可以按照其需求自行调用，类似添加字段的需求其实就不再需要后端多次修改了。
![Graphql](https://img.draveness.me/2018-07-16-yelp-schema.png "Optional title")

## how to Graphql
http://graphql.cn/learn/

### query and modify
![Graphql](https://img.draveness.me/2018-07-16-graph-query-language.png "Optional title")


### schema and type
![Graphql](https://img.draveness.me/2018-07-16-graphql-schema.png "Optional title") 

## github api
https://api.github.com/graphql

```graphql
query {
  viewer {
    login
    name
  }
}
```

```graphql
query($number_of_repos:Int!){
  viewer {
    nonetheless: name
     repositories(last: $number_of_repos) {
       nodes {
         name
       }
     }
   }
}

{
   "number_of_repos": 3
}
```

```graphql
query($login:String!){
  user(login:$login){
    watching(first:1){
      nodes{
        id
        viewerHasStarred
      }
    }
  } 
}

{
  "login": "nonetheless"
}
```

```graphql
mutation($input:AddStarInput!){
 addStar(input:$input){
  clientMutationId
}
}

{
  "input": {
    "clientMutationId":"gdafdsafe",
    "starrableId":"MDEwOlJlcG9zaXRvcnkyODgxNzg5="
  }
}
```

## build Graphql Server

https://github.com/chentsulin/awesome-graphql#lib-py