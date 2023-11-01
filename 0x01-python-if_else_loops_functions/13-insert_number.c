#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head pointer of the list.
 * @number: data for the new node.
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *ptr;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL || head == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	temp = *head;
	ptr = temp->next;
	if (ptr == NULL)
	{
		if (new->n > temp->n)
			temp->next = new;
		else
		{
			new->next = temp;
			*head = new;
		}
	}
	else
	{
		if (new->n < temp->n)
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		while (ptr != NULL)
		{
			if (new->n > ptr->n)
			{
				temp = ptr;
				ptr = ptr->next;
			}
			else
			{
				temp->next = new;
				new->next = ptr;
				break;
			}
		}
		if (ptr == NULL)
			temp->next = new;
	}
	return (new);
}
