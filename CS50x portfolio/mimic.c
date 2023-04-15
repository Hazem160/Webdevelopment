#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>



int count_words(string Text);
int count_letters (string Text);
int count_sentences (string Text);

int main(void)
{

string Text= get_string("Text:");
int LETTERS = strlen(Text);
printf("Number of letters:%i\n",LETTERS);

int words = count_words(Text);
printf("%i\n",words);
float Letters= count_letters(Text);
float L= Letters/ words * 100;
printf ("Number of letters: %f\n",L);

printf("Letters per 100 words: %.3f\n",L);
float Sentences= count_sentences(Text);
float S= Sentences/ words * 100;
printf("Sentences per 100 words: %.3f\n",S);
int index = 0.0588 * L - 0.296 * S - 15.8;
printf("%i\n",index);

}

int count_letters (string Text)
{
    int letters=0;
for (int k=0, m=strlen(Text); k<m; k++)
 {
    if (isspace(Text[k])== true)
    {
       letters ++;
    }
    else {letters++;}
 }
 return letters;
}




int count_words(string Text)
{
    int words= 0;
    for (int j=0,l=strlen(Text);j<l; j++)
    {
        if (Text[j]==32 || isspace(Text[j])== true)
        {
words ++;
        }
    }
    return words;
}



int count_sentences(string Text)
{
int sentences= 0;

    for (int i=0,n=strlen(Text);i<n; i++)
    {

        if (Text[i] == 33|| Text[i]== 46 || Text[i]== 63)
        {
         sentences ++;
        }
    }
    return sentences;
}