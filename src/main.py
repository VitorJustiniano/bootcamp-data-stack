from time import sleep


def pimeira_atividade():
    print("primeira atividade rodou com sucesso")
    sleep(2)

def segunda_atividade():
    print("segunda atividade rodou com sucesso")
    sleep(2)

def terceira_atividade():
    print("terceira atividade rodou com sucesso")
    sleep(2)

def pipeline():
    pimeira_atividade()
    segunda_atividade()
    terceira_atividade()

pipeline()