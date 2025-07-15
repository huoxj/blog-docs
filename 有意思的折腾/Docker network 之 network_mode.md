---
date: 2025-07-15
---
通过多个 docker network，容器之间可以通过容器名进行网络访问。这一点不必多说。Network_mode 的 container 模式提供了直接接入容器网络的方式，而无需专门创建网络。

通常使用 docker network 时，都会先使用 docker network create 创建一个网络，然后让需要通信的容器加入这个网络。Docker compose 类似：

```yaml
services:
	service1:
		networks:
			- test_network
	service2:
		networks:
			- test_network
networks:
	test_network:
		name: test_network
	external_test_network:  # Or reuse an external network
		external: true
		name: test_network
```

除此之外，还可以通过 network_mode 连接多个容器。任何容器在创建时会创建一个独立的网络，其他容器可以通过**直接接入**这个网络来实现通信。比如，让服务 2 接入服务 1 的网络：

```yaml
services:
	service1:
		...
	service2:
		network_mode: service:service1
```

值得注意的是 network_mode 的语法。冒号后显然是容器名，冒号前的 service 是 docker compose 的一个语法糖，会自动解析同一 yaml 配置中其他的容器。

所以如果服务需要接入当前配置中不存在的服务，比如目标服务之前已经起起来了，那么就需要使用 container：

```yaml
# service1.yaml
services:
	service1:
		...
# service2.yaml
services:
	service2:
		network_mode: container:service1
```

> network_mode 对应的是 docker CLI 的 `--net=container:service1`。

