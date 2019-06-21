# assembly

> vue 组件库
## 用法
#安装
``` node
npm install smalltools-ui
```

#在main.js全局注册
``` js
import smalltools from 'smalltools-ui'
Vue.use(smalltools)
```

## 组件


## st-num

属性参数列表
--
|参数名称|类型|默认值|描述|
|:---:|:---:|:---:|:---:|
|v-model|Number|无|用于绑定的数值|
|min|Number|无|最小值，默认不做下限|
|max|Number|无|最大值，默认不做上限|
|disabled|Boolean|false|是否禁止键入数值，默认允许|


事件列表
--
|事件名称|描述|参数|
|:---:|:---:|:---:|
|change|数值改变时触发|返回当前的数值|
