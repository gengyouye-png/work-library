#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRUE 1
#define FALSE 0

void shuffle(int *deck, int n_cards)
{
    static int first_time = TRUE;

    if (first_time)
    {
        first_time = FALSE;
        srand((unsigned int)time(NULL));
    }

    for (int i = n_cards - 1; i > 0; i--)
    {
        int j = rand() % (i + 1);
        int temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
}

int main(void)
{
    int deck[] = {1, 2, 3, 4, 5};
    int n_cards = sizeof(deck) / sizeof(deck[0]);

    shuffle(deck, n_cards);

    printf("洗牌結果：");

    for (int i = 0; i < n_cards; i++)
    {
        printf("%d ", deck[i]);
    }

    printf("\n");
    return 0;
}