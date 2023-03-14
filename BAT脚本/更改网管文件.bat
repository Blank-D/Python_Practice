%关闭回显，设置延迟环境变量扩展%
@echo off & setlocal EnableDelayedExpansion

rem 计算调用的参数个数
for %%a in (%*) do set /a num+=1
if defined num (echo 调用了 %num% 个参数) else echo 没有调用任何参数

set fileName=%1
set oldText=%2
set newText=%3

echo %fileName%,%oldText%,%newText%,%num%

rem 参数个数小于3个提示用户
if %num% lss 3 (
	goto :errArgsTip
)

if %num% geq 4 (
	set featureText=%4
)

echo fileName=%fileName% oldText=%oldText% newText=%newText%

if defined featureText (echo featureText=%featureText%)

for /f "delims=" %%a in ('findstr /n .* %fileName%') do (
	set "str=%%a"
	rem 替换内容
	if defined featureText (
		rem 查找每行字符串是否包含指定的特征字符，只对包含特征字符的行替换文本
		echo !str!| findstr %featureText% >nul && (
			set "str=!str:%oldText%=%newText%!"
		)
	) else (
		set "str=!str:%oldText%=%newText%!"
	)
	rem 将添加了行号的文本写入临时文件
	echo !str! >>tmp.txt
)
for /f "tokens=1* delims=:" %%i in ('type tmp.txt') do (
	rem 按:分割每行字符串
	set "str=%%j"
	if "!str!"==" " (
		rem 写入源文件里的空行
		call echo.>>new_A.txt
	) else (
		rem 将字符串写入文本，每行会多一个空格，使用字符串的截取功能去掉末尾的一个空格
		echo !str:~0,-1!>>new_A.txt
	)
)



REM 删除临时文件并修改后的文件为源文件
del tmp.txt&move new_A.txt %fileName%

goto :end

:errArgsTip
	echo ----------------------
	echo 请输入正确的参数 fileName oldText newText [featureText]
	echo -- fileName
	echo -- oldText
	echo -- newText
	echo -- featureText
	echo ----------------------
	
:end
	rem 执行完脚本要将num变量取消，以免影响下次执行
	set num=