#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - prints bytes on python
 * @p: object
 */
void print_python_bytes(PyObject *p)
{
	long int s;
	int a;
	char *try = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
		PyBytes_AsStringAndSize(p, &try, &s);
		printf(" size: %li\n", s);
		printf(" trying string: %s\n", try);
		if (s < 10)
		{
		printf(" first %li bytes:", (s + 1);
		}
		else
		{
			printf(" first 10 bytes:");
		}
		for (a = 0; a < s && a < 10; a++)
		{
			printf(" %02hhx", try[a]);
		}
		printf("\n");
}
/**
 * print_python_list - print list
 * @p: object
 */
void print_python_list(PyObject *p)
{
	long int s = PyList(p);
	int a;
	PyListObject *l = (PyListObject *)p;
	const char *t;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", list->allocated);
	for (a = 0; a < s; a++)
	{
		t = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, t);
		if (!strcmp(t, "bytes"))
			print_python_bytes(l->ob_item[a]);
	}
}
