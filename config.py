# -*- coding: utf-8 -*-
"""
config.py
---------
Constantes globais do jogo de penaltis.
Altere aqui para ajustar dificuldade, tamanho da tela, etc.
"""

# ── Janela ────────────────────────────────────────────────────────────────────
TITULO  = 'Penaltis - Brasil x Alemanha'
WIDTH   = 800
HEIGHT  = 600
FPS     = 60

# ── Cores ─────────────────────────────────────────────────────────────────────
WHITE       = (255, 255, 255)
BLACK       = (0,   0,   0)
GREEN       = (34,  139, 34)
DARK_GREEN  = (0,   100, 0)
YELLOW      = (255, 215, 0)
RED         = (220, 20,  60)
BLUE        = (30,  144, 255)
GRAY        = (180, 180, 180)
DARK_GRAY   = (60,  60,  60)
SKY_TOP     = (80,  160, 220)
SKY_BOT     = (180, 220, 255)
ORANGE      = (255, 140, 0)
LIGHT_GREEN = (124, 252, 0)
GOLD        = (255, 200, 0)

# Brasil
BRA_AMARELO = (250, 220,   0)
BRA_VERDE   = (0,   155,  58)
BRA_AZUL    = (0,    39, 118)

# Alemanha
ALE_PRETO   = (20,   20,  20)
ALE_VERM    = (200,   0,  30)

# ── Gol ───────────────────────────────────────────────────────────────────────
GOL_X = WIDTH  // 2 - 200
GOL_W = 400
GOL_Y = 50
GOL_H = 220

# ── Regras ────────────────────────────────────────────────────────────────────
MAX_COBRANÇAS    = 7
GOLS_PARA_VENCER = 4
VIDAS_INICIO     = 3
MAX_CHARGE       = 90   # frames para carga maxima

# ── Estados do jogo ───────────────────────────────────────────────────────────
STATE_INTRO   = 'intro'
STATE_PLAYING = 'playing'
STATE_RESULT  = 'result'
STATE_WIN     = 'win'
STATE_LOSE    = 'lose'

# ── Zonas do gol: nome -> (fracao_x, fracao_y) ───────────────────────────────
ZONAS = {
    'canto_sup_esq': (0.12, 0.18),
    'centro_esq':    (0.12, 0.60),
    'canto_inf_esq': (0.12, 0.88),
    'centro_alto':   (0.50, 0.18),
    'centro':        (0.50, 0.55),
    'centro_baixo':  (0.50, 0.88),
    'canto_sup_dir': (0.88, 0.18),
    'centro_dir':    (0.88, 0.60),
    'canto_inf_dir': (0.88, 0.88),
}

NOMES_ZONA = {
    'canto_sup_esq': 'Canto sup. esq',
    'centro_esq':    'Centro esq',
    'canto_inf_esq': 'Canto inf. esq',
    'centro_alto':   'Centro alto',
    'centro':        'Centro',
    'centro_baixo':  'Centro baixo',
    'canto_sup_dir': 'Canto sup. dir',
    'centro_dir':    'Centro dir',
    'canto_inf_dir': 'Canto inf. dir',
}

# Zonas que o goleiro NUNCA defende (centro do gol)
ZONAS_CENTRO = ('centro', 'centro_alto', 'centro_baixo')

# Zonas laterais que o goleiro pode defender
ZONAS_GOLEIRO = [
    'canto_sup_esq', 'centro_esq', 'canto_inf_esq',
    'canto_sup_dir', 'centro_dir', 'canto_inf_dir',
]
