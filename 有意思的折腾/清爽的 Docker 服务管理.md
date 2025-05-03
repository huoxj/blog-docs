---
date: '2025-05-01'
---

## 需求

使用 Docker 部署服务是很好的习惯。只不过随着服务的变多，使用时很难回忆起服务跑在哪个端口上。并且，现在服务大都由 docker run 部署，这样是比较脆弱的，应该用 docker-compose 管理这些服务。总之，目前的高优先级需求为：

- 能够方便地访问到服务，而不是记端口
- 将现有服务迁移为 docker-compose 管理

其他要求：

- 只考虑局域网环境
- 保证系统迁移、重建的易用性（比如使用 git 管理 docker-compose 以及一些常用服务的配置）
- 尽量仍然使用命令行工具进行管理，不要引入额外实体

## 访问服务

访问服务有很多简单的临时解决方法。比如：
- 常用服务收藏到浏览器书签
- 将服务分类，同类服务绑定到同一个端口段中

不过我还是提出一个更加繁琐但是更易用的解决方法。实现的效果是通过域名访问 NAS 服务，比如 `jellyfin.nas.com` 访问 jellyfin。但是这并不需要你真正买一个域名，因为本文是局域网内使用的情景。所以我下面称之为“假域名”。

具体而言：
- 使用配置文件配置假域名和端口的对应关系。For example, 使用 .env 管理:
```
JELLYFIN_DOMAIN=jellyfin.nas.com
JELLYFIN_PORT=9000

MYSQL_DOMAIN=mysql.nas.com
MYSQL_PORT=3306
...
```
- Docker-compose 配置 port 的字段直接从 .env 获取
- Nginx 从 .env 自动配置反向代理
- 在局域网路由器处手动配置 DNS 解析规则，将 nas.com 解析到 nas 的内网地址（一次性）

> 未实践

> 似乎 traefik + portainer 可以满足上述需求了，待研究

## Docker-compose 迁移



## Docker-compose 管理