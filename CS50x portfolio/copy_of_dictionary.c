

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

unsigned int count = 0;
char* wordes;


// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int hash_value;
// Hash table
node *table[N];



// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    hash_value = hash(wordes);

    node *cursor= table[hash_value];

    //for (int i=0; i<LENGTH + 1; i++)

    //{
            if(strcasecmp((wordes),(cursor->word))==0)
        {
           return true;
        }
          cursor= cursor-> next;
    // }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int n= word[0];

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


    return n % N;

}

    // TODO: Improve this hash function
    //return toupper(word[0]) - 'A';



// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
     for (int m=0; m< N; m++)
    {
        //table[m]= malloc(sizeof(node));
          table[m]=NULL;
           //  {
                 // return false;
             // }
           // table[m]= NULL;
    }

    FILE *file= fopen(dictionary,"r");
    if (file==NULL)
        {
             return false;
        }

    wordes= malloc(sizeof(char)* (LENGTH +1));

    if (wordes==NULL)
    {
        return false;
    }
    int index = 0;

     while (fscanf(file,"%s",wordes)!= EOF)
        {
             index= hash(wordes);
            // wordings= table[index];
            // *node tmp= wordings;
            count++;

    node *first_word = NULL;

         if (table[index]==NULL)
         {

            first_word= malloc(sizeof(node));

                if(first_word == NULL)
                {
                    return false;
                }
                first_word-> next= NULL;

                for (int k=0; k<LENGTH + 1; k++)
                    {
                        if (wordes[k]== '\0')
                            {
                                break;
                           }
                            else
                           {
                                 first_word-> word[k] = wordes[k];
                                 table[index]= first_word;
                           }

                    }
             }

                else
            {
                    node* wordings = malloc(sizeof(node));

                         if (wordings==NULL)
                         {
                            return false;
                         }
                          wordings->next= NULL;


                    for (int j=0; j<LENGTH + 1; j++)
                    {
                             if (wordes[j]== '\0')
                            {
                              break;
                             }
                              else
                              {
                                wordings -> word[j] = wordes[j];
                              }
                     }

                  node* tmp= table[index];
                   wordings-> next= table[index];
                  table[index]= wordings;
                  wordings= tmp;



            }

         }


                fclose(file);
                return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (count < 0)
    {
        return 0;
    }
        else
        {
            return count;
        }

}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{

    for (int i=0; i< N; i++)
    {
        node *tmp = table[i];
       while (tmp!= NULL)
       {
            node *cursor = tmp->next;
            //cursor = tmp-> next;
            free (tmp);
            tmp = cursor;
       }
    }
   // for (int h=0; h < N; h++ )
    //{
      //  free(table[h]);

   // }
     free (wordes);
    // TODO
    return true;
}
