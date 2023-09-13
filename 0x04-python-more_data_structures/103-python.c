#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - print list
 * @p: object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s, a;
	PyObject *elem;

	s = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (a = 0; a < s; a++)
	{
		elem = PyList_Get_Item(p, i);
		printf("Element %ld: %s\n", a, Py_TYPE(elem)->tp_name);
	}
}
/**
 * print_python_bytes - prints bytes on python
 * @p: object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s, a;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		s = PyBytes_Size(p);
		printf(" size: %ld\n", s);
		printf(" trying string: %s\n", PyBytes_AsString(p));
		printf("[*] first %ld bytes:" (s < 10 ? s + 1 : 10));
		for (a = 0; a < s && a < 10; a++)
		{
			printf(" %02x", (unsigned char)PyBytes_AsString(p)[a]);
		}
		if (s < 10)
		{
			printf(" %02x", (unsigned char)PyBytes_AsString(p)[a]);
		}
		printf("\n");
	}
	else
	{
		printf(" [ERROR] Invalid Bytes Object\n");
	}
}
