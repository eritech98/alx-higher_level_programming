#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: pointer to the head pointer of the list
 * Return: 0 if it's not a palindrome, 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	int len = 0;
	int index = 0;
	int mid = 0;
	int beg = 0;
	int end = 0;
	int *array = malloc(sizeof(int));

	if (*head == NULL)
		return (1);

	while (p != NULL)
	{
		array[index] = p->n;
		index++;
		p = p->next;
		len++;
		array = realloc(array, sizeof(int) * (len + 1));
	}

	end = len - 1;

	if (len % 2 == 0)
		mid = (len / 2) - 1;
	else
		mid = (len / 2);
	while (beg <= mid)
	{
		if (array[beg] != array[end])
			return (0);
		beg++;
		end--;
	}
	free(array);
	return (1);
}
