
#include <stdlib.h>
#include <stdio.h>

typedef struct node_temp
{
    int value;
    struct node *add;
}
node;


int main(void)
 {

int MAX_VALUE = 5;
node *list= malloc(sizeof(node));
list = NULL;it
node *list_tmp = malloc( sizeof(node));


//node *list_tmp = list;

  for (int i=0; i< MAX_VALUE; i++)
    {
    list_tmp -> add = NULL;
    list_tmp -> value = i;
    list = list_tmp;
    printf("%i\n", list-> value);
    list_tmp = malloc(sizeof(node));

    }

}

