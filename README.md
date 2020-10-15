# Par++ Avance 1

Se utilizó la herramienta ply para el scanner y parser. 
Se definieron las palabras reservadas, tokens, expresiones regulares simples y complejas.
Se realizaron pruebas por medio de lectura de archivos .txt y todos los casos fueron aprobados. 

Algunas modificaciones y agregaciones fueron realizadas a los diagramas y gramática ya que no se tenían contempladas y fueron surgiendo a la hora de realizar el código. Estas fueron actualizadas en los archivos del equipo. La gramática fue terminada en su totalidad para este avance. 

El archivo "prueba-1.txt" cubre todas las funciones definidas. 


# Par++ Avance 2
Se trabajó en la semántica básica de variables y expresiones del lenguaje Par++.
Para el directorio de procedimientos se utilizó un diccionario que contiene el nombre de las funciones, el tipo de dato y las variables involucradas. Para la tabla de variables también se utilizó un diccionario que contiene el nombre de la variable, kind, tipo de dato, scope y su valor.

Se crearon 2 funciones, una para agregar una nueva función al directorio de procedimiento, validando que su nombre sea único y asignando sus datos correspondientes. La otra función se encarga de agregar elementos a la tabla de variables de acuerdo a su scope y validando que no haya sido declarada previamente dentro del mismo scope. 

En cuanto al subo semántico también se utilizó un diccionario como estructura de dato, la cual tiene la siguiente estructura: 
cubo = {
  left: {
    operador:{
      right: value
    }
  }
}
Donde left indica el tipo de dato (int, float, char y bool), operador incluye lógicos, relacionales y aritméticos y right indica el otro tipo de dato, value indica el tipo de dato de retorno o error en el caso indicado.
