#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (vote(name) == 1 )
        {
            printf("Invalid vote.\n");
            voter_count ++;
        }
else if (!strcmp(name, candidates[0].name))
        {
            candidates[0].votes+= 1 ;
        }
else {
            candidates[1].votes+= 1;
      }


    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name){
 if (strcmp(name, candidates[0].name)==0)

   { return 0;}

    else if (strcmp(name, candidates[1].name)==0)
    {return 0;}

    else{ return 1;}
    }


// Print the winner (or winners) of the election
void print_winner(void)
{
if (candidates[0].votes> candidates[1].votes)
{
    printf ("%s won!\n",candidates[0].name);
}

    else if (candidates[0].votes== candidates[1].votes)
    {
        printf("%s\n", candidates[0].name);
        printf ("%s tied!\n", candidates[1].name);
    }
else printf ("%s won!\n", candidates[1].name);
    return;
}