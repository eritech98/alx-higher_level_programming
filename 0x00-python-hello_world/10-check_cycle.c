#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singlyist has a cyclet.
 * @list: head pointerlit
 * Return: 0 if there's no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_e = list;
	listint_t *fast_e = list;

	while (slow_e != NULL && fast_e != NULL)
	{
		slow_e = slow_e->next;
		if (fast_e->next != NULL)
			fast_e = fast_e->next->next;
		if (slow_e == fast)
		{
			return (1);
		}
	}
	
	return (0);
}
