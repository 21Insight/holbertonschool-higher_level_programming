#include "lists.h"

/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */

void reverse(listint_t **h_r)
{
	listint_t *prv;
	listint_t *crr;
	listint_t *nxt;

	prv = NULL;
	crr = *h_r;

	while (crr != NULL)
	{
		nxt = crr->next;
		crr->next = prv;
		prv = crr;
		crr = nxt;
	}

	*h_r = prv;
}

/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *SLW, *FS, *P_SLW;
	listint_t *scn_half, *MDL;
	int ASP;

	SLW = FS = P_SLW = *head;
	MDL = NULL;
	ASP = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (FS != NULL && FS->next != NULL)
		{
			FS = FS->next->next;
			P_SLW = SLW;
			SLW = SLW->next;
		}

		if (FS != NULL)
		{
			MDL = SLW;
			SLW = SLW->next;
		}

		scn_half = SLW;
		P_SLW->next = NULL;
		reverse(&scn_half);
		ASP = compare(*head, scn_half);

		if (MDL != NULL)
		{
			P_SLW->next = MDL;
			MDL->next = scn_half;
		}
		else
		{
			P_SLW->next = scn_half;
		}
	}

	return (ASP);
}
