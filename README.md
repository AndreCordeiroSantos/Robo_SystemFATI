# Robo_SystemFATI
Robô para o sistema FATI
Criado e desenvolvido por Andre Santos, em um ambiente CallCenter de um (Banco Nacional)
Descrição do Robô de Automação de Instalação de Programas em Python

O robô de automação de instalação de programas criado em Python é um script eficiente e poderoso projetado para simplificar o processo de instalação ou atualização de programas em um ambiente com um único usuário administrador. Ele foi desenvolvido para lidar com a necessidade de instalar programas em um grande número de máquinas, agilizando o processo que normalmente seria demorado se realizado manualmente, máquina por máquina.

O robô funciona utilizando a estrutura de cliente-servidor, onde vários computadores com acesso a um sistema web podem enviar solicitações de instalação de programas de qualquer lugar. Essas solicitações são enviadas para um banco de dados MySQL, onde o robô acessa essas informações para executar a instalação.

O fluxo de trabalho do robô é o seguinte:

1 - O cliente envia uma solicitação de instalação ou atualização de programa através do sistema web.
2 - Os detalhes da solicitação, como o programa a ser instalado e a máquina de destino, são armazenados no banco de dados MySQL.
3 - O robô periodicamente verifica o banco de dados em busca de solicitações pendentes.
4 - Quando encontra uma solicitação pendente, o robô analisa o status da tabela e identifica que há uma instalação a ser realizada.
5 - O robô utiliza scripts em PowerShell, integrados no Python, para executar a instalação do programa de forma rápida e eficiente na máquina de destino.
6 - Após a conclusão da instalação, o status da tabela no banco de dados é atualizado para refletir o resultado da operação.
7 - O robô continua verificando o banco de dados em intervalos regulares para identificar novas solicitações e executar as instalações correspondentes.

Essa abordagem automatizada permite que a instalação ou atualização de programas seja realizada de forma mais rápida e eficiente, economizando tempo e recursos. O uso do banco de dados MySQL como intermediário centraliza e organiza as solicitações, garantindo que nenhuma instalação seja perdida ou ignorada.
