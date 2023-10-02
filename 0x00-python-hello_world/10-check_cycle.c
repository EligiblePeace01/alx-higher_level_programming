#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 *
 * Description:
 * This function determines whether a given singly linked list
 * has a cycle or not.
 * It uses Floyd's cycle-finding algorithm,
 * where two pointers traverse the list,
 * one moving at twice the speed of the other.
 * If there's a cycle, the two pointers
 * will eventually meet at the same node.
 * If no cycle is found, they will reach the end of the list.
 *
 * Return:
 * 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p2;   /* Pointer that moves twice as fast */
	listint_t *prev; /* Pointer to track the previous position */

	p2 = list;       /* Initialize both pointers to the beginning */
	prev = list;

	while (list && p2 && p2->next)
	{
		list = list->next;         /* Move one step at a time */
		p2 = p2->next->next;       /* Move two steps at a time */

		if (list == p2)
		{
			list = prev;      /* Reset the 'list' pointer to the beginning */
			prev =  p2;         /* Update 'prev' to the current position */
			/* Traverse the list to find the node where the cycle begins */
			while (1)
			{
				p2 = prev;
				/**
				 * Move 'p2' until it reaches the end of the list or
				 * returns to the 'prev' position (indicating the cycle's start)
				 */
				while (p2->next != list && p2->next != prev)
				{
					p2 = p2->next;
				}

				/* If 'p2' reaches 'list', a cycle is found */
				if (p2->next == list)
					break;

				list = list->next;
			}
			return (1); /* Return 1 to indicate a cycle is detected */
		}
	}
	return (0); /* Return 0 to indicate no cycle is detected */
}
