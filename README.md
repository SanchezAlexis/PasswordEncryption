# Cifrado de contraseñas

La protección de contraseñas es una de las prácticas mas importantes en el campo de la seguridad informática. Con el objetivo de proteger la información personal de los usuarios, las contraseñas deben estar cifradas en todo momento. El cifrado es un procedimiento criptográfico que oculta la información de un mensaje mediante el uso de un algoritmo. Existen distintos tipos de cifrado: simétrico y asimétrico. El cifrado simétrico usa la misma llave para el encriptado y desencriptado de un archivo. El cifrado asimétrico usa distintas llaves para realizar el mismo proceso. El código presentado en este repositorio utiliza cifrado simétrico mediante una llave pública. Estos scripts muestran como encriptar un archivo que contiene las contraseñas de un usuario. Este código es parte del *backend* de una aplicación que se encarga de mantener las contraseñas seguras y cifradas. 

## Procedimiento

Se debe tener una contraseña maestra con la cual se generará una llave que se usará para cifrar. Los nombres y contraseñas de cada cuenta se escriben en un archivo de texto y se cifra el contenido usando la llave. Este proceso solo sucederá cuando sea la primera vez que se ingresan datos. Para acceder a los datos, se pide la contraseña maestra y se trata de desencriptar el archivo. En caso de no lograr la descripción, quiere decir que se dio incorrectamente la contraseña maestra. 

### Bibliotecas usadas

La biblioteca *cryptography* permitirá hacer la generación de una llave y el encriptado del archivo. Esta biblioteca usará las siguientes extensiones:

	 - Hashes: Obtiene el hasheo de la llave.
	 - PBKDF2HMAC: Aporta mayor seguridad a la llave para evitar ataques de fuerza bruta. 
	 - Fernet: Realiza el cifrado y descrifrado. 

### Generación de llave para encriptado (GenerateKey)

El método generateKey recibe como único parámetro la contraseña maestra, dada por el usuario. Esta contraseña se decodifica a bits para poder manejarla. El hasheo de contraseñas consiste en procesar texto mediante una función que regresa una cadena en base hexadecimal. El recurso PBKDF2HMAC creará un objeto de hasheo usando una sal (elemento que da mayor seguridad a la llave) y el algoritmo SHA256. La llave se crea usando el objeto de hasheo y la contraseña. Finalmente, se decodifican los bits y se obtiene de regreso la llave final. 

![hasheo2](https://user-images.githubusercontent.com/54086948/109071702-adb0bb00-76b9-11eb-8e32-c799e0ed89a1.jpeg)

### Encriptado

El método *encryption* recibe como parámetros la llave generada y una lista de diccionarios. Esta lista será utilizada para crear un archivo de tipo JSON que pueda ser cifrado. Antes de cifrar, se revisa que la lista tenga elementos. En caso de no tener datos, el usuario está ingresando por primera vez y se crea un archivo JSON vacío. En este archivo se guardarán los datos que vaya proporcionando el usuario. En caso de tener datos, el usuario esta dando sus contraseñas para guardarlas con cifrado. En este caso, se convierte el contenido de la lista en estructura JSON con los datos de la lista de diccionarios y se guarda en un archivo. Usando la llave, se crea un objeto único de tipo Fernet que hará el cifrado. El contenido del archivo JSON es tomado como texto y se encripta usando el objeto Fernet. Con el texto cifrado, se escribe un archivo de tipo *Encrypted* y se guarda en la raíz del proyecto. Finalmente, el archivo creado con texto sin cifrar se elimina del proyecto. Solo quedará almacenado el archivo cifrado. 

![encriptado2](https://user-images.githubusercontent.com/54086948/109071700-adb0bb00-76b9-11eb-851d-fbb30ed5e599.jpeg)

### Desencriptado

El proceso de desencriptado funciona de manera similar al encriptado, pero de manera inversa. En primer lugar, se debe dar la contraseña maestra y generar una llave con el método generateKey. La llave creada se recibe como parámetro en el método de desencriptado. Usando un manejo de excepciones, se intenta abrir el archivo de tipo *encrypted* con toda la información de las contraseñas.  En caso de no encontrar el archivo, se lanza una excepción y se regresa un objeto vacío. En caso de haberlo encontrado, se lee el contenido del archivo y crea un objeto Fernet con la llave recién creada. Se intenta hacer el descifrado con el objeto Fernet. Si no se puede descifrar, quiere decir que la contraseña dada no es igual a la contraseña con la cual se cifró inicialmente el archivo. Con el texto desencriptado, se convierte String y luego a una lista de diccionarios. Con esta lista, se convierte a formato JSON y regresa esa información. Dicha información, serán los nombres y contraseñas sin cifrar. El archivo JSON puede visualizarse usando herramientas adicionales de interfaz gráfica. 

![descifrado2](https://user-images.githubusercontent.com/54086948/109071699-ad182480-76b9-11eb-9727-aa6d3c25006e.jpeg)
