#include <stdio.h>
#include <Python.h>
/**
 * print_python_list - prints list of python
 * @p: object to print
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t a, all, si;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *va = (PyVarObject *)p;
	const char *ty;

	si = va->ob_size;
	all = list->allocated;
	fflush(stdout);
	printf("[*] Python list\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", si);
	printf("[*] Allocated = %ld\n", all);
	for (a = 0; a < si; a++)
	{
		ty = list->ob_item[a]->ob_type->tp_name;
		printf("Element %ld: %s\n", a, ty);
		if (strcmp(ty, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[a]);
		}
		else if (strcmp(ty, "float") == 0)
		{
			print_python_float(list->ob_item[a]);
		}
	}
}
/**
 * print_python_bytes - print python info
 * @p: A byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t si, a;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
	{
		si = 10;
	}
	else
	{
		si = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %ld bytes: ", si);
	for (a = 0; a < si; a++)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (si - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
/**
 * print_python_float - prints python info
 * @p: float object
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;
	PyFloatObject *f = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buff = PyOS_double_to_string(fl->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}
