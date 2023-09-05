#include "lists.h"

/**
 * insert_node - inserts a num into a node
 * @head: pointer to a pointer to list
 * @number: num to be inserted
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ne, *cur, *p;

	ne = malloc(sizeof(listint_t));
	if (ne == NULL)
	{
		return (NULL);
	}
	ne->n = number;
	ne->next = NULL;
	cur = *head;
	p = NULL;
	while (cur != NULL && cur->n < number)
	{
		p = cur;
		cur = cur->next;
	}
	if (p == NULL)
	{
		ne->next = *head;
		*head = ne;
	}
	else
	{
		p->next = ne;
		ne->next = cur;
	}
	return (ne);
}
