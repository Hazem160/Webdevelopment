#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{

    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;


    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;


    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;


    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;


    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("Total number of coins: %i\n", coins);
}

int get_cents(void)
{
int cents;
    do {
    cents= get_int ("How many cents are you owed:");
    }
    while (cents<=0); // TODO
    return cents;
}

int calculate_quarters(int cents)
{
    int quarters = cents/25;
    printf("Number of quarters: %i\n",quarters);
    // TODO
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes= cents/10;
    printf("Number of dimes: %i\n",dimes);
    // TODO
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels= cents/5;
     printf("Number of nickels: %i\n",nickels);
    // TODO
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies= cents/1;
    printf("Number of pennies: %i\n",pennies);
    // TODO
    return pennies;
}
