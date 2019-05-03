# QQ-Group-Check-in
QQ群签到

依赖库
requests, PyExecJS

自行运行
<code>pip install requests PyExecJS</code>
安装依赖库

配合crontab有奇效

1.<code>crontab -e</code>

2.<code>0 0 * * * python /项目位置/QQ-Group-Check-in/qq.py</code>设置凌晨签到

# 本项目只支持python3

---
近日有[**运行获取不到skey**](https://github.com/evilinsipid/QQ-Group-Check-in/issues/5)的问题发生

不过呢感谢 @muzhiyun 的帮助，问题得到了解决，问题定位在**腾讯异地登陆保护**

所以发生这种情况时，也就爱莫能助了(无奈
