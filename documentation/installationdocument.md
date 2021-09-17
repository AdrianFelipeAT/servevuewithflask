## Installation Document
### Serve VueJs with Flask

1. Instalar entorno virtual    
   
   ~~~
   pip install virtualenv
   ~~~

2. Crear el entorno virtual (venv es el nombre del entorno, sin embargo el nombre es opcional), se indica además que el entorno correrá con python3

    ~~~
    virtualenv -p python3 venv
    ~~~

3. Iniciar el entorno virtual

    ~~~
    source venv/bin/activate
    ~~~

4. Instalar paquetes para iniciar Vue
   ~~~
   sudo npm i -g @vue/cli-init
   ~~~

5.  Instalar las dependencias:  
    1.  Acceder a directorio front_vue/  

    ~~~
    npm install
    ~~~
    1.  Acceder a directorio documentation/  

    ~~~
    pip install -r requirements.txt
    ~~~

6. Instalar Axios
   1. (Axios es una librería JavaScript que puede ejecutarse en el navegador y que nos permite hacer sencillas las operaciones como cliente HTTP)  
   
    ~~~
    npm install --save axios
    ~~~

7. Correr servidor local de Flask
    ~~~
    python3 serve.py
    ~~~

