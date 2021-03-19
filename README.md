# 109021058_YenHsunKuo_20210319

## <font color = "FF8000"><b>操作流程</font>
1. 點選左下齒輪
2. 點選Command Palette...
3. 上方輸入sftp(需先載該套件)
4. <img src = "imgs/161666274_1894602764049589_9218215833832650248_n.jpg" style = "border: 5px solid #484891">
5. 開html檔 儲存後輸入密碼
6. http://210.70.80.21/~bs109021058 (帳號)
<br>
<font color = "red">PS.如非用學校網路需用VPN(學校主頁網站右側網路資源中下載)</font>
<br>
使用VPN速度會較慢 可在jason內新增設定 <font color = "yellow">"connectTimeout": 30000,</font>(單位為毫秒 1000毫秒 = 1秒)
<br>
<font color = "green">VPN資源:</font> https://ic.asia.edu.tw/files/13-1057-80657.php?Lang=zh-tw
<br>
7. 終端機(檢查是否有檔案):
- ssh bs109021058@210.70.80.21
- (密碼)
- ll
- cd public_html
- ll
<br>
<br>
<br>

## <font color = "FF8000"><b>HTML語法</font>
- 置中: style = "text-align: center;"
- 選色: style = "background-color: rgb(253, 255, 218)"
- 漸層選色: style = "background-image:liner-gradient"
- 換色: <span style = "color:></span>
- 表格外框: <style = "border: 5px solid #0000ff;">
- 表格寫法:
<br>tr(橫行)
<br>th(直列)
<br>/th
<br>/tr
- ccs設定全套用:
<br>
table{
<br>    border: 1px solid #0000ff;
<br>    border_collapse: collapse;
<br>    width: 600px;
<br>    text-align: center;
<br>    margin: 2em auto 1em auto ;(上右下左)    
}



