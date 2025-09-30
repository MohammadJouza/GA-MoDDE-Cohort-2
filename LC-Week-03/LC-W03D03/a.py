# User name: root
# password: 0000
# #%qwwdjklsdflczxdv234


"""  
do these commands
1- psql -U postgres
2- CREATE DATABASE generalassembly;
C:\Program Files\PostgreSQL\18\bin
"""
# YS: finish everything
# NO: have Error / Problem
# 

cd "C:\Program Files\PostgreSQL\18\bin"


initdb -D "C:\Program Files\PostgreSQL\18\data" -U postgres -W


pg_ctl register -N "postgresql-x64-18" -D "C:\Program Files\PostgreSQL\18\data"


net start postgresql-x64-18



""" 
C:\Windows\System32
C:\Windows
C:\Windows\System32\Wbem
C:\Windows\System32\WindowsPowerShell\v1.0\


 """



""" 
Zinab Path



C:\Users\owner\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\Zainab\AppData\Local\Programs\Python\Python313\Scripts\;C:\Users\Zainab\AppData\Local\Programs\Python\Python313\;C:\Users\Zainab\AppData\Local\Microsoft\WindowsApps;C:\Users\Zainab\AppData\Roaming\npm;C:\Users\Zainab\.dotnet\tools;C:\Users\Zainab\AppData\Roaming\Python\Python311\Scripts;C:\Users\Zainab\AppData\Roaming\Programs\Zero Install;%USERPROFILE%\.dotnet\tools;C:\Program Files\PostgreSQL\18\bin


 """


CREATE TABLE students_2 (
  student_id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  mobile VARCHAR(50)
);