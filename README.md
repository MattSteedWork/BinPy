# BinPy
Search GTFObins from the command line, full program or quick search.   

### Full Program   
```   
python3 BinPy.py
   
Example:   
   

▄▄▄▄    ██▓ ███▄    █       ██▓███  ▓██   ██▓
▓█████▄ ▓██▒ ██ ▀█   █      ▓██░  ██▒ ▒██  ██▒
▒██▒ ▄██▒██▒▓██  ▀█ ██▒     ▓██░ ██▓▒  ▒██ ██░
▒██░█▀  ░██░▓██▒  ▐▌██▒     ▒██▄█▓▒ ▒  ░ ▐██▓░
░▓█  ▀█▓░██░▒██░   ▓██░ ██▓ ▒██▒ ░  ░  ░ ██▒▓░
░▒▓███▀▒░▓  ░ ▒░   ▒ ▒  ▒▓▒ ▒▓▒░ ░  ░   ██▒▒▒  
▒░▒   ░  ▒ ░░ ░░   ░ ▒░ ░▒  ░▒ ░      ▓██ ░▒░  
░    ░  ▒ ░   ░   ░ ░  ░   ░░        ▒ ▒ ░░   
░       ░           ░   ░            ░ ░      
     ░                  ░            ░ ░      

Type 'help' for more information
Search GTFObins: 7z
7z: https://gtfobins.github.io/gtfobins/7z/

+-----------+-----------------------------+-----------------------------+
| Function  | Description                 | Code                        |
+-----------+-----------------------------+-----------------------------+
| File read | It reads data from files,   | LFILE=file_to_read          |
|           | it may be used to do        | 7z a -ttar -an -so $LFILE | |
|           | privileged reads or         | 7z e -ttar -si -so          |
|           | disclose files outside a    |                             |
|           | restricted file system.     |                             |
+-----------+-----------------------------+-----------------------------+


+----------+-----------------------------+-----------------------------+
| Function | Description                 | Code                        |
+----------+-----------------------------+-----------------------------+
| Sudo     | If the binary is allowed to | LFILE=file_to_read          |
|          | run as superuser by sudo,   | sudo 7z a -ttar -an -so     |
|          | it does not drop the        | $LFILE | 7z e -ttar -si -so |
|          | elevated privileges and may |                             |
|          | be used to access the file  |                             |
|          | system, escalate or         |                             |
|          | maintain privileged access. |                             |
+----------+-----------------------------+-----------------------------+
```
#### Quick Search   
```
python3 BinPy.py 'search Term'   
   
Example:   
   
python3 BinPy.py 7z
   
7z: https://gtfobins.github.io/gtfobins/7z/

+-----------+-----------------------------+-----------------------------+
| Function  | Description                 | Code                        |
+-----------+-----------------------------+-----------------------------+
| File read | It reads data from files,   | LFILE=file_to_read          |
|           | it may be used to do        | 7z a -ttar -an -so $LFILE | |
|           | privileged reads or         | 7z e -ttar -si -so          |
|           | disclose files outside a    |                             |
|           | restricted file system.     |                             |
+-----------+-----------------------------+-----------------------------+


+----------+-----------------------------+-----------------------------+
| Function | Description                 | Code                        |
+----------+-----------------------------+-----------------------------+
| Sudo     | If the binary is allowed to | LFILE=file_to_read          |
|          | run as superuser by sudo,   | sudo 7z a -ttar -an -so     |
|          | it does not drop the        | $LFILE | 7z e -ttar -si -so |
|          | elevated privileges and may |                             |
|          | be used to access the file  |                             |
|          | system, escalate or         |                             |
|          | maintain privileged access. |                             |
+----------+-----------------------------+-----------------------------+


```



