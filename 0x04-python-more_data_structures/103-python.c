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
	Py_ssize_t s, a;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
		s = PyBytes_Size(p);
		printf(" size: %ld\n", s);
		printf(" trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		printf(" first %ld bytes:", (s < 10 ? s : 10));
		for (a = 0; a < s && a < 10; a++)
		{
			printf("%02x ", (unsigned char)(((PyBytesObject *)p)->ob_sval[a]));
		}
		printf("\n");
}
/**
 * print_python_list - print list
 * @p: object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s, a;
	PyObject *try;

	s = ((PyVarObject *)p)->ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
	for (a = 0; a < s; a++)
	{
		try = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((PyObject *)try)->ob_type->tp_name);
		if (PyBytes_Check(try))
			print_python_bytes(try);
	}
}
