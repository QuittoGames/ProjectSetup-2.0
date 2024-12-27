**ProjectSetup - Versão 2.0**

O ProjectSetup é um script automatizado para criação de projetos, com foco em simplificar o processo de configuração de novos diretórios e arquivos. A versão anterior do ProjectSetup permitia a criação de pastas e arquivos com extensões e nomes configuráveis, mas a versão 2.0 traz melhorias significativas, incluindo novos tipos de projeto, como sites e projetos Django, além de uma interface de usuário mais interativa.

Novidades da Versão 2.0:
Interface Interativa: Agora, o usuário pode escolher entre diferentes tipos de projetos (Código, Website ou Django) diretamente no menu inicial.
Criação de Sites: A nova versão permite a criação rápida de sites com a estrutura básica de arquivos HTML.
Integração com Django: Adicionamos uma funcionalidade para criar automaticamente um projeto Django, facilitando o início de projetos web baseados nesse framework.
Melhorias na Estrutura de Código: O código foi otimizado, com a separação de funções específicas para cada tipo de projeto e verificação mais robusta de entradas do usuário.
Estrutura do Projeto:

- `index.py`: O script principal agora gerencia a criação de diferentes tipos de projetos, como aplicativos em Python, sites ou projetos Django.
- `config.py`: Este arquivo contém as configurações para os tipos de arquivos e extensões suportados.
- `tool.py`: Funções utilitárias para limpar a tela, verificar dependências e instalar o Django.
- `UI.py`: Interface de usuário para facilitar a interação com o script.

Como Executar:
Clone o repositório:
git clone https://github.com/QuittoGames/ProjectSetup-2.0

Nota sobre o estado de desenvolvimento da UI
A interface gráfica (UI) ainda está em desenvolvimento e não está pronta para produção. Isso significa que, embora o código esteja funcional, pode haver ajustes e melhorias a serem feitos para torná-la mais estável e eficiente antes de ser utilizada em um ambiente de produção.

bash
Copiar código
Para executar o script, basta rodar o arquivo index.py com Python:

Esta descrição e o código demonstram as melhorias da versão 2.0 em relação à versão anterior, oferecendo uma explicação clara do novo fluxo e recursos. Se precisar de mais detalhes ou ajustes, estou à disposição!
