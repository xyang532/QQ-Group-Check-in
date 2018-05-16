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
