## Part 1: SAXPY

使用 CUDA 实现 SAXPY。

实现很简单，跟着实验文档和 CUDA 文档做下来就行。

Question 2：为什么观测到的带宽约为 5.3 GB/s，远不及 PCIe 3.0 的理论带宽上限？
- 主板芯片组性能限制
- **Pinned memory** 机制
	- GPU 通过 DMA 访存
	- Pinned memory 是物理内存上一块固定的区域，不会被换出，能通过 DMA 加速通信
	- CPU 内存(host data)上的数据是虚拟内存上的可分页数据，可能存在于物理内存上或者硬盘上（页被换出物理内存了）
	- GPU 直接通过物理地址访存，host data 需要先拷贝到临时的 pinned memory 区上，再拷贝到 GPU (device memory)
	- 用 `cudaHostAlloc` 或 `cudaMallocHost` 分配 pinned memory
	- [CUDA:页锁定内存(pinned memory)和按页分配内存(pageable memory ) - 牛犁heart - 博客园](https://www.cnblogs.com/whiteBear/p/17842246.html)
