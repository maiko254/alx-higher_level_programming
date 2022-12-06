#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to first node in list
 * @number: number to insert into list
 *
 * Return: NULL - if function fails
 *                Otherwise - a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (curr == NULL || curr->n >= number)
	{
		new->next = curr;
		*head = new;
		return (new);
	}

	while (curr && curr->next && curr->next->n < number)
		curr = curr->next;

	new->next = curr->next;
	curr->next = new;

	return (new);
}
