#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *previous = NULL;

	while (node)
	{
		next = node->next;
		node->next = previous;
		previous = node;
		node = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temporary, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temporary = *head;
	while (temporary)
	{
		size++;
		temporary = temporary->next;
	}

	temporary = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temporary = temporary->next;

	if ((size % 2) == 0 && temporary->n != temporary->next->n)
		return (0);

	temporary = temporary->next->next;
	rev = reverse_listint(&temporary);
	mid = rev;

	temporary = *head;
	while (rev)
	{
		if (temporary->n != rev->n)
			return (0);
		temporary = temporary->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
