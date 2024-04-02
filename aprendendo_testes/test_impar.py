from impar import is_impar

def testa_se_retorna_true_para_numero_impar():
    'Retorna true se o numero for impar'
    assert is_impar(15) is True

def testa_se_retorna_false_para_numero_par():
    'Retorna false se o numero for par'
    assert is_impar(22) is False    