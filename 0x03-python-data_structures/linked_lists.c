#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head
 *
 * Return: Number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *curr;
	unsigned int n;

	curr = h;
	n = 0;
	while (curr != NULL)
	{
		printf("%i\n", curr->n);
		curr = curr->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of the first node of listint_t list
 * @n: integer to be included in the new node
 *
 * Return: Address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *curr;

	curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (curr->next != NULL)
			curr = curr->next;
		curr->next = new;
	}

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to the list to be freed
 *
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *curr;

	while (head != NULL)
	{
		curr = head;
		head = head->next;
		free(curr);
	}
}
