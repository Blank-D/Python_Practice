%�رջ��ԣ������ӳٻ���������չ%
@echo off & setlocal EnableDelayedExpansion

rem ������õĲ�������
for %%a in (%*) do set /a num+=1
if defined num (echo ������ %num% ������) else echo û�е����κβ���

set fileName=%1
set oldText=%2
set newText=%3

echo %fileName%,%oldText%,%newText%,%num%

rem ��������С��3����ʾ�û�
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
	rem �滻����
	if defined featureText (
		rem ����ÿ���ַ����Ƿ����ָ���������ַ���ֻ�԰��������ַ������滻�ı�
		echo !str!| findstr %featureText% >nul && (
			set "str=!str:%oldText%=%newText%!"
		)
	) else (
		set "str=!str:%oldText%=%newText%!"
	)
	rem ��������кŵ��ı�д����ʱ�ļ�
	echo !str! >>tmp.txt
)
for /f "tokens=1* delims=:" %%i in ('type tmp.txt') do (
	rem ��:�ָ�ÿ���ַ���
	set "str=%%j"
	if "!str!"==" " (
		rem д��Դ�ļ���Ŀ���
		call echo.>>new_A.txt
	) else (
		rem ���ַ���д���ı���ÿ�л��һ���ո�ʹ���ַ����Ľ�ȡ����ȥ��ĩβ��һ���ո�
		echo !str:~0,-1!>>new_A.txt
	)
)



REM ɾ����ʱ�ļ����޸ĺ���ļ�ΪԴ�ļ�
del tmp.txt&move new_A.txt %fileName%

goto :end

:errArgsTip
	echo ----------------------
	echo ��������ȷ�Ĳ��� fileName oldText newText [featureText]
	echo -- fileName
	echo -- oldText
	echo -- newText
	echo -- featureText
	echo ----------------------
	
:end
	rem ִ����ű�Ҫ��num����ȡ��������Ӱ���´�ִ��
	set num=