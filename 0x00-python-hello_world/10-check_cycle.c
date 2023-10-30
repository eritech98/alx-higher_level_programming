#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singlyist has a cyclet.
 * @list: head pointerlit
 * Return: 0 if there's no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		if (fast->next != NULL)
			fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	
	return (0);
}
