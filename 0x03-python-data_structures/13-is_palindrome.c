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
	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	return (che_p(head, *head));
}
/**
 * che_p - check if palindrome
 * @head: ptr to start
 * @last: ptr to end
 * Return: 0
 */
int che_p(listint_t **head, listint_t *last)
{
	if (last == NULL)
	{
		return (1);
	}
	if (che_p(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
