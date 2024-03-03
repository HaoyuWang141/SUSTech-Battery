#### Deep learning to estimate lithium-ion battery state of health without additional degradation experiments

电压充电曲线 -> SOH

+ input：充电数据(windows) , Capacity - Voltage, 1d
+ model：DNN : 1d-CNN + FC
+ output: 
+ preidiction: DNN群体一起预测, 去除离群值取平均



![image-20240228151455639](E:\SUSTech-Battery-SOH-Prediction\paper\assets\image-20240228151455639.png)

![image-20240228151512085](E:\SUSTech-Battery-SOH-Prediction\paper\assets\image-20240228151512085.png)

![image-20240228151524462](E:\SUSTech-Battery-SOH-Prediction\paper\assets\image-20240228151524462.png)

提到了高斯过程回归(GPR), 随机森林(RF), 支持向量回归(SVR), CNN

**data:**

PANASONIC NCR18650BD (3.03 Ah nominal capacity, 3 cells) :

range: 3.0 - 4.2 V, step: 10mV (0.01V), samples: 920, 926, 924



GOTION IFP20100140A (27 Ah nominal capacity, 3 cells):

range: 2.5-3.65V, step: 0.01V, samples: 1420/1422/1420



#### Semi-supervised estimation of capacity degradation for lithium ion batteries with electrochemical impedance spectroscopy

完整EIS -> capacity

input: EIS

model: CNN



#### Remaining useful life prediction for lithium-ion batteries based on an integrated health indicator
研究 **恒流充电时间, 恒压充电时间** 与 **容量, 电阻** 的关系: Beta 分布函数

 -> beta 分布函数 -> RUL

恒压充电时间: 不太好用