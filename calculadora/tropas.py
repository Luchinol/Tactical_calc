# tropas.py

# Datos de Fuerzas Propias (detalladas)
friendly_forces = [
    ("Grupo Acorazado Ligero", "Compañía Infantería Mecanizada", "Compañía", 1, "Carros M-113", 13),
    ("", "Escuadrón de Tanques Leo 1", "Escuadrón", 2, "Tanques leopard 1", 26),
    ("Sección Telecomunicaciones", "Cuadrilla de Telecomunicaciones Comando", "Subcuadrilla", 2, "Camión Liviano", 2),
    ("", "Cuadrilla de Telecomunicaciones Combate", "Subcuadrilla", 1, "Camión Liviano", 1)
]

# Datos de Fuerzas Adversarias (estructura detallada y actualizada)
adversary_structure = [
    {
        "unidad_superior": "DIVISIÓN 'LINARES'",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de transmisiones de Zona N°5050",
                "pequena_unidad": "Compañía",
                "cantidad": None,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            },
            {
                "unidad_subordinada": "Batallón de Ingenieros N°5040",
                "pequena_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            }
        ]
    },
    {
        "unidad_superior": "GUC Blindada 'LANCEROS' N°5100",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de tanques N°5120",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5110",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5111",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5112",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5125",
                "pequena_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44
            },
            {
                "unidad_subordinada": "Batallón Ingenieros de combate N°5141",
                "pequena_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            }
        ]
    },
    {
        "unidad_superior": "GUC Acorazada 'Bari'",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de tanques N°5121",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5113",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5114",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Batallón de Infantería Blindado N°5115",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5226",
                "pequena_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44
            },
            {
                "unidad_subordinada": "Batallón Ingenieros de combate N°5142",
                "pequena_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            },
            {
                "unidad_subordinada": "Compañía de transmisiones N°5252",
                "pequena_unidad": None,
                "cantidad": None,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            }
        ]
    },
    {
        "unidad_superior": "GUC CABALLERÍA BLINDADA 'ALDUNATE' N°5300",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón de tanques N°5123",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5316",
                "pequena_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5318",
                "pequena_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44
            },
            {
                "unidad_subordinada": "Regimiento de Caballería Blindada N°5319",
                "pequena_unidad": "Escuadrones",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 44
            },
            {
                "unidad_subordinada": "Batallón Ingenieros de combate N°5344",
                "pequena_unidad": "Compañía",
                "cantidad": 2,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            },
            {
                "unidad_subordinada": "Compañía de transmisiones N°5355",
                "pequena_unidad": None,
                "cantidad": None,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            }
        ]
    },
    {
        "unidad_superior": "ESCALÓN TÁCTICO",
        "subordinados": [
            {
                "unidad_subordinada": "Batallón Infantería Blindado",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "VTP",
                "cantidad_medios_por_uf": 39
            },
            {
                "unidad_subordinada": "Batallón de Tanques",
                "pequena_unidad": "Compañía",
                "cantidad": 3,
                "tipo_medios": "Tanque T-55",
                "cantidad_medios_por_uf": 14
            },
            {
                "unidad_subordinada": "Compañía de Ingeneiros Mecanizados",
                "pequena_unidad": "Sección",
                "cantidad": 3,
                "tipo_medios": None,
                "cantidad_medios_por_uf": None
            }
        ]
    }
]

def get_friendly_forces():
    """Devuelve la lista de fuerzas propias detalladas."""
    return friendly_forces

def get_adversary_structure():
    """Devuelve la estructura jerárquica detallada de las fuerzas adversarias."""
    return adversary_structure