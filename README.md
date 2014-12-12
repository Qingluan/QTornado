#QTornado  Document
>Include Part
 
 - src
    + init_filter.py
    + initial_content.py
    + lib.py
    + Qtornado.py
 - bin 
    + Qtornado.py 
 
## Introduction 
    a foolish experence contribute me  to make this ..
    this is a very small and simple web framework base on tornado 
## Install 
    curl -fsSL https://raw.githubusercontent.com/Qingluan/QTornado/install.sh | sh 
## Useage 
    
    Qtornado.py PROJECT  
        -i , --init controller_name :  will create a new web  attached a    controller with arg --init  
        -c  controller_name : will add new controller , template ,route 
        -r True/False : just use within "-i " ,this will clear all incomplete files and re-init  
## Example

<code>Qtornado.py Web_test -i login</code> 

this will generate a tree like this :

    Web_test
    ├── controller.py
    ├── main.py
    ├── setting.py
    ├── static
    └── template
        ├── index.html
        └── login.html

and run web with <code>cd web_test && python main.py </code>

and you can change your db_engine by overide  generated file "setting.py"

    db_engine = motor.MotorClient()  # default is mongo db

...