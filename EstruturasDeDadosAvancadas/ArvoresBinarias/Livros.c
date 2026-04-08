#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Livro{
    char nome[50];
    char autor[50];
    float preco;
    int quantidadeDisponivel;
    struct Livro *left, *right;
} Livro;

Livro* inserirNovoLivro(Livro* raiz, char* nome, char* autor, float preco, int quantidadeDisponivel) {
    if (raiz == NULL) {
        Livro* novo = (Livro*)malloc(sizeof(Livro));
        strcpy(novo->nome, nome);
        strcpy(novo->autor, autor);
        novo->preco = preco;
        novo->quantidadeDisponivel = quantidadeDisponivel;
        novo->left = novo->right = NULL;
        return novo;
    }

    if (strcmp(nome, raiz->nome) < 0) {
        raiz->left = inserirNovoLivro(raiz->left, nome, autor, preco, quantidadeDisponivel);
    } else if (strcmp(nome, raiz->nome) > 0) {
        raiz->right = inserirNovoLivro(raiz->right, nome, autor, preco, quantidadeDisponivel);
    } else {
        printf("Erro: Nome %s ja cadastrado no sistema", nome);
    }
    return raiz;
}

Livro* buscarLivro(Livro* raiz, char* nome) {
    if (raiz == NULL) return NULL;

    if (strcmp(nome, raiz->nome) == 0) {
        return raiz;
    } else if (strcmp(nome, raiz->nome) < 0) {
        return buscarLivro(raiz->left, nome);
    }
    return buscarLivro(raiz->right, nome);
}

void alterarPrecoLivro(Livro* raiz, char* nome) {
    Livro* auxiliar = buscarLivro(raiz, nome);

    if (auxiliar != NULL) {
        printf("=== Livro Encontrado! ===\n");
        printf("Nome: %s\n", auxiliar->nome);
        printf("=========================\n");
        printf("Informe o novo preco: ");
        scanf("%f", &auxiliar->preco);
        printf("\nPreco alterado com sucesso!\n");
    } else {
        printf("\nErro: Livro '%s' nao encontrado.\n", nome); 
    }
}

void alterarQuantidadeDisponivel(Livro* raiz, char* nome) {
    Livro* auxiliar = buscarLivro(raiz, nome);

    if (auxiliar != NULL) {
        printf("=== Livro Encontrado! ===\n");
        printf("Nome: %s\n", auxiliar->nome);
        printf("=========================\n");
        printf("Informe a nova quantidade disponivel: ");
        scanf("%d", &auxiliar->quantidadeDisponivel);
        printf("\nQuantidade disponivel alterada com sucesso!\n");
    } else {
        printf("\nErro: Livro '%s' nao encontrado.\n", nome); 
    }
}

void listarLivros(Livro* raiz) {
    if (raiz != NULL) {
        listarLivros(raiz->left);
        printf("Nome: %s | Autor: %s | Preco: %.2f | Quantidade: %d\n", raiz->nome, raiz->autor, raiz->preco, raiz->quantidadeDisponivel);

        listarLivros(raiz->right);
    }
}

int main() {
    Livro *raiz = NULL;
    char nome[50], autor[50];
    float preco;
    int quantidadeDisponivel;
    int opcao = 0;

    do {
        printf("\n=== Sistema de Gestao de Livros ===\n");
        printf("1. Cadastrar Novo Livro\n");
        printf("2. Buscar Livro\n");
        printf("3. Alterar Preco\n");
        printf("4. Alterar Quantidade Disponivel\n");
        printf("5. Listar Livros\n");
        printf("6. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Nome: ");
                scanf(" %[^\n]", nome);
                printf("Autor: ");
                scanf(" %[^\n]", autor);
                printf("Preco: ");
                scanf("%f", &preco);
                printf("Quantidade Disponivel: ");
                scanf("%d", &quantidadeDisponivel);
                raiz = inserirNovoLivro(raiz, nome, autor, preco, quantidadeDisponivel);
                break;
            case 2:
                printf("\nDigite o nome do livro para buscar: ");
                getchar(); // Limpar o buffer
                scanf("%[^\n]", nome);
                Livro* livroEncontrado = buscarLivro(raiz, nome);

                if (livroEncontrado != NULL) {
                    printf("=== Livro Encontrado! ===\n");
                    printf("Nome: %s\n", livroEncontrado->nome);
                    printf("Autor: %s\n", livroEncontrado->autor);
                    printf("Preco: %.2f\n", livroEncontrado->preco);
                    printf("Quantidade Disponivel: %d\n", livroEncontrado->quantidadeDisponivel);
                    printf("=========================\n");
                } else {
                    printf("\nLivro '%s' nao encontrado.\n", nome);
                }
                break;
            case 3:
                printf("\nDigite o nome do livro para alterar o preco: ");
                getchar();
                scanf("%[^\n]", nome);
                alterarPrecoLivro(raiz, nome);
                break;
            case 4:   
                printf("\nDigite o nome do livro para alterar a quantidade disponivel: ");
                getchar();
                scanf("%[^\n]", nome);
                alterarQuantidadeDisponivel(raiz, nome);             
                break;
            case 5:
                printf("\n--- Lista de Livros ---\n");

                if (raiz == NULL) {
                    printf("Arvore vazia.\n");
                } else {
                    listarLivros(raiz);
                }
                break;
            case 6:
                printf("Saindo do sistema...\n");
                break;
            default:
                printf("Opcao invalida!\n");
                break;
        }
    } while (opcao != 6);
    return 0;
}