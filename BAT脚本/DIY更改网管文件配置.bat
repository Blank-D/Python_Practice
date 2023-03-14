@echo off & setlocal EnableDelayedExpansion

rem for %%a in (%*) do set /a num+=1

rem 更改路径下的文件配置D:\unm2000\server\etc\platform-options.ini
cd D:/unm2000/server/etc
set filename=platform-options.ini


rem 遍历filename里面的所有行进行筛选
for /f "delims=" %%i in ('findstr /n .* %filename%')  do (
	set str=%%i
	rem 取出每行第三个字符至最后一个字符
	set temp_str=!str:~3,-1!
	rem 判断取出的字符是否等于TEST
	if !temp_str! equ TEST (
		rem 若这一行为TEST,则取出这一行的行索引
		set /a editRow1=!str:~0,1!+1
		set /a editRow2=!str:~0,1!+2
		echo !editRow1!,!editRow2!
	)
	rem 取出[TEST]下一行的索引+1
	set /a file_index=!str:~0,1!
	if !file_index! equ !editRow1! (
		echo !str!| findstr false >nul && (
			set "str=!str:false=true!"
		)
	)
	if !file_index! equ !editRow2! (
		echo !str!| findstr false >nul && (
			set "str=!str:false=true!"
		)
	)
	echo !str! >>tmp.txt
)
for /f "tokens=1* delims=:" %%i in ('type tmp.txt') do (
	set str2=%%j
	if "!str2!"==" " (
		call echo.>>new_file.ini
	) else (
		echo !str2:~0,-1! >>new_file.ini
	)
)
del %filename%,tmp.txt
move new_file.ini %filename%

rem 更改路径下的文件配置D:/unm2000/tools/data/cmsecurity.dat
cd D:/unm2000/tools/data
set filename=cmsecurity.dat
set ttx=e3afed0047b08059d0fada10f400c1e5
for /f "delims=" %%i in ('findstr /n .* %filename%') do (
	set str=%%i
		echo !str!| findstr 11111111111 >nul && (
		set "str=!str:11111111111=%ttx%!"
	)
	echo !str! >>tmp.ini
)
for /f "tokens=1* delims=:" %%i in ('type tmp.ini') do (
	set str2=%%j
	if "!str2!"==" " (
		call echo.>>new_file.ini
	) else (
		echo !str2:~0,-1! >>new_file.ini
	)
)
del %filename%,tmp.ini
move new_file.ini %filename%

rem 清理创建的临时变量
echo clear variable...
set num=,str=,editRow1=,editRow2=
echo completed!