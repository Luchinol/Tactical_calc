# tropas.py

# Datos de Fuerzas Propias (detalladas) con parámetros AHP extendidos
# Cada tupla contiene:
# (Unidad Superior, Unidades Subordinadas, UF, Cantidad UF, Tipo de Medios, Cantidad Medios/U.F.,
#  Movilidad, Combate Nocturno, Celeridad, Flexibilidad, Integracion Medios, Integracion Apoyos)
friendly_forces = [
    ("Grupo Acorazado Ligero", "Compañía Infantería Mecanizada", "Compañía", 1, "Carros M-113", 13,
     3.0, 4.0, 3.0, 3.0, 4.0, 4.0),
    ("", "Escuadrón de Tanques Leo 1", "Escuadrón", 2, "Tanques leopard 1", 26,
     4.0, 4.0, 4.0, 3.5, 4.0, 4.0),
    ("Sección Telecomunicaciones", "Cuadrilla de Telecomunicaciones Comando", "Subcuadrilla", 2, "Camión Liviano", 2,
     2.5, 3.0, 2.0, 4.0, 3.0, 3.0),
    ("", "Cuadrilla de Telecomunicaciones Combate", "Subcuadrilla", 1, "Camión Liviano", 1,
     2.5, 3.0, 2.0, 4.0, 3.0, 3.0)
]

# Datos de Fuerzas Adversarias (estructura detallada y actualizada con valores AHP)
adversary_structure = [
    {
        "unidad_superior": "DIVISIÓN 'LINARES'",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de transmisiones de Zona N°5050",
                "pequeña_unidad": "Compañía",
                "cantidad": None,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [2.0, 2.0, 2.0, 2.5, 2.0, 2.0]
            },
            {
                "unidad_subordinada": "Batallón de Ingenieros N°5040",
                "pequeña_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [3.0, 3.0, 3.0, 3.5, 3.0, 3.0]
            }
        ]
    },
    {
        "unidad_superior": "GUC Blindada 'LANCEROS' N°5100",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de tanques N°5120",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14,
                "ahp": [4.5, 4.0, 4.5, 4.0, 4.5, 4.0]
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5110",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5111",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5112",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5125",
                "pequeña_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44,
                "ahp": [4.0, 4.0, 4.0, 3.5, 4.0, 4.0]
            },
            {
                "unidad_subordinada": "Batallón Ingenieros de combate N°5141",
                "pequeña_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [3.0, 3.0, 3.0, 3.5, 3.0, 3.0]
            }
        ]
    },
    {
        "unidad_superior": "GUC Acorazada 'Bari'",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de tanques N°5121",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14,
                "ahp": [4.5, 4.0, 4.5, 4.0, 4.5, 4.0]
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5113",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5114",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5115",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5226",
                "pequeña_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44,
                "ahp": [4.0, 4.0, 4.0, 3.5, 4.0, 4.0]
            },
            {
                "unidad_subordinada": "Batallón Ingenieros de combate N°5142",
                "pequeña_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [3.0, 3.0, 3.0, 3.5, 3.0, 3.0]
            },
            {
                "unidad_subordinada": "Compañía de transmisiones N°5252",
                "pequeña_unidad": None,
                "cantidad": None,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [2.0, 2.0, 2.0, 2.5, 2.0, 2.0]
            }
        ]
    },
    {
        "unidad_superior": "GUC CABALLERÍA BLINDADA 'ALDUNATE' N°5300",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de tanques N°5123",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14,
                "ahp": [4.5, 4.0, 4.5, 4.0, 4.5, 4.0]
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5316",
                "pequeña_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44,
                "ahp": [4.0, 4.0, 4.0, 3.5, 4.0, 4.0]
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5318",
                "pequeña_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44,
                "ahp": [4.0, 4.0, 4.0, 3.5, 4.0, 4.0]
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5319",
                "pequeña_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44,
                "ahp": [4.0, 4.0, 4.0, 3.5, 4.0, 4.0]
            },
            {
                "unidad_subordinada": "Batallón Ingenieros de combate N°5344",
                "pequeña_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [3.0, 3.0, 3.0, 3.5, 3.0, 3.0]
            },
            {
                "unidad_subordinada": "Compañía de transmisiones N°5355",
                "pequeña_unidad": None,
                "cantidad": None,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [2.0, 2.0, 2.0, 2.5, 2.0, 2.0]
            }
        ]
    },
    {
        "unidad_superior": "ESCALÓN TÁCTICO",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón Infantería Blindado",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39,
                "ahp": [3.5, 3.5, 3.0, 3.0, 3.5, 3.0]
            },
            {
                "unidad_subordinada": "Batallón de Tanques",
                "pequeña_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14,
                "ahp": [4.5, 4.0, 4.5, 4.0, 4.5, 4.0]
            },
            {
                "unidad_subordinada": "Compañía de Ingeneiros Mecanizados",
                "pequeña_unidad": "Sección",
                "cantidad": 3,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None,
                "ahp": [3.0, 3.0, 3.0, 3.5, 3.0, 3.0]
            }
        ]
    }
]

def get_friendly_forces():
    """Devuelve la lista de fuerzas propias detalladas con parámetros AHP extendidos."""
    return friendly_forces

def get_adversary_structure():
    """Devuelve la estructura jerárquica detallada de las fuerzas adversarias, con parámetros AHP para cada subordinado."""
    return adversary_structure