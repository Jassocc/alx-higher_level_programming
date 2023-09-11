#include <Python.h>

/**
 * print_python_list_info - prints info on pythonlists
 * @p: object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t siz, i;
	PyObject *it;

	siz = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", siz);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < siz; i++)
	{
		it = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(it)->tp_name);
	}
}
