
#include <stdio.h>
# include <stdlib.h>
#include <sys/resource.h>
#include <ctype.h>
#include <stdbool.h>
#define LENGTH 45

//const char *dictionary= "Ciao";
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

bool unload(void);
bool load(const char *dictionary);
unsigned int hash(const char *word);
const unsigned int N = 26;

node *table[N];
unsigned int count;


int main(void)
{
    const char *dictionary= "Ciao";
bool loaded = load(dictionary);
unload();
}

bool load(const char *dictionary)
{
     for (int m=0; m< N; m++)
    {
        table[m]= malloc(sizeof(node));
         if (table[m]==NULL)
             {
                for (int o=0; o < m+1; o++)
                {
                    free(table[o]);
                }

                  return false;
              }
            table[m]= NULL;
    }

    FILE *file= fopen(dictionary,"r");
    if (file==NULL)
        {
             return false;
        }

    char* wordes= malloc(sizeof(char) * LENGTH);

    if (wordes==NULL)
    {
        return false;
    }
    int index;

     while (fscanf(file,"%s",wordes)!= EOF)
        {
             index= hash(wordes);
            // wordings= table[index];
            // *node tmp= wordings;
            count++;

             if(table[index]!= NULL)
                 {
                    node* wordings = malloc(sizeof(node));
                    //wordings->next= NULL;

                     if (wordings==NULL)
                     {
                      return false;
                     }
                    for (int j=0; j<LENGTH; j++)
                    {
                        wordings -> word[j] = wordes[j];
                        if (&wordes[j]==NULL)
                        {
                            break;
                        }
                    }

                  node* tmp= table[index];
                  table[index]=wordings;
                  wordings= tmp;
                  wordings-> next= table[index];


                 }

         else{
                for (int k=0; k<LENGTH; k++)
                    {
                        table[index]->word[k]= wordes[k];

                         if (&wordes[k]==NULL)
                            {
                                break;
                            }
                    }



                }

            }
                fclose(file);
                return true;

    //node* wordings = malloc(sizeof(node));
    // TODO
    //return false;
}



bool unload(void)
{

    for (int i=0; i< N; i++)
    {
        node *tmp = table[i];
       while (tmp!= NULL)
       {
            node *cursor = tmp;
            cursor = tmp-> next;
            free (tmp);
            tmp = cursor;
       }
    }
    for (int p=0; p< N; p++)
    {
        free(table[p]);
    }

    // TODO
    return true;
}

unsigned int hash(const char *word)
{
    int n= word[0];
   // int l=0;
    for (int i=0; i< LENGTH + 1; i++)
     {
        while (&(word[i]) != NULL)
        {
            while (word[i]!= '\0')
          {

                n= n+ word[i+1]- 'z';
                i++;

          }
             return n % N;
        }

     }

    // TODO: Improve this hash function
    //return toupper(word[0]) - 'A';
    return n % N;
}


