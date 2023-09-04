#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - check if the list has a cycle
 * @list: linked list to check
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list, *s = list;

	if (!list)
	{
		return (0);
	}
	while (1)
	{
		if (f->next != NULL && f->next->next != NULL)
		{
			f = f->next->next;
			s = s->next;
			if (f == s)
			{
				return (1);
			}
		}
		else
		{
			return (0);
		}
	}
}
