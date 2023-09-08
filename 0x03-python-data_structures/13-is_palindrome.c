#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to head
 * Return: 1 if true 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *fa = *head;
	listint_t *sl = *head;
	listint_t *pr = NULL;
	listint_t *tem;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (fa != NULL && fa->next == NULL)
	{
		fa = fa->next->next;
		tem = sl->next;
		sl->next = pr;
		pr = sl;
		sl = tem;
	}
	if (fa != NULL)
	{
		sl = sl->next;
	}
	while (pr != NULL)
	{
		if (pr->n != sl->n)
		{
			return (0);
		}
		pr = pr->next;
		sl = sl->next;
	}
	return (1);
}
