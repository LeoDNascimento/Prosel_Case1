import requests
import os
from shutil import make_archive
from datetime import date

"""
 @description Função que irá realizar o download dos arquivos online em uma pasta local

 @param {string} url = url do arquivo online
 @param {string} local_address = local da pasta em que o download será feito
"""
def download_files(url, local_address):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_address, 'wb') as file:
            file.write(response.content)
        print("Download finalizado")
    else:
        response.raise_for_status()

def compact_files(dir_name):
    dir_name = os.path.join(dir_name)
    make_archive('arquivos_compactados_{}'.format(date.today()), 'zip', dir_name)
   
if __name__ == '__main__':
    # Variavel que armazena o nome da pasta que será feito o download
    OUTPUT_DIR = "output"
    BASE_URL = "https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/{}"
    
    url_list = ['Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf','Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546.pdf','Anexo_III_DC_2021_RN_465.2021.v2.pdf','Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf']
    aux=1
    for i in url_list:
        file_name = os.path.join(OUTPUT_DIR, 'ANEXO_{}.pdf'.format(aux))
        download_files(BASE_URL.format(i), file_name)
        aux+=1
    compact_files(OUTPUT_DIR)


"""
https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf

https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546.pdf

https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf

https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf
"""