import helper
from send_mail import *


if __name__ == '__main__':

    helper.pdf_generator("Fulano de Tal")
    helper.merge_pdf("files/certificado.pdf", "files/modelo-certificado.pdf", "files/saida-certificado.pdf")

    send('fulanodetal@gmail.com', 'Certificado', 'Olá, estamos enviando em anexo o seu certificado de participação no evento.', files=["files/saida-certificado.pdf"])