# Changelog

## Alejandro
- Cree una rama llamada "**Alejandro**" para trabajar en las funciones del script principal.
### Funciones
- **Decimal**: La función convierte un **Byte** a decimal.
```
def  decimal(x) -> int:
    x  =  str(x)[::-1]
    result  =  0
    for  i  in  range(len(x)):
        if  x[i] ==  "1":
        result  +=  2**i
    return  result
```
- **Convert**: Convierte de carácter a la representación en **binario**.
```
def  convert(x) -> str:
    return  "0"  +  bin(x)[2::]
```

## Santiago
- Cree una rama llamada "santiago" para trabajar en el script principal del proyecto.