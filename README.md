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
    curl -fsSL https://raw.githubusercontent.com/Qingluan/QTornado/master/install.sh | sh 
## Useage 
    
    usage: it is usage for qingluanTornado 
    this is a assistant for write web html weite by Qingluan github :
    http://github.com/Qingluan
    optional arguments:
      -h, --help            show this help message and exit
      -p PRO_NAME_PATH, --pro_name_path PRO_NAME_PATH
                            this argu is represent project's name
      -i INIT, --init INIT  add a init controller in initialization
      -c ADD_CONTROLLER, --add-controller ADD_CONTROLLER
      -r RE, --re RE
      -t THEME_CHOICE, --theme-choice THEME_CHOICE
      -u, --uninstall

## Example

<code>Qtornado.py -p Web_test -i login</code> 

this will generate a tree like this :

    Web_test
    ├── manifest.py
    ├── controller.py
    ├── main.py
    ├── setting.py
    ├── static
    └── template
        ├── index.html
        └── login.html

and run web with <code>cd web_test && python main.py </code> to start server 

if you want to change port , write _setting.py_ , change <code>port=8080</code>

and you can change your db_engine by overide  generated file "setting.py"

    db_engine = motor.MotorClient()  # default is mongo db

...

if you want to add a _html+controller+router_  , you can just 
> cd web_test
> python manifest.py -c newcontroller

