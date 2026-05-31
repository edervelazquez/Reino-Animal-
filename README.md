# Reino Animal

Práctica de Programación Orientada a Objetos (POO) en Python que modela una
jerarquía del reino animal aplicando los cuatro pilares del paradigma:
**abstracción**, **encapsulamiento**, **herencia** y **polimorfismo**.

Una clase abstracta `Animal` define la estructura común, y las clases `Gato`,
`Pollo` y `Vaca` heredan de ella, cada una con su propio comportamiento. Un
módulo principal (`main.py`) instancia los objetos y prueba sus métodos.

## Conceptos aplicados

- **Abstracción:** `Animal` hereda de `ABC` y declara el método abstracto
  `_hablar()` con `@abstractmethod`, obligando a cada clase hija a implementarlo.
- **Encapsulamiento:** atributos privados con doble guion bajo (p. ej. `__nombre`,
  `__edad`).
- **Herencia:** `Gato`, `Pollo` y `Vaca` reutilizan los atributos y métodos de
  `Animal` mediante `super().__init__(...)`.
- **Polimorfismo:** el método `_hablar()` se redefine en cada clase hija, por lo
  que la misma llamada produce un resultado distinto según el objeto
  (`Miau`, `Pio`, `Muuu`).

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `reino_animal.py` | Clase abstracta `Animal` con los atributos `nombre` y `edad`, el método abstracto `_hablar()` y el método `obtenerDatos()`. |
| `gato.py` | Clase `Gato`; implementa `_hablar()` → `"Miau"`. |
| `pollo.py` | Clase `Pollo`; implementa `_hablar()` → `"Pio"` y el método propio `poner_huevo()`. |
| `vaca.py` | Clase `Vaca`; implementa `_hablar()` → `"Muuu"` y el método propio `produccionDelDia()`. |
| `main.py` | Instancia las clases y prueba todos los métodos. |

## Cómo ejecutar

Requiere Python 3.

```bash
python main.py
```

## Salida esperada

```
--INSTANCIAS DEL REINO ANIMAL--
---METODOS DE GATO
Miau
Es un Gato y tiene 10 anios.
---METODOS DE POLLO
Pio
Es un Pollo y tiene 2 anios.
El Pollo esta poniendo un huevo...
---METODOS DE VACA--
Muuu
Es un Vaca, y tiene 3 anios.
La vaca produjo el dia de hoy 25 L de leche
```

## Autor

Eder Velázquez — Universidad Politécnica de Baja California

