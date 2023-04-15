#include <stdio.h>

unsigned int hash(const char *word);
#define LENGTH 45
const unsigned int N = 26;

int main(void)
{
int number = hash("giancarlodelpierodelmiopiedesiuumdsadadasdasdatttttttttttttttttttrsddfffffffffffffdsdfsfsf");
printf ("%i\n", number);

}

unsigned int hash(const char *word)
{
    int n= word[0];
    //int l=0;
    for (int i=0; i< LENGTH + 1; i++)
     {
        while (&(word[i]) != NULL)
        {
            while (word[i]!= '\0')
          {
                //l= 'z';
               // n= l-word[i];
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